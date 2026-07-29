# 🧪 Домашняя лаборатория — как собрать

Своя лаборатория — место, где ты законно ломаешь и защищаешь. Собирается один раз, служит весь курс. Этот гайд — от «ничего нет» до полноценного стенда с атакой, защитой и Active Directory.

> ⚠️ **Золотое правило:** лаборатория **изолирована** от домашней сети и интернета (кроме контролируемого доступа). Атакуешь только внутри неё.

---

## 🖥️ Требования к железу

| Уровень | ОЗУ | Диск | Что потянешь |
|---|---|---|---|
| Минимум | 8 ГБ | 60 ГБ | Kali + 1 цель по очереди |
| Комфорт | 16 ГБ | 150 ГБ | Kali + 2–3 цели + blue-team стек |
| Идеал | 32 ГБ | 250+ ГБ SSD | Полный AD-домен + защита одновременно |

Слабый ПК? → используй **GitHub Codespaces** (60 ч/мес), **облачный VPS** (Oracle Free Tier / DigitalOcean кредит из [student-pack.md](student-pack.md)), или разноси нагрузку по времени.

---

## 🧰 Что установить (база)

### Гипервизор (выбери один)
- **[VirtualBox](https://www.virtualbox.org/)** — бесплатный, для старта идеален. Рекомендую.
- **[VMware Workstation Player](https://www.vmware.com/products/workstation-player.html)** — бесплатен для личного использования, стабильнее под нагрузкой.

### Настройка сети (критично!)
В VirtualBox создай сеть **Host-Only** или **Internal Network**:
- `Файл → Инструменты → Менеджер сетей` → создай Host-Only сеть.
- Все учебные ВМ подключай к ней. Так они видят друг друга, но изолированы.
- Атакующей Kali можно дать 2 адаптера: Host-Only (лаба) + NAT (интернет для обновлений). Цели — **только** Host-Only.

### Снапшоты (обязательно!)
Перед каждой атакой делай **снапшот** ВМ. Сломал — откатился за секунды. Это твоя страховка.

---

## ⚔️ Атакующая машина

**[Kali Linux](https://www.kali.org/get-kali/#kali-virtual-machines)** — скачай готовый образ для VirtualBox/VMware.
- Обнови: `sudo apt update && sudo apt upgrade`
- Всё уже внутри: Nmap, Wireshark, Burp, Metasploit, hashcat, Impacket и т.д.

Альтернатива: **[Parrot Security OS](https://www.parrotsec.org/)** — аналог Kali.

---

## 🎯 Машины-цели (жертвы)

| Цель | Для чего | Месяц | Ссылка |
|---|---|---|---|
| **Metasploitable 2** | Дырявый Linux, первые взломы | 2 | [SourceForge](https://sourceforge.net/projects/metasploitable/) |
| **DVWA** | Веб-уязвимости (SQLi, XSS) | 3 | [github](https://github.com/digininja/DVWA) |
| **OWASP Juice Shop** | Современное уязвимое веб-приложение | 3 | [github](https://github.com/juice-shop/juice-shop) |
| **VulnHub машины** | Полный цикл до root | 2–4 | [vulnhub.com](https://www.vulnhub.com/) |
| **Windows 10/11 Eval** | Windows privesc, цель AD | 2,4 | [Microsoft Eval Center](https://www.microsoft.com/en-us/evalcenter/) |

---

## 🐳 Docker-лаборатория (быстро и легко)

Многие цели поднимаются одной командой — не нужны тяжёлые ВМ:

```bash
# DVWA
docker run --rm -it -p 80:80 vulnerables/web-dvwa

# OWASP Juice Shop
docker run --rm -p 3000:3000 bkimminich/juice-shop
```

С месяца 7 Docker становится и целью изучения (container escape), и инструментом. Установи [Docker Desktop](https://www.docker.com/products/docker-desktop/) / Docker Engine.

---

## 🏰 Active Directory лаборатория (месяц 4)

Мини-домен для отработки атак на AD:
- **1× Windows Server** (Eval) — контроллер домена (DC), поднимаешь роль AD DS.
- **1–2× Windows 10** (Eval) — клиенты в домене.
- Атакуешь с Kali: BloodHound, Kerberoasting, боковое перемещение.

Готовый автоматический вариант (не собирать вручную):
- **[GOAD (Game of Active Directory)](https://github.com/Orange-Cyberdefense/GOAD)** — разворачивает уязвимый AD-домен скриптом.
- **[DetectionLab](https://github.com/clong/DetectionLab)** — AD + blue-team стек сразу.

---

## 🛡️ Blue-team стек (месяцы 5, 8)

Чтобы видеть атаки со стороны защиты:
- **[Sysmon](https://learn.microsoft.com/sysinternals/downloads/sysmon)** + конфиг [SwiftOnSecurity](https://github.com/SwiftOnSecurity/sysmon-config) — телеметрия Windows.
- **[Wazuh](https://wazuh.com/)** — бесплатный EDR/SIEM (сервер + агенты).
- **[Elastic Stack](https://www.elastic.co/security)** — логи и дашборды.
- **[Velociraptor](https://docs.velociraptor.app/)** — форензика и hunting.

Готовые стенды: **[DetectionLab](https://github.com/clong/DetectionLab)**, **[SIEM From Scratch](https://www.youtube.com/results?search_query=wazuh+home+lab)**.

Схема purple-team практики (месяц 5, день 145):
```
[Kali] ──атака──► [Windows цель + Sysmon] ──логи──► [Wazuh/Elastic] ──► ты видишь атаку с двух сторон
```

---

## 🏗️ Рекомендованная сборка по этапам

1. **Месяц 1–2:** VirtualBox + Kali + Metasploitable 2 + Host-Only сеть. Этого достаточно для старта.
2. **Месяц 3:** + DVWA/Juice Shop (лучше через Docker) + Burp.
3. **Месяц 4:** + Windows цели + AD (GOAD или вручную).
4. **Месяц 5:** + Wazuh/Sysmon (blue-team).
5. **Месяц 7:** + Docker/Kubernetes (minikube/kind) + облачные полигоны (flaws.cloud — облако, ВМ не нужны).
6. **Месяц 8:** + DetectionLab / полный детект-стек.

---

## ✅ Чек-лист безопасности лаборатории

- [ ] Учебные цели **только** в Host-Only/Internal сети
- [ ] Цели **не** имеют выхода в интернет
- [ ] Перед атакой сделан снапшот
- [ ] Уязвимые ВМ не запущены, когда не нужны
- [ ] Никогда не атакуешь то, что вне лаборатории
- [ ] Malware-образцы (месяц 5) — только в изолированной ВМ без сети
