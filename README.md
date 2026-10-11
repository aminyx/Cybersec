# 🛡️ Cybersecurity Course — с нуля до Junior 2026–2027

![version](https://img.shields.io/badge/версия-1.0.0-34D399)
![edition](https://img.shields.io/badge/редакция-2026-67E8F9)
![days](https://img.shields.io/badge/дней-270-success)
![languages](https://img.shields.io/badge/языки-RU%20%2F%20TJ-blue)
![license](https://img.shields.io/badge/лицензия-GPL--3.0-yellow)

Полный курс кибербезопасности на **двух языках**. 270 дней, фундамент + современный стек (Cloud, DevSecOps, AI Security, MCP), 6 экзаменов, 10 проектов, портфолио, бейджи и сертификат.

Курс бесплатный. Все платформы официальные. Практика — только на легальных полигонах.

🌐 **Сайт курса:** https://aminyx.github.io/Cybersec/ (включается в Settings → Pages → Source: GitHub Actions)

📊 Актуальная статистика — [STATS.md](STATS.md) · 📘 Полное описание — [docs/PROJECT.md](docs/PROJECT.md) · 🏗️ Архитектура — [ARCHITECTURE.md](ARCHITECTURE.md)

---

## 🌐 Выбери язык / Забонро интихоб кун

| Язык | Папка | Старт |
|---|---|---|
| 🇷🇺 **Русский** (полностью готов) | [`ru/`](ru/README.md) | [Открыть курс →](ru/README.md) |
| 🇹🇯 **Тоҷикӣ** (полностью готов) | [`tg/`](tg/README.md) | [Курсро кушо →](tg/README.md) |

Для кого: 🇹🇯 Таджикистан · 🇷🇺 Россия · 🇺🇿 Узбекистан · 🇰🇬 Кыргызстан · 🇰🇿 Казахстан — русскоязычные и таджикоязычные студенты.

---

## 🗺️ Карта курса (Roadmap)

```
        ФАЗА 1 — ФУНДАМЕНТ (дни 1–180)
        ─────────────────────────────
   Linux ─► Networking ─► Web ─► Pentest ─► Blue Team ─► Career
    🏅         🏅         🏅       🏅          🏅          🏅

        ФАЗА 2 — СОВРЕМЕННЫЙ СТЕК (дни 181–270)
        ──────────────────────────────────────
   Cloud ─► Docker ─► Kubernetes ─► DevSecOps ─► Detection ─► AI Security ─► MCP
    🏅        🏅          🏅            🏅            🏅            🏅          🏅

                        ▼
              🎓 CYBER SECURITY JUNIOR
           270 дней · 6 экзаменов · 10 проектов
```

Подробная карта с бейджами → [ru/roadmap.md](ru/roadmap.md)

---

## 📦 Что внутри (каждая языковая папка)

**Фундамент (Фаза 1):** Месяцы 1–6 — сети, Linux, веб, пентест, Active Directory, blue team, карьера.
**Современный стек (Фаза 2):** Месяцы 7–9 — Cloud/K8s, DevSecOps/Detection/EDR, AI/LLM Security + MCP.

**Дополнительно:**
- 🎒 [student-pack.md](ru/student-pack.md) — бесплатные сервисы для студентов (GitHub, JetBrains, Azure, Copilot)
- 🧪 [home-lab.md](ru/home-lab.md) — как собрать домашнюю лабораторию
- ❓ [faq.md](ru/faq.md) — частые вопросы («ничего не понимаю», «плохой английский» и т.д.)
- ✅ [checklists.md](ru/checklists.md) — чек-листы навыков после каждого месяца
- 🏅 [roadmap.md](ru/roadmap.md) — карта + бейджи
- 🎓 [certificate.md](ru/certificate.md) — сертификат по окончании (+ генератор PDF)
- 💼 [after-course.md](ru/after-course.md) — профессии, зарплаты, что дальше
- 🚀 [advanced-course.md](ru/advanced-course.md) — второй уровень (Red Team, Malware, RE, C2...)
- 📚 [resources.md](ru/resources.md) · 📖 [glossary.md](ru/glossary.md) · 📓 [study-guide.md](ru/study-guide.md) · 📊 [progress.md](ru/progress.md) · 📝 [exams.md](ru/exams.md) · 🛠️ [projects.md](ru/projects.md)

---

## 🚀 Как начать

1. Выбери язык выше.
2. Прочитай `study-guide.md` (как учиться и не бросить) и `faq.md`.
3. Оформи `student-pack.md` (бесплатные инструменты).
4. Собери лабораторию по `home-lab.md`.
5. Открой Месяц 1, День 1 — и вперёд.
6. Каждый день отмечай прогресс в `progress.md`.
7. Застрял — спроси в [Discussions → Q&A](https://github.com/aminyx/Cybersec/discussions/categories/q-a).

---

## 🧰 Платформа курса

Курс — это не только тексты. Вокруг него собрана инфраструктура:

| Раздел | Что это |
|---|---|
| 🌐 [site/](site/README.md) | **Сайт курса**: карта, карточки месяцев, все 270 дней, поиск, трекинг прогресса, достижения. Двуязычный. `python -m http.server --directory site` |
| 🎬 [videos/](videos/README.md) | **Видео уроков**, встроенные в сайт (плеер на странице дня) |
| ❓ [checks/](checks/README.md) | **Проверка знаний**: 270 тестов, день не закрыть без сдачи |
| 🚩 [challenges/](challenges/README.md) | **Еженедельные CTF** с автопроверкой флага (офлайн, без сервера). `python challenges/check.py` |
| 📄 [templates/](templates/README.md) | Шаблоны: pentest-отчёт, incident report, write-up, CVE, Sigma-правило, README проекта |
| 🎯 [ru/interview-questions.md](ru/interview-questions.md) | Банк вопросов для собеседований с ответами (по трекам) |
| ⚙️ [.github/workflows/](.github/workflows/project-check.yml) | Авто-проверка портфолио-проектов (README, лицензия, линтеры, поиск секретов) |
| 💬 [docs/community-setup.md](docs/community-setup.md) | Готовая структура сообщества (Telegram/Discord): каналы, правила, тексты |
| 🏢 [docs/github-org.md](docs/github-org.md) | Настройка GitHub-организации и репозиториев |
| 🎥 [docs/video-scripts.md](docs/video-scripts.md) | Сценарии вступительных видео к месяцам (+готовый для Месяца 1) |
| 🤝 [CONTRIBUTING.md](CONTRIBUTING.md) | Партнёрская программа: перевод, лаборатории, видео, поддержка |

---

## 📂 Структура репозитория

```
cybersecurity-course/
├── README.md              ← ты здесь (выбор языка)
├── ru/                    ← 🇷🇺 русская версия (полная, +interview-questions.md)
├── tg/                    ← 🇹🇯 таджикская версия (полная, 100%)
├── site/                  ← 🌐 сайт курса (index.html, app.js, build-data.py)
├── checks/                ← ❓ 270 проверочных тестов + CLI
├── videos/                ← 🎬 реестр встроенных видео
├── challenges/            ← 🚩 CTF-челленджи + автопроверка
├── templates/             ← 📄 шаблоны документов
├── docs/                  ← 📚 PROJECT, сообщество, орг, видео, FAQ преподавателей
├── scripts/               ← 🔧 генератор статистики
├── .github/workflows/     ← ⚙️ CI для проектов
├── assets/                ← 🎓 генератор PDF-сертификата
└── governance             ← LICENSE, CHANGELOG, SECURITY, CODE_OF_CONDUCT, …
```

---

## 📚 Документация и участие

| Документ | О чём |
|---|---|
| [docs/PROJECT.md](docs/PROJECT.md) | Полное описание проекта (21 раздел) |
| [ARCHITECTURE.md](ARCHITECTURE.md) · [docs/adr/](docs/adr/README.md) | Архитектура, диаграммы и решения (ADR) |
| [ROADMAP.md](ROADMAP.md) | Куда движется проект (v1.1, v1.2, v2.0, Mobile, LMS, AI Tutor) |
| [STATS.md](STATS.md) | Автостатистика курса |
| [CHANGELOG.md](CHANGELOG.md) · [VERSIONING.md](VERSIONING.md) | Изменения и схема версий |
| [CONTRIBUTING.md](CONTRIBUTING.md) · [TRANSLATION_GUIDE.md](TRANSLATION_GUIDE.md) | Как участвовать и переводить |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) · [SECURITY.md](SECURITY.md) | Правила сообщества и безопасность |
| [MAINTAINERS.md](MAINTAINERS.md) · [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md) | Ответственные и релизы |
| [docs/wiki/](docs/wiki/Home.md) | Wiki: setup, troubleshooting, contribute |
| [docs/teachers-faq.md](docs/teachers-faq.md) | FAQ для преподавателей |

**Разработка:** `docker compose up` поднимает сайт локально · `python scripts/check_repo.py` валидирует репозиторий · CI ([ci.yml](.github/workflows/ci.yml)) проверяет каждый PR. Подробности — [docs/wiki/](docs/wiki/Home.md).

---

## ⚖️ Легальность

Практика — **только** на своих машинах, своём VPS и обучающих платформах. Атака чужих систем без письменного разрешения — уголовное преступление (УК РТ ст. 298–304 / УК РФ ст. 272–274). Bug bounty — строго в рамках scope.

**Лицензия:** [GPL-3.0](LICENSE) — используй, изменяй и распространяй свободно; производные работы тоже должны оставаться открытыми под GPL-3.0. Учись сам и учи других. 🤝
