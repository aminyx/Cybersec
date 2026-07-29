# Linux / macOS Setup

Настройка окружения разработки/запуска на Linux и macOS.

## 1. Python

Обычно уже установлен. Проверь:
```bash
python3 --version
```
Если нет:
- Debian/Ubuntu: `sudo apt update && sudo apt install python3`
- Fedora: `sudo dnf install python3`
- macOS: `brew install python3`

## 2. Запуск сайта

Из корня репозитория:
```bash
python3 -m http.server 8129 --directory site
```
Открой `http://localhost:8129`.

## 3. Генераторы

```bash
python3 site/build-data.py       # пересобрать данные сайта
python3 scripts/build_stats.py   # пересобрать STATS.md
python3 scripts/check_repo.py    # проверить репозиторий
```

## 4. Сертификат (опционально)

```bash
python3 -m pip install fpdf2
python3 assets/generate_certificate.py --name "Имя Фамилия" --date "2027-04-25"
```

## 5. CTF

```bash
python3 challenges/check.py
python3 challenges/check.py w04-logs "CSC{...}"
```

Для задания w04 пригодятся стандартные утилиты (`grep`, `sort`, `uniq`) — на Linux они есть из коробки.

## 6. Виртуальное окружение (рекомендуется для инструментов)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

## 7. Docker (опционально)

```bash
docker compose up
```
Сайт на `http://localhost:8129`. Разовые команды:
```bash
docker compose run --rm tools python scripts/check_repo.py
```
См. [docker-compose.yml](../../docker-compose.yml).

## Примечание

В отличие от Windows, проблем с кодировкой консоли на Linux/macOS нет — терминал по умолчанию UTF-8.
