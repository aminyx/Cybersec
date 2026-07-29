#!/usr/bin/env python3
"""
Детерминированно перемешивает варианты ответов в checks/month-*.json.

Зачем: при ручном написании тестов верный ответ неизбежно скапливается на одной
позиции. Студент замечает паттерн и жмёт её не думая — проверка обесценивается.
Скрипт циклически сдвигает варианты (сдвиг зависит от номера дня) и пересчитывает
индекс верного ответа, давая ровное распределение A/B/C/D.

Идемпотентность: сдвиг детерминирован, но повторный запуск снова сдвинет варианты.
Запускать осознанно после добавления новых тестов, затем проверить распределение.

Запуск:  python scripts/shuffle_checks.py [--dry-run]
"""
import json
import sys
from collections import Counter
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent
CHECKS = ROOT / "checks"


def rotate(check):
    """Сдвигает варианты на (номер дня % длина) и пересчитывает индекс ответа."""
    opts, ans, d = check["o"], check["a"], check["d"]
    n = len(opts)
    shift = d % n
    if shift == 0:
        return check, 0
    new = [None] * n
    for i, opt in enumerate(opts):
        new[(i + shift) % n] = opt
    check["o"] = new
    check["a"] = (ans + shift) % n
    return check, shift


def main():
    dry = "--dry-run" in sys.argv
    before, after = Counter(), Counter()
    total = 0

    # и русские (checks/), и переводы (checks/<lang>/)
    paths = sorted(CHECKS.glob("month-*.json"))
    for sub in sorted(d for d in CHECKS.iterdir() if d.is_dir()):
        paths += sorted(sub.glob("month-*.json"))

    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        for c in data["checks"]:
            before[c["a"]] += 1
            rotate(c)
            after[c["a"]] += 1
            total += 1
        if not dry:
            # аккуратный формат: одна проверка на строку, как в исходных файлах
            lines = ['{', f'  "_comment": {json.dumps(data.get("_comment", ""), ensure_ascii=False)},', '  "checks": [']
            for i, c in enumerate(data["checks"]):
                comma = "," if i < len(data["checks"]) - 1 else ""
                lines.append("    " + json.dumps(c, ensure_ascii=False, separators=(",", ":")) + comma)
            lines += ["  ]", "}", ""]
            path.write_text("\n".join(lines), encoding="utf-8")

    label = "DRY-RUN, ничего не записано" if dry else "файлы обновлены"
    print(f"Файлов обработано: {len(paths)}")
    print(f"Обработано тестов: {total} ({label})")
    print("Распределение ДО :", {k: before[k] for k in sorted(before)})
    print("Распределение ПОСЛЕ:", {k: after[k] for k in sorted(after)})


if __name__ == "__main__":
    main()
