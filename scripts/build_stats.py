#!/usr/bin/env python3
"""
Автогенерация статистики курса. Считает метрики прямо из Markdown и пишет STATS.md.

Запуск из корня репозитория:
    python scripts/build_stats.py

Пересоздавай перед релизом (см. RELEASE_CHECKLIST.md) — цифры всегда будут точными.
"""
import json
import re
import sys
from pathlib import Path

# Windows-консоль (cp1251) падает на кириллице — форсируем UTF-8
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "STATS.md"

DAY_RE = re.compile(r"^###\s+(?:День|Рӯзи)\s+\d+", re.M)
WEEK_RE = re.compile(r"^##\s+(?:Неделя|Ҳафтаи)\s+\d+", re.M)
URL_RE = re.compile(r"https?://[^\s)\]]+")

# маркеры блоков дня
MARK = {
    "theory": ("📺", "📖"),
    "practice": ("💻",),
    "task": ("✍️",),
    "check": ("🎯",),
}


def read(p):
    return p.read_text(encoding="utf-8") if p.exists() else ""


def count_marker(text, markers):
    n = 0
    for line in text.splitlines():
        s = line.lstrip()
        if s.startswith("- "):
            body = s[2:].lstrip()
            if any(body.startswith(m) for m in markers):
                n += 1
    return n


def lang_present(code):
    return (ROOT / code / "month-01-networks-linux.md").exists()


def collect_course(code):
    """Метрики по одному языку (по умолчанию считаем каноничный ru)."""
    files = sorted((ROOT / code).glob("month-*.md"))
    joined = "\n".join(read(f) for f in files)
    urls = set()
    for f in (ROOT / code).glob("*.md"):
        urls.update(URL_RE.findall(read(f)))
    return {
        "months": len(files),
        "days": len(DAY_RE.findall(joined)),
        "weeks": len(WEEK_RE.findall(joined)),
        "theory": count_marker(joined, MARK["theory"]),
        "practice": count_marker(joined, MARK["practice"]),
        "tasks": count_marker(joined, MARK["task"]),
        "checks": count_marker(joined, MARK["check"]),
        "resources": len(urls),
    }


def count_exams():
    txt = read(ROOT / "ru" / "exams.md")
    return len(re.findall(r"^##\s+.*Экзамен\s+\d+", txt, re.M))


def count_projects():
    txt = read(ROOT / "ru" / "projects.md")
    return len(re.findall(r"^##\s+\d+\.", txt, re.M))


def count_quizzes():
    d = ROOT / "checks"
    if not d.is_dir():
        return 0
    n = 0
    for p in d.glob("month-*.json"):
        try:
            n += len(json.loads(p.read_text(encoding="utf-8")).get("checks", []))
        except Exception:
            pass
    return n


def count_videos():
    p = ROOT / "videos" / "videos.json"
    if not p.exists():
        return 0
    try:
        raw = json.loads(p.read_text(encoding="utf-8"))
        return len(raw.get("videos", [])) + len(raw.get("playlists", []))
    except Exception:
        return 0


def count_ctf():
    try:
        data = json.loads(read(ROOT / "challenges" / "challenges.json"))
        return len(data.get("challenges", []))
    except Exception:
        return 0


def count_templates():
    d = ROOT / "templates"
    if not d.is_dir():
        return 0
    files = list(d.glob("*.md")) + list(d.glob("*.yml"))
    return len([f for f in files if f.name.lower() != "readme.md"])


def count_interview_qs():
    txt = read(ROOT / "ru" / "interview-questions.md")
    return len(re.findall(r"^\*\*\d+\.", txt, re.M))


def count_md_lines():
    total = 0
    for f in ROOT.rglob("*.md"):
        if ".git" in f.parts:
            continue
        total += len(read(f).splitlines())
    return total


def get_version():
    v = read(ROOT / "VERSION").strip()
    return v or "—"


def main():
    langs = [c for c in ("ru", "tg") if lang_present(c)]
    course = collect_course("ru") if "ru" in langs else collect_course(langs[0])

    stats = {
        "version": get_version(),
        "languages": len(langs),
        "languages_list": langs,
        "months": course["months"],
        "days": course["days"],
        "weeks": course["weeks"],
        "practice_blocks": course["practice"],
        "theory_blocks": course["theory"],
        "assignments": course["tasks"],
        "self_checks": course["checks"],
        "external_resources": course["resources"],
        "exams": count_exams(),
        "projects": count_projects(),
        "badges": 13,
        "quizzes": count_quizzes(),
        "videos": count_videos(),
        "ctf_challenges": count_ctf(),
        "templates": count_templates(),
        "interview_questions": count_interview_qs(),
        "markdown_lines": count_md_lines(),
    }

    rows = [
        ("📅 Учебных дней", stats["days"]),
        ("🗓 Месяцев", stats["months"]),
        ("📆 Недель", stats["weeks"]),
        ("💻 Практических блоков (лаб. работ)", stats["practice_blocks"]),
        ("📺 Блоков теории", stats["theory_blocks"]),
        ("✍️ Заданий на закрепление", stats["assignments"]),
        ("🎯 Вопросов самопроверки", stats["self_checks"]),
        ("🔗 Внешних ресурсов (уник. ссылок)", stats["external_resources"]),
        ("📝 Экзаменов", stats["exams"]),
        ("🛠 Портфолио-проектов", stats["projects"]),
        ("🏅 Бейджей достижений", stats["badges"]),
        ("❓ Проверочных тестов (по дням)", stats["quizzes"]),
        ("🎬 Встроенных видео и плейлистов", stats["videos"]),
        ("🚩 CTF-заданий", stats["ctf_challenges"]),
        ("📄 Шаблонов документов", stats["templates"]),
        ("🎤 Вопросов к собеседованию", stats["interview_questions"]),
        ("🌍 Языков", stats["languages"]),
        ("📖 Строк в Markdown", stats["markdown_lines"]),
    ]

    lines = [
        "# 📊 Статистика курса",
        "",
        "> Автогенерация: `python scripts/build_stats.py`. Не редактируй вручную.",
        f"> Версия курса: **{stats['version']}** · Языки: **{', '.join(stats['languages_list'])}**",
        "",
        "| Метрика | Значение |",
        "|---|---:|",
    ]
    for label, val in rows:
        lines.append(f"| {label} | **{val}** |")
    lines += [
        "",
        "---",
        "",
        "Метрики считаются напрямую из учебных файлов (`ru/`), заданий "
        "(`challenges/challenges.json`) и шаблонов — поэтому всегда актуальны. "
        "Пересобирай перед каждым релизом (см. [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md)).",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")

    # ASCII-only консольный вывод
    print(f"OK -> STATS.md (version {stats['version']})")
    for label, val in rows:
        ascii_label = label.encode("ascii", "ignore").decode().strip() or label
        print(f"  {val:>6}  {ascii_label}")


if __name__ == "__main__":
    main()
