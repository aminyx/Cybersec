# Troubleshooting

Типовые проблемы и решения.

## Сайт

**Сайт открылся без стилей / пустой.**
Ты открыл `index.html` через `file://`. Браузер блокирует `data.js`. Запусти сервер:
```bash
python -m http.server 8129 --directory site
```
и открой `http://localhost:8129`.

**На сайте старое содержание после правки Markdown.**
Пересобери данные: `python site/build-data.py`, обнови страницу (Ctrl+F5).

**`data.js не загружен` на странице.**
Файл `site/data.js` отсутствует или пуст. Сгенерируй: `python site/build-data.py`.

**Прогресс пропал.**
Он в `localStorage` браузера. Мог сброситься при очистке данных сайта, в режиме инкогнито или при смене домена/порта.

## Python-скрипты

**`UnicodeEncodeError: 'charmap' codec can't encode…` на Windows.**
Консоль Windows (cp1251) не печатает кириллицу. Все наши скрипты форсируют UTF-8, но если пишешь свой — добавь в начало:
```python
import sys
sys.stdout.reconfigure(encoding="utf-8")
```

**`ModuleNotFoundError: No module named 'fpdf'`.**
Нужен только для сертификата: `pip install fpdf2`.

**`build-data.py` отработал, но месяцев/дней 0.**
Скорее всего сломан формат заголовков (`### День N —`) или маркеров дня. Проверь: `python scripts/check_repo.py`.

## CTF

**`check.py` пишет «Неверно», хотя решение верное.**
Проверь формат флага целиком: `CSC{...}`, без лишних пробелов/кавычек. Регистр важен.

**Хочу сбросить решённые задания.**
Удали файл `challenges/.solved`.

## CI (GitHub Actions)

**CI падает на «data.js устарел».**
Ты изменил курс, но не пересобрал данные. Запусти `python site/build-data.py`, закоммить `site/data.js`.

**CI падает на «STATS.md устарел».**
`python scripts/build_stats.py`, закоммить `STATS.md`.

**CI падает на битой ссылке.**
Запусти локально `python scripts/check_repo.py` — он покажет файл и ссылку.

## Docker

**`docker compose up` не поднимает сайт.**
Проверь, что порт 8129 свободен. Логи: `docker compose logs site`. Пересборка образа: `docker compose build --no-cache`.

---

Не помогло? Заведи Issue с меткой `question` и приложи: ОС, версию Python, полный текст ошибки.
