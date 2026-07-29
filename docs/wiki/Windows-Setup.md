# Windows Setup

Настройка окружения разработки/запуска на Windows.

## 1. Python

Установи Python 3.8+ (рекомендуется 3.12):
```powershell
winget install Python.Python.3.12
```
Проверь:
```powershell
python --version
```

## 2. Запуск сайта

Из корня репозитория:
```powershell
python -m http.server 8129 --directory site
```
Открой `http://localhost:8129`.

## 3. Генераторы

```powershell
python site\build-data.py       # пересобрать данные сайта
python scripts\build_stats.py   # пересобрать STATS.md
python scripts\check_repo.py    # проверить репозиторий
```

## 4. Сертификат (опционально)

```powershell
pip install fpdf2
python assets\generate_certificate.py --name "Имя Фамилия" --date "2027-04-25"
```

## 5. CTF

```powershell
python challenges\check.py
python challenges\check.py w01-base64 "CSC{...}"
```

## ⚠️ Важно про кодировку консоли

Стандартная консоль Windows — cp1251, она не печатает часть Unicode. Наши скрипты форсируют UTF-8 сами. Если хочешь, чтобы кириллица корректно отображалась во всех программах:
```powershell
chcp 65001
```
(переключает консоль в UTF-8 на текущую сессию).

## 6. Git Bash (альтернатива)

Если ставишь [Git for Windows](https://git-scm.com/download/win), получаешь Git Bash — POSIX-совместимую оболочку, где работают Unix-команды (`ls`, `grep`, `python`). Удобно для тех, кто привык к Linux.

## 7. Docker (опционально)

Установи [Docker Desktop](https://www.docker.com/products/docker-desktop/), затем:
```powershell
docker compose up
```
Сайт поднимется на `http://localhost:8129`. См. [docker-compose.yml](../../docker-compose.yml).
