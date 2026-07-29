#!/usr/bin/env python3
"""
Валидатор репозитория. Проверяет целостность до мёржа PR.

Что проверяет:
  - внутренние markdown-ссылки резолвятся (битые файлы = ошибка);
  - локальные изображения существуют;
  - обязательные файлы и папки на месте;
  - паритет месяцев ru/ ↔ tg/;
  - валидность challenges.json (JSON) и наличие полей;
  - якоря (#...) в ссылках на .md — предупреждение, если не найдены.

Внешние ссылки (http/https/mailto) НЕ проверяются (флаки в CI по сети).
Ссылки внутри блоков кода игнорируются.

Запуск:  python scripts/check_repo.py
Код возврата: 0 — всё ок; 1 — есть ошибки.
"""
import json
import re
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "README.md", "LICENSE", "VERSION", "CHANGELOG.md", "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md", "SECURITY.md", "ARCHITECTURE.md", "STATS.md",
    "ru/README.md", "tg/README.md",
    "site/index.html", "site/app.js", "site/styles.css", "site/build-data.py",
    "challenges/check.py", "challenges/challenges.json",
    "scripts/build_stats.py",
    ".github/workflows/project-check.yml",
]
REQUIRED_DIRS = ["ru", "tg", "site", "challenges", "templates", "docs", "assets", "scripts"]

FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$", re.M)

errors, warnings = [], []


def strip_code(text):
    text = FENCE_RE.sub("", text)
    text = INLINE_CODE_RE.sub("", text)
    return text


def gh_slug(heading):
    s = heading.strip().lower()
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)   # ссылки -> текст
    s = re.sub(r"[*_`]", "", s)                        # эмфазис
    out = []
    for ch in s:
        if ch.isalnum() or ch in ("-", "_"):
            out.append(ch)
        elif ch.isspace():
            out.append("-")
        # прочее (пунктуация, эмодзи) отбрасывается
    return re.sub(r"-+", "-", "".join(out)).strip("-")


def anchors_of(path):
    try:
        txt = path.read_text(encoding="utf-8")
    except Exception:
        return set()
    return {gh_slug(h) for h in HEADING_RE.findall(txt)}


def is_external(target):
    return target.startswith(("http://", "https://", "mailto:", "tel:", "data:", "//"))


def check_links():
    md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    anchor_cache = {}

    for md in md_files:
        rel = md.relative_to(ROOT)
        try:
            raw = md.read_text(encoding="utf-8")
        except Exception as e:
            errors.append(f"{rel}: не читается ({e})")
            continue
        text = strip_code(raw)

        # изображения (локальные)
        for src in IMG_RE.findall(text):
            src = src.split()[0].strip()  # убрать возможный title
            if is_external(src) or src.startswith("#"):
                continue
            tgt = (md.parent / src.split("#")[0]).resolve()
            if not tgt.exists():
                errors.append(f"{rel}: битое изображение -> {src}")

        # ссылки
        for target in LINK_RE.findall(text):
            target = target.split()[0].strip()  # убрать title в кавычках
            if is_external(target):
                continue
            if target.startswith("#"):
                # якорь в этом же файле
                anchors = anchor_cache.setdefault(md, anchors_of(md))
                if gh_slug(target[1:]) not in anchors:
                    warnings.append(f"{rel}: якорь не найден -> {target}")
                continue
            path_part, _, anchor = target.partition("#")
            if not path_part:
                continue
            tgt = (md.parent / path_part).resolve()
            if not tgt.exists():
                errors.append(f"{rel}: битая ссылка -> {target}")
                continue
            if anchor and tgt.suffix == ".md":
                anchors = anchor_cache.setdefault(tgt, anchors_of(tgt))
                if gh_slug(anchor) not in anchors:
                    warnings.append(f"{rel}: якорь не найден -> {target}")


