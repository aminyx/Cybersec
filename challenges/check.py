#!/usr/bin/env python3
"""
Автопроверка CTF-флагов. Флаги хранятся только как SHA-256 — ответы подсмотреть нельзя.

Использование:
    python check.py                      # список заданий
    python check.py w01-base64           # показать задание и подсказки
    python check.py w01-base64 CSC{...}  # проверить флаг
    python check.py --score              # сколько решено (по локальному прогрессу)

Прогресс решённых задач хранится в challenges/.solved (в .gitignore).
"""
import hashlib
import json
import sys
from pathlib import Path

# Консоль Windows по умолчанию cp1251 и не печатает кириллицу/спецсимволы — форсируем UTF-8
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

HERE = Path(__file__).resolve().parent
DB = HERE / "challenges.json"
SOLVED = HERE / ".solved"

G = "\033[32m"; R = "\033[31m"; Y = "\033[33m"; DIM = "\033[2m"; B = "\033[1m"; X = "\033[0m"
if sys.platform == "win32":
    # включить ANSI-цвета в старых консолях Windows; при неудаче — без цвета
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11), 7)
    except Exception:
        G = R = Y = DIM = B = X = ""


def load():
    return json.loads(DB.read_text(encoding="utf-8"))["challenges"]


def solved_set():
    if SOLVED.exists():
        return set(SOLVED.read_text(encoding="utf-8").split())
    return set()


def mark_solved(cid):
    s = solved_set(); s.add(cid)
    SOLVED.write_text("\n".join(sorted(s)), encoding="utf-8")


def list_all():
    chs = load(); done = solved_set()
    print(f"\n{B}CTF-челленджи CyberSec Course{X}  ({len(done)}/{len(chs)} решено)\n")
    for c in chs:
        mark = f"{G}[x]{X}" if c["id"] in done else "[ ]"
        print(f"  {mark} {B}{c['id']}{X}  {c['title']}")
        print(f"      {DIM}~{c['minutes']} мин · доступно после Дня {c['after_day']}{X}")
    print(f"\n{DIM}Задание:  python check.py <id>{X}")
    print(f"{DIM}Ответ:    python check.py <id> 'CSC{{...}}'{X}\n")


def show(cid):
    c = next((x for x in load() if x["id"] == cid), None)
    if not c:
        print(f"{R}Нет задания с id '{cid}'.{X} Список: python check.py"); return
    print(f"\n{B}{c['title']}{X}  {DIM}({c['id']}, ~{c['minutes']} мин){X}\n")
    print(c["task"])
    print(f"\n{Y}Подсказки{X} {DIM}(открывай по одной, только если застрял){X}:")
    for i, h in enumerate(c["hints"], 1):
        print(f"  {DIM}{i}.{X} {h}")
    print(f"\n{DIM}Проверить: python check.py {c['id']} 'твой_флаг'{X}\n")


def check(cid, flag):
    c = next((x for x in load() if x["id"] == cid), None)
    if not c:
        print(f"{R}Нет задания '{cid}'.{X}"); return 1
    got = hashlib.sha256(flag.strip().encode()).hexdigest()
    if got == c["flag_sha256"]:
        mark_solved(cid)
        print(f"\n{G}{B}✔ Верно!{X} Задание {G}{cid}{X} решено. 🎉")
        d = len(solved_set()); tot = len(load())
        print(f"{DIM}Прогресс: {d}/{tot}. {'Все решены — красавчик!' if d==tot else 'Дальше: python check.py'}{X}\n")
        return 0
    print(f"\n{R}Неверно.{X} Проверь формат CSC{{...}} и попробуй ещё. "
          f"{DIM}Подсказки: python check.py {cid}{X}\n")
    return 1


def score():
    d = len(solved_set()); tot = len(load())
    bar = "█" * d + "░" * (tot - d)
    print(f"\nРешено: {B}{d}/{tot}{X}  {G}{bar}{X}\n")


def main():
    a = sys.argv[1:]
    if not a:
        list_all()
    elif a[0] == "--score":
        score()
    elif len(a) == 1:
        show(a[0])
    else:
        sys.exit(check(a[0], " ".join(a[1:])))


if __name__ == "__main__":
    main()
