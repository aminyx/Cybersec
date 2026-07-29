# How to Contribute

Краткая версия. Полные правила — в [CONTRIBUTING.md](../../CONTRIBUTING.md).

## В двух словах

1. Форкни репозиторий.
2. Создай ветку: `git checkout -b fix/short-description`.
3. Внеси изменения.
4. **Если правил учебные файлы** — пересобери артефакты:
   ```bash
   python site/build-data.py
   python scripts/build_stats.py
   ```
5. Проверь локально:
   ```bash
   python scripts/check_repo.py
   ```
6. Открой Pull Request с понятным описанием.

CI ([ci.yml](../../.github/workflows/ci.yml)) автоматически проверит структуру, ссылки и актуальность `data.js`/`STATS.md`.

## Что можно улучшать

- Переводы на новые языки → [TRANSLATION_GUIDE.md](../../TRANSLATION_GUIDE.md)
- Новые CTF-задания → [challenges/README.md](../../challenges/README.md)
- Учебные лаборатории, docker-стенды
- Исправление ссылок, опечаток, обновление версий инструментов
- Методические материалы для преподавателей

## Правила стиля

- Сохраняй формат дня: 📺 теория → 💻 практика → ✍️ задание → 🎯 проверь себя.
- Тон — на «ты», дружелюбно и честно.
- Только бесплатные и легальные ресурсы.
- Соблюдай [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md).

## Признание

Все контрибьюторы попадают в список участников; авторы крупных разделов — в [MAINTAINERS.md](../../MAINTAINERS.md).
