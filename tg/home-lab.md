# 🧪 Лабораторияи хонагӣ — чӣ тавр сохтан

Лабораторияи худат — ҷоест, ки ту қонунӣ мешиканӣ ва ҳифз мекунӣ. Як бор сохта мешавад, тамоми курс хидмат мекунад. Ин дастур — аз «ҳеҷ чиз нест» то стенди пурраи ҳамла, ҳифз ва Active Directory.

> ⚠️ **Қоидаи тиллоӣ:** лаборатория аз шабакаи хонагӣ ва интернет **ҷудо** аст (ба ҷуз дастрасии назоратшаванда). Танҳо дар дохили он ҳамла мекунӣ.

---

## 🖥️ Талабот ба сахтафзор

| Сатҳ | RAM | Диск | Чӣ метавонӣ |
|---|---|---|---|
| Ҳадди ақал | 8 ГБ | 60 ГБ | Kali + 1 ҳадаф навбат ба навбат |
| Роҳат | 16 ГБ | 150 ГБ | Kali + 2–3 ҳадаф + blue-team стек |
| Идеал | 32 ГБ | 250+ ГБ SSD | Домени пурраи AD + ҳифз ҳамзамон |

ПК-и суст? → **GitHub Codespaces** (60 соат/моҳ), **VPS-и абрӣ** (Oracle Free Tier / кредити DigitalOcean аз [student-pack.md](student-pack.md)), ё бори корро аз рӯи вақт тақсим кун.

---

## 🧰 Чӣ насб кардан (асос)

