# Месяц 8 — DevSecOps, Detection Engineering & EDR (Фаза 2)

**Цель месяца:** три очень востребованных направления. **DevSecOps** — безопасность встроена в разработку (идеально ложится на твой Python-бэкграунд). **Detection Engineering** — не просто читать алерты, а *писать* правила обнаружения. **EDR** — инструменты, на которых реально работает современный blue team.

**Предпосылка:** месяцы 1–6 (особенно месяц 5 — blue team) + месяц 7.

**Главные ресурсы месяца:**
- 🔧 [Semgrep](https://semgrep.dev/), [CodeQL](https://codeql.github.com/), [Trivy](https://github.com/aquasecurity/trivy), [gitleaks](https://github.com/gitleaks/gitleaks)
- 🎯 [Sigma](https://github.com/SigmaHQ/sigma), [Sysmon](https://learn.microsoft.com/sysinternals/downloads/sysmon), [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- 🛡️ [Wazuh](https://wazuh.com/), [Velociraptor](https://docs.velociraptor.app/), [Elastic Security](https://www.elastic.co/security)
- 🧪 [DetectionLab](https://github.com/clong/DetectionLab)

---

## Неделя 29 — DevSecOps: безопасность в CI/CD

### День 211 — Что такое DevSecOps
- 📺 **Теория (1,5 ч):** [DevSecOps простыми словами (YouTube)](https://www.youtube.com/results?search_query=devsecops+что+это). Shift-left, безопасность на каждом этапе pipeline. [OWASP DevSecOps Guideline](https://owasp.org/www-project-devsecops-guideline/).
- 💻 **Практика (2 ч):** Разбери типичный CI/CD pipeline. Создай репозиторий с [GitHub Actions](https://docs.github.com/actions).
- ✍️ **Задание:** схема pipeline с точками контроля безопасности.
- 🎯 **Проверь себя:** что значит «shift left» в безопасности?

### День 212 — SAST: статический анализ кода
- 📺 **Теория (1,5 ч):** SAST, [Semgrep](https://semgrep.dev/), [CodeQL](https://codeql.github.com/). Поиск уязвимостей в коде без запуска.
- 💻 **Практика (2,5 ч):** Прогони [Semgrep](https://semgrep.dev/playground/) на намеренно уязвимом коде ([DVWA](https://github.com/digininja/DVWA) исходники или [OWASP Juice Shop](https://github.com/juice-shop/juice-shop)). Разбери находки.
- ✍️ **Задание:** найди SQLi/командную инъекцию в коде через Semgrep.
- 🎯 **Проверь себя:** чем SAST отличается от DAST?

### День 213 — SCA и сканирование зависимостей
- 📺 **Теория (1,5 ч):** [Trivy](https://github.com/aquasecurity/trivy), [Snyk](https://snyk.io/), Dependabot, supply chain атаки.
- 💻 **Практика (2 ч):** Просканируй зависимости проекта на уязвимости. Настрой [Dependency Review](https://docs.github.com/code-security).
- ✍️ **Задание:** найди уязвимую зависимость в проекте, предложи фикс.
- 🎯 **Проверь себя:** что такое supply chain атака (пример: xz, event-stream)?

### День 214 — Secret Scanning
- 📺 **Теория (1,5 ч):** утечки секретов в git-истории, [gitleaks](https://github.com/gitleaks/gitleaks), [TruffleHog](https://github.com/trufflesecurity/trufflehog).
- 💻 **Практика (2 ч):** Прогони gitleaks по репозиторию (даже своему старому!). Разбери, как секрет живёт в истории даже после удаления.
- ✍️ **Задание:** найди «забытый» секрет в git-истории тестового репо.
- 🎯 **Проверь себя:** почему `git rm` не удаляет секрет из истории?

### День 215 — Собираем защищённый pipeline
- 📺 **Теория (1 ч):** интеграция всех сканеров в GitHub Actions, quality gates.
- 💻 **Практика (3 ч):** Настрой pipeline: Semgrep + Trivy + gitleaks запускаются автоматически на каждый push, блокируют мёрж при критичных находках.
- ✍️ **Задание (мини-проект):** репозиторий с безопасным CI/CD pipeline на GitHub.
- 🎯 **Проверь себя:** твой pipeline остановит уязвимый код до продакшена?

### День 216 — SBOM и цепочка поставок
- 📺 **Теория (1,5 ч):** [SBOM](https://www.cisa.gov/sbom), [CycloneDX](https://cyclonedx.org/), подпись артефактов ([Sigstore/cosign](https://www.sigstore.dev/)).
- 💻 **Практика (2 ч):** Сгенерируй SBOM для проекта (Trivy/Syft), разбери состав.
- ✍️ **Задание:** объясни, зачем компании SBOM.
- 🎯 **Проверь себя:** что даёт SBOM при новой CVE вроде Log4Shell?

### День 217 — Повторение недели
- 💻 **Практика (3,5 ч):** Доведи pipeline, добавь недостающие сканеры.
- ✍️ **Задание:** документация pipeline в README.
- 🎯 **Проверь себя:** понимаешь весь путь код → продакшен с контролем на каждом шаге?

---

## Неделя 30 — Detection Engineering

### День 218 — От аналитика к инженеру детекта
- 📺 **Теория (1,5 ч):** [Detection Engineering (YouTube)](https://www.youtube.com/results?search_query=detection+engineering+что+это). Разница: аналитик читает алерты, инженер *создаёт* правила. Detection-as-code.
- 💻 **Практика (2 ч):** Изучи структуру [Sigma-правил](https://github.com/SigmaHQ/sigma) глубоко. Разбери 5 готовых правил.
- ✍️ **Задание:** разбери Sigma-правило по строкам.
- 🎯 **Проверь себя:** почему Sigma — «универсальный» формат детекта?

### День 219 — Sysmon: телеметрия Windows
- 📺 **Теория (1,5 ч):** [Sysmon](https://learn.microsoft.com/sysinternals/downloads/sysmon), конфиг [SwiftOnSecurity](https://github.com/SwiftOnSecurity/sysmon-config). Event ID: 1 (process), 3 (network), 11 (file), 22 (DNS).
- 💻 **Практика (2,5 ч):** Установи Sysmon на Windows-ВМ с хорошим конфигом. Выполни действие → найди его в логах.
- ✍️ **Задание:** сопоставь 6 ключевых Sysmon Event ID с тем, что они ловят.
- 🎯 **Проверь себя:** какой Event ID покажет запуск подозрительного процесса?

### День 220 — Atomic Red Team: симуляция атак
- 📺 **Теория (1 ч):** [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) — тесты, воспроизводящие техники MITRE ATT&CK.
- 💻 **Практика (3 ч):** Запусти atomic-тест (напр. T1059 — выполнение команд) на ВМ, посмотри след в Sysmon/логах.
- ✍️ **Задание:** запусти 3 atomic-теста, зафиксируй телеметрию каждого.
- 🎯 **Проверь себя:** как atomic-тесты помогают проверять детекты?

### День 221 — Пишем свои правила детекта
- 📺 **Теория (1,5 ч):** методология: техника ATT&CK → телеметрия → правило → тест → тюнинг (борьба с false positive).
- 💻 **Практика (2,5 ч):** Напиши Sigma-правило на одну из атак, что делал в месяцах 2–4 (Kerberoasting, reverse shell, privesc). Проверь atomic-тестом.
- ✍️ **Задание:** рабочее Sigma-правило + доказательство срабатывания.
- 🎯 **Проверь себя:** как снизить false positives у своего правила?

### День 222 — ELK / Elastic Security
- 📺 **Теория (1,5 ч):** [Elastic Stack](https://www.elastic.co/security) (Elasticsearch, Logstash, Kibana), детект-правила в Elastic.
- 💻 **Практика (2 ч):** THM комната по Elastic/ELK. Построй дашборд, напиши запрос-детект.
- ✍️ **Задание:** дашборд обнаружения подозрительных входов.
- 🎯 **Проверь себя:** роль каждого компонента ELK?

### День 223 — Threat Hunting
- 📺 **Теория (1,5 ч):** [Threat hunting методология](https://www.youtube.com/results?search_query=threat+hunting+для+начинающих), гипотезы, hunt на основе ATT&CK.
- 💻 **Практика (2,5 ч):** Проведи hunt в учебных данных: выдвинь гипотезу → проверь по логам → найди/опровергни.
- ✍️ **Задание:** отчёт по одному hunt'у.
- 🎯 **Проверь себя:** чем hunting отличается от реагирования на алерт?

### День 224 — Повторение недели
- 💻 **Практика (3,5 ч):** Напиши ещё 2–3 правила детекта на свои атаки, протестируй.
- ✍️ **Задание:** репозиторий `detection-rules` на GitHub с твоими Sigma-правилами.
- 🎯 **Проверь себя:** у тебя есть коллекция собственных детектов?

---

## Неделя 31 — EDR и современный Blue Team

### День 225 — Что такое EDR/XDR
- 📺 **Теория (2 ч):** [EDR простыми словами (YouTube)](https://www.youtube.com/results?search_query=edr+что+это+простыми+словами). CrowdStrike, Microsoft Defender for Endpoint, SentinelOne, Elastic. Как EDR видит поведение, а не только сигнатуры.
- 💻 **Практика (1,5 ч):** Изучи возможности [Microsoft Defender](https://learn.microsoft.com/defender-endpoint/) (доступен на Windows) — телеметрия, детекты.
- ✍️ **Задание:** сравни антивирус vs EDR.
- 🎯 **Проверь себя:** почему EDR ловит то, что антивирус пропускает?

### День 226 — Wazuh: open-source XDR/SIEM
- 📺 **Теория (1,5 ч):** [Wazuh](https://wazuh.com/) — бесплатный EDR+SIEM. Агенты, правила, дашборды.
- 💻 **Практика (2,5 ч):** Разверни Wazuh (сервер + агент на ВМ). Посмотри алерты, интеграцию с MITRE ATT&CK.
- ✍️ **Задание:** настрой Wazuh, вызови и поймай подозрительное действие.
- 🎯 **Проверь себя:** что показывает Wazuh-агент на хосте?

### День 227 — Velociraptor: DFIR и хантинг
- 📺 **Теория (1,5 ч):** [Velociraptor](https://docs.velociraptor.app/) — сбор артефактов и hunting на масштабе.
- 💻 **Практика (2,5 ч):** Установи Velociraptor, собери артефакты с эндпоинта, проведи hunt.
- ✍️ **Задание:** собери артефакты и найди признак «компрометации».
- 🎯 **Проверь себя:** зачем нужен инструмент вроде Velociraptor при инциденте на 1000 машин?

### День 228 — DetectionLab: полигон
- 💻 **Практика (4 ч):** Разверни/используй [DetectionLab](https://github.com/clong/DetectionLab) (или его аналог) — готовая среда с Sysmon, Splunk/ELK, Velociraptor. Атакуй и наблюдай.
- ✍️ **Задание:** проведи атаку и полностью отследи её в стеке защиты.
- 🎯 **Проверь себя:** видишь атаку одновременно с 3 сторон (лог, EDR, SIEM)?

### День 229 — Purple Team автоматизация
- 📺 **Теория (1,5 ч):** [Purple team / adversary emulation](https://www.youtube.com/results?search_query=purple+team+adversary+emulation), [Caldera](https://github.com/mitre/caldera).
- 💻 **Практика (2,5 ч):** Запусти цепочку атак (atomic/Caldera), проверь, какие детекты сработали, а какие — нет. Найди «слепые зоны».
- ✍️ **Задание:** карта покрытия детектами по ATT&CK (что ловится, что нет).
- 🎯 **Проверь себя:** как найти пробел в обнаружении?

### День 230 — Резервный день
- 💻 **Практика (4 ч):** Догоняй EDR/detection хвосты.
- ✍️ **Задание:** порядок в портфолио.
- 🎯 **Проверь себя:** долгов нет?

### День 231 — Экзамен месяца (Blue Team advanced)
- 💻 **Практика (4,5 ч), сам:** см. [exams.md](exams.md) → Экзамен 3 (Blue Team). Дан pcap + evtx + auth.log + syslog. Найди IOC, разложи по MITRE ATT&CK и Kill Chain, напиши Incident Report + предложи детекты.
- ✍️ **Задание:** Incident Report «Итоги месяца 8».
- 🎯 **Проверь себя:** справился — ты уже сильный blue-team кандидат.

---

## Неделя 32 — Закрепление и проекты

### День 232 — Проект: Log Analyzer
- 💻 **Практика (4,5 ч):** [Проект №2 — Log Analyzer](projects.md) на Python: парсит syslog/Windows logs, мапит на MITRE ATT&CK.
- ✍️ **Задание:** рабочий каркас на GitHub.
- 🎯 **Проверь себя:** —

### День 233 — Проект: IOC Scanner
- 💻 **Практика (4,5 ч):** [Проект №6 — IOC Scanner](projects.md) с YARA и Sigma.
- ✍️ **Задание:** каркас на GitHub.
- 🎯 **Проверь себя:** —

### День 234 — Проект: Docker Security Scanner
- 💻 **Практика (4,5 ч):** [Проект №7 — Docker Security Scanner](projects.md) поверх Trivy API.
- ✍️ **Задание:** каркас на GitHub.
- 🎯 **Проверь себя:** —

### День 235 — YARA-правила
- 📺 **Теория (1,5 ч):** [YARA](https://virustotal.github.io/yara/) — правила для поиска malware по паттернам.
- 💻 **Практика (2 ч):** Напиши YARA-правило на учебный образец.
- ✍️ **Задание:** рабочее YARA-правило.
- 🎯 **Проверь себя:** чем YARA (файлы) отличается от Sigma (логи)?

### День 236 — Интеграция навыков
- 💻 **Практика (4 ч):** Свяжи всё: атака (red) → телеметрия (Sysmon/EDR) → детект (Sigma) → расследование (Velociraptor) → отчёт.
- ✍️ **Задание (мини-проект):** статья «Полный цикл детекта атаки X».
- 🎯 **Проверь себя:** держишь всю цепочку в голове?

### День 237 — Резервный день
- 💻 **Практика (4 ч):** Догоняй проекты и хвосты.
- ✍️ **Задание:** порядок в портфолио.
- 🎯 **Проверь себя:** —

### День 238 — Мини-проект: SIEM своими руками (старт)
- 💻 **Практика (4,5 ч):** [Проект №1 — мини-SIEM](projects.md) на Python + SQLite + веб-UI. Флагманский проект для blue-team резюме.
- ✍️ **Задание:** архитектура + каркас на GitHub.
- 🎯 **Проверь себя:** —

### День 239 — Разбор месяца
- 📺 **Разбор (2 ч):** пересмотри детекты и проекты, отточи методику.
- ✍️ **Задание:** методичка detection engineering.
- 🎯 **Проверь себя:** —

### День 240 — Рефлексия месяца
- ✍️ **Задание:** отметь дни в [progress.md](progress.md). Отдохни.
- 🎯 **Проверь себя:** остался месяц 9 — AI Security, самый горячий навык 2026.

---

## Итог месяца 8 — что ты теперь умеешь

- ✅ DevSecOps: SAST (Semgrep/CodeQL), SCA (Trivy/Snyk), secret scanning (gitleaks), защищённый CI/CD, SBOM
- ✅ Detection Engineering: пишешь Sigma/YARA-правила, Sysmon-телеметрия, Atomic Red Team, тюнинг детектов
- ✅ EDR: Wazuh, Velociraptor, Defender, DetectionLab, purple team (Caldera)
- ✅ Threat hunting по гипотезам
- ✅ Несколько Python-проектов для портфолио

**Следующий шаг:** [month-09-ai-security.md](month-09-ai-security.md) — AI/LLM Security и MCP. То, чего нет почти ни у кого.