def check_structure():
    for f in REQUIRED_FILES:
        if not (ROOT / f).exists():
            errors.append(f"структура: нет обязательного файла {f}")
    for d in REQUIRED_DIRS:
        if not (ROOT / d).is_dir():
            errors.append(f"структура: нет обязательной папки {d}/")

    ru = sorted(p.name for p in (ROOT / "ru").glob("month-*.md"))
    tg = sorted(p.name for p in (ROOT / "tg").glob("month-*.md"))
    if ru != tg:
        errors.append(f"паритет месяцев ru/tg нарушен: ru={len(ru)} tg={len(tg)}")


def check_challenges():
    p = ROOT / "challenges" / "challenges.json"
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"challenges.json: невалидный JSON ({e})")
        return
    for c in data.get("challenges", []):
        for field in ("id", "title", "task", "flag_sha256"):
            if field not in c:
                errors.append(f"challenges.json: у задания нет поля '{field}'")
        h = c.get("flag_sha256", "")
        if not re.fullmatch(r"[0-9a-f]{64}", h):
            errors.append(f"challenges.json: {c.get('id')} — flag_sha256 не похож на SHA-256")


# Учебные ресурсы, которые ДОЛЖНЫ остаться на http:// — это не недосмотр:
#  · httpforever.com — нужен именно незашифрованный HTTP, чтобы увидеть трафик в Wireshark (день 5)
#  · flaws.cloud / flaws2.cloud — так их публикует автор учебного полигона AWS
ALLOWED_HTTP = {"http://httpforever.com", "http://flaws.cloud/", "http://flaws2.cloud/"}


def check_http_links():
    """Ловит новые http:// ссылки, кроме заведомо учебных."""
    for md in [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]:
        text = strip_code(md.read_text(encoding="utf-8"))
        for url in re.findall(r"\((http://[^)\s]+)\)", text):
            if url.rstrip("/") not in {u.rstrip("/") for u in ALLOWED_HTTP}:
                warnings.append(f"{md.relative_to(ROOT)}: ссылка по http:// -> {url} "
                                f"(если это учебная цель — добавь в ALLOWED_HTTP)")


def check_quizzes():
    """Проверки знаний: полнота (все 270 дней), корректность, отсутствие перекоса ответов."""
    d = ROOT / "checks"
    if not d.is_dir():
        errors.append("нет папки checks/ с проверочными тестами")
        return
    seen, spread = {}, {}
    for p in sorted(d.glob("month-*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"{p.name}: невалидный JSON ({e})")
            continue
        for c in data.get("checks", []):
            day = c.get("d")
            if day in seen:
                errors.append(f"checks: дубль дня {day} ({p.name} и {seen[day]})")
            seen[day] = p.name
            opts = c.get("o", [])
            if len(opts) < 2:
                errors.append(f"checks: день {day} — меньше двух вариантов")
            if len(set(opts)) != len(opts):
                errors.append(f"checks: день {day} — повторяющиеся варианты")
            if not isinstance(c.get("a"), int) or not 0 <= c["a"] < len(opts):
                errors.append(f"checks: день {day} — неверный индекс верного ответа")
            else:
                spread[c["a"]] = spread.get(c["a"], 0) + 1
            if not c.get("q") or not c.get("e"):
                errors.append(f"checks: день {day} — нет вопроса или объяснения")

    missing = sorted(set(range(1, 271)) - set(seen))
    if missing:
        warnings.append(f"checks: нет проверок для дней {missing[:10]}"
                        f"{' и ещё ' + str(len(missing) - 10) if len(missing) > 10 else ''}")

    # перекос: если >50% верных ответов на одной позиции, студент угадает паттерн
    if spread:
        top = max(spread.values())
        if top / sum(spread.values()) > 0.5:
            warnings.append("checks: верные ответы скучены на одной позиции — "
                            "запусти python scripts/shuffle_checks.py")


def main():
    check_structure()
    check_links()
    check_challenges()
    check_quizzes()
    check_http_links()

    for w in warnings:
        print(f"  WARN  {w}")
    for e in errors:
        print(f"  FAIL  {e}")

    print()
    print(f"Итог: {len(errors)} ошибок, {len(warnings)} предупреждений.")
    if errors:
        print("Репозиторий НЕ прошёл проверку.")
        sys.exit(1)
    print("OK: репозиторий валиден.")


if __name__ == "__main__":
    main()
