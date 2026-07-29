#!/usr/bin/env python3
"""
Проверка знаний по дням курса из терминала (для тех, кто учится по файлам, а не через сайт).

    python checks/quiz.py 1          # пройти проверку за день 1
    python checks/quiz.py 1-7        # проверка по диапазону дней
    python checks/quiz.py --random 5 # 5 случайных вопросов из пройденных тем
    python checks/quiz.py --stats    # прогресс

Результаты сохраняются в checks/.passed (в .gitignore, у каждого свой).
"""
import argparse
import json
import random
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

HERE = Path(__file__).resolve().parent
PASSED = HERE / ".passed"

G = "\033[32m"; R = "\033[31m"; Y = "\033[33m"; DIM = "\033[2m"; B = "\033[1m"; X = "\033[0m"
if sys.platform == "win32":
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11), 7)
    except Exception:
        G = R = Y = DIM = B = X = ""


def load_all():
    out = {}
    for p in sorted(HERE.glob("month-*.json")):
        for c in json.loads(p.read_text(encoding="utf-8")).get("checks", []):
            out[int(c["d"])] = c
    return out


def passed_set():
    if PASSED.exists():
        return {int(x) for x in PASSED.read_text(encoding="utf-8").split() if x.strip().isdigit()}
    return set()


def mark(day):
    s = passed_set(); s.add(day)
    PASSED.write_text("\n".join(str(d) for d in sorted(s)), encoding="utf-8")


def ask(check):
    """Задаёт один вопрос. Возвращает True при верном ответе."""
    print(f"\n{DIM}День {check['d']}{X}")
    print(f"{B}{check['q']}{X}\n")
    for i, opt in enumerate(check["o"]):
        print(f"  {B}{chr(65 + i)}{X}) {opt}")

    while True:
        try:
            raw = input(f"\n{Y}Твой ответ (A/B/C/D, q — выход):{X} ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            print("\nВыход."); sys.exit(0)
        if raw == "Q":
            sys.exit(0)
        if len(raw) == 1 and "A" <= raw <= chr(64 + len(check["o"])):
            idx = ord(raw) - 65
            break
        print(f"{R}Введи букву варианта.{X}")

    if idx == check["a"]:
        print(f"\n{G}{B}Верно!{X} {check['e']}")
        mark(check["d"])
        return True
    right = chr(65 + check["a"])
    print(f"\n{R}Неверно.{X} Правильный ответ: {B}{right}{X}. {check['e']}")
    return False


def parse_days(spec):
    if "-" in spec:
        a, b = spec.split("-", 1)
        return list(range(int(a), int(b) + 1))
    return [int(spec)]


def main():
    ap = argparse.ArgumentParser(description="Проверка знаний по дням курса")
    ap.add_argument("days", nargs="?", help="день или диапазон, например 1 или 1-7")
    ap.add_argument("--random", type=int, metavar="N", help="N случайных вопросов")
    ap.add_argument("--stats", action="store_true", help="показать прогресс")
    args = ap.parse_args()

    all_checks = load_all()
    if not all_checks:
        sys.exit("Нет файлов checks/month-*.json")

    if args.stats:
        p = passed_set()
        print(f"\nПройдено проверок: {B}{len(p)}/{len(all_checks)}{X}")
        if p:
            print(f"{DIM}Последний сданный день: {max(p)}{X}")
        print()
        return

    if args.random:
        pool = random.sample(sorted(all_checks), min(args.random, len(all_checks)))
        days = pool
    elif args.days:
        days = parse_days(args.days)
    else:
        ap.print_help()
        return

    ok = 0
    asked = 0
    for d in days:
        c = all_checks.get(d)
        if not c:
            print(f"{R}Нет проверки для дня {d}.{X}")
            continue
        asked += 1
        if ask(c):
            ok += 1

    if asked:
        pct = round(ok / asked * 100)
        color = G if pct >= 80 else (Y if pct >= 50 else R)
        print(f"\n{B}Итог:{X} {color}{ok}/{asked} ({pct}%){X}")
        if pct < 80:
            print(f"{DIM}Меньше 80% — вернись к материалам этих дней.{X}")
        print()


if __name__ == "__main__":
    main()
