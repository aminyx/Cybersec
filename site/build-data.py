#!/usr/bin/env python3
"""
Генератор данных для сайта курса.

Парсит ru/month-*.md и tg/month-*.md, извлекает месяцы, недели, дни
(с блоками теория/практика/задание/проверка) и записывает site/data.js.

Запуск из корня репозитория:
    python site/build-data.py

Пересоздавай после любой правки учебных файлов, чтобы сайт был в синхроне.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = Path(__file__).resolve().parent

# Маркеры блоков внутри дня: emoji -> ключ
BLOCK_MARKERS = {
    "📺": "theory",
    "📖": "theory",
    "💻": "practice",
    "✍️": "task",
    "🎯": "check",
}

RES_HEAD_RE = re.compile(r"^\*\*(?:Главные ресурсы месяца|Захираҳои асосии моҳ):\*\*")
MONTH_RE = re.compile(r"^#\s+(?:Месяц|Моҳи)\s+(\d+)\s*[—–-]\s*(.+)$")
WEEK_RE = re.compile(r"^##\s+(?:Неделя|Ҳафтаи)\s+(\d+)\s*[—–-]\s*(.+)$")
DAY_RE = re.compile(r"^###\s+(?:День|Рӯзи)\s+(\d+)\s*[—–-]\s*(.+)$")
GOAL_RE = re.compile(r"^\*\*(?:Цель месяца|Мақсади моҳ):\*\*\s*(.+)$")


def strip_md(text: str) -> str:
    """Чистит markdown, НО СОХРАНЯЕТ ссылки [текст](url) — сайт делает их кликабельными.
    Раньше ссылки вырезались, и студент видел «видео из плейлиста» без самого плейлиста."""
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)          # жирный
    text = re.sub(r"`([^`]+)`", r"\1", text)                # код
    return text.strip()


def extract_links(text: str):
    """Список ссылок дня: [{title, url}] — для отдельного блока «Материалы»."""
    out, seen = [], set()
    for title, url in re.findall(r"\[([^\]]+)\]\((https?://[^)]+)\)", text):
        url = url.strip()
        if url in seen:
            continue
        seen.add(url)
        item = {"title": title.strip(), "url": url}
        # ссылка на ПОИСК YouTube — не конкретное видео; помечаем, чтобы сайт
        # не выдавал её за готовый материал
        if "youtube.com/results" in url:
            item["search"] = True
        out.append(item)
    return out


def parse_month_file(path: Path):
    """Разбирает один файл месяца -> dict."""
    month = {"num": None, "title": "", "goal": "", "weeks": [], "days": [], "resources": []}
    cur_week = None
    cur_day = None
    in_resources = False

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()

        # блок «Главные ресурсы месяца» — запасные материалы для дней без своих ссылок
        if RES_HEAD_RE.match(line):
            in_resources = True
            continue
        if in_resources:
            if line.startswith("- "):
                month["resources"] += extract_links(line)
                continue
            if line.strip():
                in_resources = False

        m = MONTH_RE.match(line)
        if m:
            month["num"] = int(m.group(1))
            month["title"] = strip_md(m.group(2))
            continue

        g = GOAL_RE.match(line)
        if g and not month["goal"]:
            month["goal"] = strip_md(g.group(1))
            continue

        w = WEEK_RE.match(line)
        if w:
            cur_week = {"num": int(w.group(1)), "title": strip_md(w.group(2))}
            month["weeks"].append(cur_week)
            cur_day = None
            continue

        d = DAY_RE.match(line)
        if d:
            cur_day = {
                "num": int(d.group(1)),
                "title": strip_md(d.group(2)),
                "week": cur_week["num"] if cur_week else None,
                "theory": "",
                "practice": "",
                "task": "",
                "check": "",
                "links": [],
                "raw": "",   # временное поле для сбора ссылок, удаляется ниже
            }
            month["days"].append(cur_day)
            continue

        # Блоки внутри дня
        if cur_day and line.startswith("- "):
            body = line[2:].strip()
            cur_day["raw"] += body + "\n"
            for emoji, key in BLOCK_MARKERS.items():
                if body.startswith(emoji):
                    # первый непустой блок этого типа побеждает
                    if not cur_day[key]:
                        cur_day[key] = strip_md(body[len(emoji):].strip())
                    break

    # собрать ссылки дня и убрать временное поле
    for d in month["days"]:
        d["links"] = extract_links(d.pop("raw", ""))

    return month


def collect(lang_dir: Path):
    months = []
    for path in sorted(lang_dir.glob("month-*.md")):
        m = parse_month_file(path)
        if m["num"] is None:
            print(f"  ! пропущен (нет заголовка месяца): {path.name}", file=sys.stderr)
            continue
        m["file"] = path.name
        months.append(m)
    months.sort(key=lambda x: x["num"])
    return months


def load_quizzes(lang="ru"):
    """Тесты для языка. Русские лежат в checks/, переводы — в checks/<lang>/.
    Если перевода дня нет, берётся русский оригинал (плавная деградация:
    студент всегда получает проверку, даже если перевод ещё не сделан)."""
    base = ROOT / "checks"
    if not base.is_dir():
        print("! папки checks/ нет — тесты не будут добавлены", file=sys.stderr)
        return {}

    def read_dir(d):
        out = {}
        for p in sorted(d.glob("month-*.json")):
            try:
                raw = json.loads(p.read_text(encoding="utf-8"))
            except Exception as e:
                print(f"! {p.name} невалиден: {e}", file=sys.stderr)
                continue
            for item in raw.get("checks", []):
                out[int(item["d"])] = item
        return out

    quizzes = read_dir(base)                     # русские — основа
    if lang != "ru":
        tr = read_dir(base / lang) if (base / lang).is_dir() else {}
        quizzes = {**quizzes, **tr}              # перевод перекрывает оригинал
        if tr:
            print(f"  {lang}: переведённых тестов {len(tr)}/{len(quizzes)}")
    return quizzes


def load_videos():
    """videos/videos.json -> ({день: [видео]}, {месяц: [плейлисты]})."""
    p = ROOT / "videos" / "videos.json"
    if not p.exists():
        print("! videos/videos.json не найден — видео не будут добавлены", file=sys.stderr)
        return {}, {}
    try:
        raw = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"! videos.json невалиден: {e}", file=sys.stderr)
        return {}, {}

    by_day = {}
    for v in raw.get("videos", []):
        by_day.setdefault(int(v["d"]), []).append(
            {"yt": v["yt"], "t": v.get("t", ""), "a": v.get("a", ""), "min": v.get("min"), "kind": "video"}
        )
    by_month = {}
    for pl in raw.get("playlists", []):
        for m in pl.get("months", []):
            by_month.setdefault(int(m), []).append(
                {"yt": pl["yt"], "t": pl.get("t", ""), "a": pl.get("a", ""), "kind": "playlist"}
            )
    return by_day, by_month


def main():
    vid_day, vid_month = load_videos()
    data = {}
    for lang in ("ru", "tg"):
        lang_dir = ROOT / lang
        if not lang_dir.is_dir():
            print(f"! нет папки {lang}/ — пропускаю", file=sys.stderr)
            continue
        months = collect(lang_dir)
        quizzes = load_quizzes(lang)   # тесты на языке студента (с откатом на русский)
        with_quiz = with_video = 0
        for m in months:
            m["videos"] = vid_month.get(m["num"], [])
            for d in m["days"]:
                qz = quizzes.get(d["num"])
                if qz:
                    d["quiz"] = {"q": qz["q"], "o": qz["o"], "a": qz["a"], "e": qz["e"]}
                    with_quiz += 1
                vids = vid_day.get(d["num"], [])
                if vids:
                    d["videos"] = vids
                    with_video += 1
        total_days = sum(len(m["days"]) for m in months)
        links_total = sum(len(d["links"]) for m in months for d in m["days"])
        data[lang] = months
        print(f"{lang}: months={len(months)} days={total_days} links={links_total} "
              f"quizzes={with_quiz} days_with_video={with_video}")

    # Отдельный файл на язык: студент качает только свой (раньше один файл вёз оба ~700 КБ)
    head = ("// АВТОГЕНЕРАЦИЯ — не редактируй вручную.\n"
            "// Пересоздать: python site/build-data.py\n"
            "window.COURSE_DATA = window.COURSE_DATA || {};\n")
    total = 0
    for lang, months in data.items():
        path = OUT_DIR / f"data-{lang}.js"
        body = (head + f"window.COURSE_DATA.{lang} = "
                + json.dumps(months, ensure_ascii=False, separators=(",", ":")) + ";\n")
        path.write_text(body, encoding="utf-8")
        kb = path.stat().st_size / 1024
        total += kb
        print(f"OK -> {path.relative_to(ROOT)} ({kb:.0f} KB)")

    # Список доступных языков — грузится первым, чтобы app.js знал, что подтягивать
    idx = OUT_DIR / "data-index.js"
    idx.write_text(head + "window.COURSE_LANGS = "
                   + json.dumps(sorted(data.keys())) + ";\n", encoding="utf-8")
    print(f"OK -> {idx.relative_to(ROOT)} (итого данных {total:.0f} KB, "
          f"на язык ~{total / max(len(data), 1):.0f} KB)")

    # Старый общий файл больше не нужен
    legacy = OUT_DIR / "data.js"
    if legacy.exists():
        legacy.unlink()
        print("removed legacy site/data.js")


if __name__ == "__main__":
    main()
