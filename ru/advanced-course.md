# 🚀 Cyber Security Advanced — второй уровень

Программа **после** основных 270 дней. Здесь ты из «нанимаемого джуна» растёшь в специалиста, которого хантят. Это **дорожная карта тем**, а не день-за-днём (детальный план распишем, когда дойдёшь — темы слишком глубокие, чтобы планировать заранее).

**Предпосылка:** пройдены Фаза 1 и Фаза 2, есть работа или крепкое портфолио, комфортно с английским.

**Формат:** ~6–9 месяцев, каждый модуль = глубокое погружение + сложные лабы + свой research.

---

## Модуль 1 — Red Team Operations
Не «найти уязвимость», а сымитировать реального противника целиком.
- Планирование операции, OPSEC, cyber kill chain на практике
- Начальный доступ: фишинг, initial access техники
- **C2-фреймворки:** [Cobalt Strike](https://www.cobaltstrike.com/) (обзор), open-source [Sliver](https://github.com/BishopFox/sliver), [Mythic](https://github.com/its-a-feature/Mythic), [Havoc](https://github.com/HavocFramework/Havoc)
- Командная работа red team, взаимодействие с blue
- Лабы: HTB Pro Labs, [Vulnlab](https://www.hackthebox.com/blog/where-to-find-vulnlab-content-on-htb) (с 2025 года — внутри HTB: Machines и Mini Pro Labs), CRTO-стиль

## Модуль 2 — Malware Analysis & Reverse Engineering
- Статический и динамический анализ вредоносов
- Ассемблер x86/x64, [Ghidra](https://ghidra-sre.org/), [IDA Free](https://hex-rays.com/ida-free/), [x64dbg](https://x64dbg.com/)
- Распаковка, деобфускация, анализ упаковщиков
- Анализ поведения, C2-коммуникаций
- Обучение: [Practical Malware Analysis (книга)](https://nostarch.com/malware), [OpenSecurityTraining2](https://ost2.fyi/), [crackmes.one](https://crackmes.one/)

## Модуль 3 — Active Directory Advanced
- Глубокие Kerberos-атаки: delegation (unconstrained/constrained/RBCD), Golden/Silver/Diamond tickets
- ADCS (сертификаты) — атаки ESC1–ESC14
- Trust attacks, forest компрометация
- Обход защит, detection evasion в AD
- Лабы: [GOAD](https://github.com/Orange-Cyberdefense/GOAD), HTB AD-цепочки, CRTP/CRTE-стиль

## Модуль 4 — Evasion & Anti-Detection
- Обход AV/EDR: обфускация, шифрование payload, in-memory
- AMSI bypass, ETW patching, unhooking
- Разработка своих payload'ов и loader'ов
- Понимание, как EDR детектит (связка с месяцем 8)
- **Только для легальных red team / research.**

## Модуль 5 — Threat Hunting & DFIR Advanced
- Продвинутая форензика: memory (Volatility deep), disk, timeline analysis
- Enterprise-hunting на масштабе ([Velociraptor](https://docs.velociraptor.app/), EDR-телеметрия)
- Реагирование на реальные APT-сценарии
- Reverse-инжиниринг вредоносов для IR
- Threat intelligence, атрибуция

## Модуль 6 — Exploit Development
- Bug hunting в бинарях, fuzzing ([AFL++](https://github.com/AFLplusplus/AFLplusplus))
- Stack/heap overflow, ROP, обход защит (ASLR/DEP/stack canary)
- Windows и Linux эксплуатация
- Kernel exploitation (основы)
- Обучение: [pwn.college](https://pwn.college/), [ROP Emporium](https://ropemporium.com/), [Nightmare](https://guyinatuxedo.github.io/), OSED-стиль

## Модуль 7 — Специализированные направления (по выбору)
Выбери, что ближе:
- **Mobile Security:** Android/iOS, [Frida](https://frida.re/), [Objection](https://github.com/sensepost/objection), [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF), root detection, SSL pinning bypass
- **Hardware Hacking:** UART/JTAG, чтение прошивок, аппаратные интерфейсы
- **IoT Security:** анализ устройств, прошивки, протоколы
- **ICS/SCADA:** промышленные системы, Modbus, безопасность АСУ ТП (критичная инфраструктура)
- **Firmware Analysis:** [binwalk](https://github.com/ReFirmLabs/binwalk), извлечение и анализ прошивок

## Модуль 8 — Zero-Day Research
Вершина. Не для всех, но если тянет:
- Поиск неизвестных уязвимостей в реальном ПО
- Продвинутый fuzzing, code auditing
- Ответственное раскрытие (responsible disclosure), CVE
- Bug bounty на высоком уровне
- Публикация research

---

## 🎓 Продвинутые сертификаты (ориентир)

| Направление | Сертификат |
|---|---|
| Pentest | OSCP → OSEP |
| Red Team | CRTO, CRTP/CRTE |
| Exploit Dev | OSED, OSEE |
| Web | OSWE, BSCP |
| Malware/RE | GREM |
| DFIR | GCFA, GCFE |
| Cloud | AWS Security Specialty, CKS |

---

## 🧭 Как подойти к Advanced

1. **Не спеши сюда.** Сначала — работа и уверенность в фундаменте. Advanced без базы = разочарование.
2. **Выбери 1–2 модуля**, а не всё сразу. Глубина важнее охвата на этом уровне.
3. **Делай research и публикуй** — на этом уровне ценят вклад в сообщество (CVE, статьи, инструменты, доклады).
4. **Строго легально.** Многие темы (evasion, exploit dev, C2) — обоюдоострые. Только легальные лабы, свои системы, авторизованные engagement'ы и research с ответственным раскрытием.

Когда дойдёшь до этого этапа — вернись, и распишем выбранный модуль по неделям детально, как основной курс.
