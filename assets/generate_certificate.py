#!/usr/bin/env python3
"""
Генератор сертификата об окончании курса Cybersecurity (self-study).

Установка:
    pip install fpdf2

Использование:
    python generate_certificate.py --name "Имя Фамилия" --date "2027-04-25"
    python generate_certificate.py --name "Имя Фамилия" --date "2027-04-25" \
        --machines 45 --projects 10 --writeups 60 --out my_cert.pdf

Результат: PDF-файл (по умолчанию certificate.pdf) в текущей папке.

Примечание: это сертификат самообучения — артефакт портфолио, а НЕ
аккредитованный отраслевой сертификат. Подробности — в ru/certificate.md.
"""

import argparse
import sys
from datetime import date


def build_certificate(name, completion_date, machines, projects, writeups, out_path):
    try:
        from fpdf import FPDF
    except ImportError:
        sys.exit(
            "Не найден модуль fpdf2. Установи его:\n    pip install fpdf2"
        )

    pdf = FPDF(orientation="L", unit="mm", format="A4")  # альбомная ориентация
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)

    w = pdf.w  # ширина страницы (297 мм)
    h = pdf.h  # высота страницы (210 мм)

    # --- Цвета ---
    dark = (20, 30, 48)      # тёмно-синий
    accent = (0, 150, 136)   # бирюзовый
    gray = (90, 90, 90)

    # --- Рамка ---
    pdf.set_draw_color(*accent)
    pdf.set_line_width(1.5)
    pdf.rect(10, 10, w - 20, h - 20)
    pdf.set_line_width(0.4)
    pdf.rect(14, 14, w - 28, h - 28)

    # --- Заголовок ---
    pdf.set_text_color(*gray)
    pdf.set_font("Helvetica", "", 16)
    pdf.set_y(30)
    pdf.cell(0, 10, "CERTIFICATE OF COMPLETION", align="C")

    # --- Название курса ---
    pdf.set_text_color(*dark)
    pdf.set_font("Helvetica", "B", 34)
    pdf.set_y(48)
    pdf.cell(0, 16, "CYBER SECURITY JUNIOR", align="C")

    # --- Линия под заголовком ---
    pdf.set_draw_color(*accent)
    pdf.set_line_width(0.8)
    pdf.line(w / 2 - 45, 70, w / 2 + 45, 70)

    # --- "This certifies that" ---
    pdf.set_text_color(*gray)
    pdf.set_font("Helvetica", "", 13)
    pdf.set_y(80)
    pdf.cell(0, 8, "This certifies that", align="C")

    # --- Имя ---
    pdf.set_text_color(*dark)
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_y(92)
    pdf.cell(0, 14, name, align="C")

    # --- Описание ---
    pdf.set_text_color(*gray)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_y(112)
    lines = [
        "successfully completed the 270-day Cybersecurity program:",
        "Foundations - Networking, Linux, Web, Pentest, Active Directory, Blue Team;",
        "Modern Stack - Cloud, Kubernetes, DevSecOps, Detection Engineering, AI/LLM Security, MCP.",
    ]
    for ln in lines:
        pdf.cell(0, 7, ln, align="C")
        pdf.ln(7)

    # --- Статистика ---
    pdf.set_text_color(*accent)
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_y(140)
    stats = f"270 days   |   6 exams   |   {projects} projects"
    if machines:
        stats += f"   |   {machines} machines"
    if writeups:
        stats += f"   |   {writeups} write-ups"
    pdf.cell(0, 8, stats, align="C")

    # --- Дата ---
    pdf.set_text_color(*dark)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_y(165)
    pdf.cell(0, 8, f"Date of completion: {completion_date}", align="C")

    # --- Подпись/футер ---
    pdf.set_text_color(*gray)
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_y(180)
    pdf.cell(
        0, 6,
        "Self-study completion certificate - portfolio artifact backed by GitHub write-ups, projects and exam reports.",
        align="C",
    )

    pdf.output(out_path)
    print(f"Сертификат создан: {out_path}")


def main():
    parser = argparse.ArgumentParser(description="Генератор сертификата курса Cybersecurity")
    parser.add_argument("--name", required=True, help="Твоё имя (как на сертификате)")
    parser.add_argument(
        "--date",
        default=str(date.today()),
        help="Дата окончания (YYYY-MM-DD). По умолчанию — сегодня",
    )
    parser.add_argument("--machines", type=int, default=0, help="Сколько машин пройдено (опц.)")
    parser.add_argument("--projects", type=int, default=10, help="Сколько проектов завершено")
    parser.add_argument("--writeups", type=int, default=0, help="Сколько write-up'ов (опц.)")
    parser.add_argument("--out", default="certificate.pdf", help="Имя выходного файла")
    args = parser.parse_args()

    build_certificate(
        name=args.name,
        completion_date=args.date,
        machines=args.machines,
        projects=args.projects,
        writeups=args.writeups,
        out_path=args.out,
    )


if __name__ == "__main__":
    main()