### Гипервизор (яктаро интихоб кун)
- **[VirtualBox](https://www.virtualbox.org/)** — ройгон, барои оғоз идеалӣ. Тавсия медиҳам.
- **[VMware Workstation Player](https://www.vmware.com/products/workstation-player.html)** — барои истифодаи шахсӣ ройгон, зери бор устувортар.

### Танзими шабака (муҳим!)
Дар VirtualBox шабакаи **Host-Only** ё **Internal Network** соз:
- `Файл → Асбобҳо → Менеҷери шабака` → шабакаи Host-Only соз.
- Ҳамаи ВМ-ҳои таълимиро ба он пайваст кун. Онҳо якдигарро мебинанд, вале ҷудо мемонанд.
- Ба Kali метавонӣ 2 адаптер диҳӣ: Host-Only (лаб) + NAT (интернет барои навкунӣ). Ҳадафҳо — **танҳо** Host-Only.

### Снапшотҳо (ҳатман!)
Пеш аз ҳар ҳамла **снапшот** соз. Шикастӣ — дар сония баргаштӣ. Ин суғуртаи туст.

---

## ⚔️ Мошини ҳамлакунанда

**[Kali Linux](https://www.kali.org/get-kali/#kali-virtual-machines)** — образи тайёрро барои VirtualBox/VMware зеркашӣ кун.
- Нав кун: `sudo apt update && sudo apt upgrade`
- Ҳама дар дохил ҳаст: Nmap, Wireshark, Burp, Metasploit, hashcat, Impacket ва ғ.

Алтернатива: **[Parrot Security OS](https://www.parrotsec.org/)**.

---

## 🎯 Мошинҳои ҳадаф (қурбониҳо)

| Ҳадаф | Барои чӣ | Моҳ | Пайванд |
|---|---|---|---|
| **Metasploitable 2** | Linux-и сӯрохдор, аввалин шикастҳо | 2 | [SourceForge](https://sourceforge.net/projects/metasploitable/) |
| **DVWA** | Осебпазириҳои web (SQLi, XSS) | 3 | [github](https://github.com/digininja/DVWA) |
| **OWASP Juice Shop** | Веб-барномаи осебпазири муосир | 3 | [github](https://github.com/juice-shop/juice-shop) |
| **VulnHub мошинҳо** | Давраи пурра то root | 2–4 | [vulnhub.com](https://www.vulnhub.com/) |
| **Windows 10/11 Eval** | Windows privesc, ҳадафи AD | 2,4 | [Microsoft Eval Center](https://www.microsoft.com/en-us/evalcenter/) |

---

## 🐳 Лабораторияи Docker (зуд ва осон)

Бисёр ҳадафҳо бо як фармон боло мешаванд — ВМ-ҳои вазнин лозим нест:

```bash
# DVWA
docker run --rm -it -p 80:80 vulnerables/web-dvwa

# OWASP Juice Shop
docker run --rm -p 3000:3000 bkimminich/juice-shop
```

Аз моҳи 7 Docker ҳам объекти омӯзиш (container escape) мешавад, ҳам асбоб. [Docker Desktop](https://www.docker.com/products/docker-desktop/) насб кун.

---

## 🏰 Лабораторияи Active Directory (моҳи 4)

Домени хурд барои машқи ҳамла ба AD:
- **1× Windows Server** (Eval) — контроллери домен (DC), нақши AD DS-ро боло мекунӣ.
- **1–2× Windows 10** (Eval) — муштариён дар домен.
- Аз Kali ҳамла: BloodHound, Kerberoasting, ҳаракати паҳлӯӣ.

Варианти тайёри худкор (дастӣ насозӣ):
- **[GOAD (Game of Active Directory)](https://github.com/Orange-Cyberdefense/GOAD)** — домени осебпазири AD-ро бо скрипт месозад.
- **[DetectionLab](https://github.com/clong/DetectionLab)** — AD + blue-team стек якбора.

---

## 🛡️ Blue-team стек (моҳҳои 5, 8)

Барои дидани ҳамлаҳо аз ҷониби ҳифз:
- **[Sysmon](https://learn.microsoft.com/sysinternals/downloads/sysmon)** + конфиги [SwiftOnSecurity](https://github.com/SwiftOnSecurity/sysmon-config) — телеметрияи Windows.
- **[Wazuh](https://wazuh.com/)** — EDR/SIEM-и ройгон (сервер + агентҳо).
- **[Elastic Stack](https://www.elastic.co/security)** — логҳо ва дашбордҳо.
- **[Velociraptor](https://docs.velociraptor.app/)** — форензика ва hunting.

Нақшаи амалияи purple-team (моҳи 5, рӯзи 145):
```
[Kali] ──ҳамла──► [Windows ҳадаф + Sysmon] ──логҳо──► [Wazuh/Elastic] ──► ҳамларо аз ду ҷониб мебинӣ
```

---

## 🏗️ Сохти тавсияшаванда аз рӯи марҳилаҳо

1. **Моҳи 1–2:** VirtualBox + Kali + Metasploitable 2 + шабакаи Host-Only. Барои оғоз кофист.
2. **Моҳи 3:** + DVWA/Juice Shop (беҳтараш тавассути Docker) + Burp.
3. **Моҳи 4:** + Windows ҳадафҳо + AD (GOAD ё дастӣ).
4. **Моҳи 5:** + Wazuh/Sysmon (blue-team).
5. **Моҳи 7:** + Docker/Kubernetes (minikube/kind) + майдончаҳои абрӣ (flaws.cloud — абр, ВМ лозим нест).
6. **Моҳи 8:** + DetectionLab / стеки пурраи детект.

---

## ✅ Чек-листи амнияти лаборатория

- [ ] Ҳадафҳои таълимӣ **танҳо** дар шабакаи Host-Only/Internal
- [ ] Ҳадафҳо ба интернет баромад **надоранд**
- [ ] Пеш аз ҳамла снапшот сохта шуд
- [ ] ВМ-ҳои осебпазир вақте лозим нест, кор намекунанд
- [ ] Ҳеҷ гоҳ ба он чи берун аз лаборатория аст ҳамла намекунӣ
- [ ] Намунаҳои malware (моҳи 5) — танҳо дар ВМ-и ҷудошуда бе шабака
