# 🚀 Cyber Security Advanced — сатҳи дуюм

Барнома **баъд аз** 270 рӯзи асосӣ. Дар ин ҷо ту аз «junior-и қобили киро» ба мутахассисе ки шикор мекунанд рушд мекунӣ. Ин **харитаи роҳи мавзӯъҳо** аст, на рӯз ба рӯз (нақшаи муфассалро вақте расидӣ менависем — мавзӯъҳо барои пешакӣ банақшагирӣ хеле амиқанд).

**Пешшарт:** Фазаҳои 1 ва 2 гузашта, кор ё портфолиои қавӣ ҳаст, бо англисӣ роҳат ҳастӣ.

**Формат:** ~6–9 моҳ, ҳар модул = ғаввосии амиқ + лабҳои душвор + research-и худӣ.

---

## Модули 1 — Red Team Operations
На «осебпазирӣ ёфтан», балки рақиби воқеиро пурра тақлид кардан.
- Банақшагирии операция, OPSEC, cyber kill chain дар амалия
- Дастрасии аввалин: фишинг, техникаҳои initial access
- **C2-фреймворкҳо:** [Cobalt Strike](https://www.cobaltstrike.com/) (шарҳ), open-source [Sliver](https://github.com/BishopFox/sliver), [Mythic](https://github.com/its-a-feature/Mythic), [Havoc](https://github.com/HavocFramework/Havoc)
- Кори дастаии red team, ҳамкорӣ бо blue
- Лабҳо: HTB Pro Labs, [Vulnlab](https://www.hackthebox.com/blog/where-to-find-vulnlab-content-on-htb) (аз соли 2025 — дар дохили HTB: Machines ва Mini Pro Labs), сабки CRTO

## Модули 2 — Malware Analysis & Reverse Engineering
- Таҳлили статикӣ ва динамикии зараровар
- Ассемблери x86/x64, [Ghidra](https://ghidra-sre.org/), [IDA Free](https://hex-rays.com/ida-free/), [x64dbg](https://x64dbg.com/)
- Кушодани бастабандӣ (unpacking), деобфускатсия, таҳлили packer-ҳо
- Таҳлили рафтор, C2-коммуникатсияҳо
- Таълим: [Practical Malware Analysis (китоб)](https://nostarch.com/malware), [OpenSecurityTraining2](https://ost2.fyi/), [crackmes.one](https://crackmes.one/)

## Модули 3 — Active Directory Advanced
- Ҳамлаҳои амиқи Kerberos: delegation (unconstrained/constrained/RBCD), Golden/Silver/Diamond tickets
- ADCS (сертификатҳо) — ҳамлаҳои ESC1–ESC14
- Trust attacks, компрометатсияи forest
- Гузаштан аз ҳифзҳо, detection evasion дар AD
- Лабҳо: [GOAD](https://github.com/Orange-Cyberdefense/GOAD), занҷирҳои AD-и HTB, сабки CRTP/CRTE

## Модули 4 — Evasion & Anti-Detection
- Гузаштан аз AV/EDR: обфускатсия, рамзгузории payload, in-memory
- AMSI bypass, ETW patching, unhooking
- Таҳияи payload-ҳо ва loader-ҳои худ
- Фаҳмиши он ки EDR чӣ тавр детект мекунад (пайванд бо моҳи 8)
- **Танҳо барои red team / research-и қонунӣ.**

## Модули 5 — Threat Hunting & DFIR Advanced
- Форензикаи пешрафта: memory (Volatility deep), disk, timeline analysis
- Enterprise-hunting дар миқёс ([Velociraptor](https://docs.velociraptor.app/), телеметрияи EDR)
- Вокуниш ба сенарияҳои воқеии APT
- Reverse-инжиниринги зараровар барои IR
- Threat intelligence, атрибутсия

## Модули 6 — Exploit Development
- Bug hunting дар бинарҳо, fuzzing ([AFL++](https://github.com/AFLplusplus/AFLplusplus))
- Stack/heap overflow, ROP, гузаштан аз ҳифзҳо (ASLR/DEP/stack canary)
- Эксплуатацияи Windows ва Linux
- Kernel exploitation (асосҳо)
- Таълим: [pwn.college](https://pwn.college/), [ROP Emporium](https://ropemporium.com/), [Nightmare](https://guyinatuxedo.github.io/), сабки OSED

## Модули 7 — Самтҳои махсус (аз рӯи интихоб)
Он чи наздиктар аст интихоб кун:
- **Mobile Security:** Android/iOS, [Frida](https://frida.re/), [Objection](https://github.com/sensepost/objection), [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF), root detection, SSL pinning bypass
- **Hardware Hacking:** UART/JTAG, хондани прошивкаҳо, интерфейсҳои аппаратӣ
- **IoT Security:** таҳлили дастгоҳҳо, прошивкаҳо, протоколҳо
- **ICS/SCADA:** системаҳои саноатӣ, Modbus, амнияти АСУ ТП (инфрасохтори критикӣ)
- **Firmware Analysis:** [binwalk](https://github.com/ReFirmLabs/binwalk), истихроҷ ва таҳлили прошивкаҳо

## Модули 8 — Zero-Day Research
Қулла. Барои ҳама не, вале агар майл дошта бошӣ:
- Ҷустуҷӯи осебпазириҳои номаълум дар нармафзори воқеӣ
- Fuzzing-и пешрафта, code auditing
- Раскрытии масъулиятнок (responsible disclosure), CVE
- Bug bounty дар сатҳи баланд
- Нашри research

---

## 🎓 Сертификатҳои пешрафта (ориентир)

| Самт | Сертификат |
|---|---|
| Pentest | OSCP → OSEP |
| Red Team | CRTO, CRTP/CRTE |
| Exploit Dev | OSED, OSEE |
| Web | OSWE, BSCP |
| Malware/RE | GREM |
| DFIR | GCFA, GCFE |
| Cloud | AWS Security Specialty, CKS |

---

## 🧭 Чӣ тавр ба Advanced наздик шудан

1. **Ба ин ҷо нашитоб.** Аввал — кор ва боварӣ ба асос. Advanced бе асос = ноумедӣ.
2. **1–2 модул интихоб кун**, на ҳамаро якбора. Дар ин сатҳ амиқӣ аз фарогирӣ муҳимтар аст.
3. **Research кун ва нашр кун** — дар ин сатҳ саҳмро ба ҷамоат қадр мекунанд (CVE, мақолаҳо, асбобҳо, докладҳо).
4. **Қатъиян қонунӣ.** Бисёр мавзӯъҳо (evasion, exploit dev, C2) дудама ҳастанд. Танҳо лабҳои қонунӣ, системаҳои худ, engagement-ҳои авторизатсияшуда ва research бо раскрытии масъулиятнок.

Вақте ба ин марҳила расидӣ — баргард, ва модули интихобшударо аз рӯи ҳафтаҳо муфассал менависем, ба монанди курси асосӣ.
