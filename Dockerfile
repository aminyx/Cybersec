# Dev-окружение проекта: генераторы + локальный сервер сайта.
# Не для продакшена (сайт хостится статикой на GitHub Pages) — только для разработки.
FROM python:3.12-slim

WORKDIR /app

# Зависимости инструментов (генераторы курса — на stdlib; это для сертификата,
# валидации YAML и линтеров при локальной проверке).
COPY requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt

# Код монтируется томом в docker-compose, поэтому сюда ничего не копируем.
EXPOSE 8129

# По умолчанию: пересобрать данные и статистику, затем поднять сайт.
CMD ["sh", "-c", "python site/build-data.py && python scripts/build_stats.py && python -m http.server 8129 --directory site --bind 0.0.0.0"]
