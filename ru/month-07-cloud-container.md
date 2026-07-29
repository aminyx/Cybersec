# Месяц 7 — Cloud & Container Security (Фаза 2)

**Цель месяца:** закрыть крупнейший пробел рынка — облако и контейнеры. Почти каждая компания в 2026 живёт в AWS/Azure/GCP и крутит Docker + Kubernetes. Джун, который умеет находить открытый S3, кривой IAM и container escape, стоит заметно дороже.

**Предпосылка:** пройдены месяцы 1–6. Ты уже умеешь атаковать и защищать классику — теперь переносим навык в облако.

**Главные ресурсы месяца:**
- ☁️ [flaws.cloud](http://flaws.cloud/) и [flaws2.cloud](http://flaws2.cloud/) — бесплатные AWS-полигоны
- 🐐 [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat), [AWSGoat](https://github.com/ine-labs/AWSGoat), [Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat)
- 🎓 [Pwned Labs](https://pwnedlabs.io/) — бесплатные облачные лабы
- 🐳 [Docker](https://docs.docker.com/), [Trivy](https://github.com/aquasecurity/trivy), [Docker Bench](https://github.com/docker/docker-bench-security)

> ⚠️ В своём AWS-аккаунте держи биллинг-алерты и Free Tier — облако может списать деньги за забытые ресурсы. Всё гаси после лабы.

---

## Неделя 25 — Docker Security

### День 181 — Основы контейнеров
- 📺 **Теория (1,5 ч):** [Docker с нуля (YouTube, русский)](https://www.youtube.com/results?search_query=docker+для+начинающих+курс). Образ (image), контейнер, слои, реестр, разница VM vs контейнер.
- 💻 **Практика (2 ч):** Установи Docker. `docker run`, `docker ps`, `docker exec -it`, `docker images`. Запусти nginx, зайди внутрь контейнера.
- ✍️ **Задание:** объясни разницу «образ vs контейнер» и «контейнер vs виртуалка».
- 🎯 **Проверь себя:** почему контейнер легче виртуалки?

### День 182 — Dockerfile и как строят образы
- 📺 **Теория (1,5 ч):** Dockerfile, `docker build`, слои, кэш, multi-stage build.
- 💻 **Практика (2 ч):** Собери свой образ с Python-приложением. Разбери, из чего он состоит: `docker history`.
- ✍️ **Задание:** напиши Dockerfile для простого скрипта.
- 🎯 **Проверь себя:** что попадает в образ на каждом слое?

### День 183 — Уязвимости контейнеров
- 📺 **Теория (1,5 ч):** [Docker security (YouTube)](https://www.youtube.com/results?search_query=docker+security+основы). Секреты в образах, привилегированный контейнер, монтирование docker.sock, root внутри контейнера.
- 💻 **Практика (2,5 ч):** [Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat) содержит и Docker-сценарии; или отдельные Docker-escape лабы. Разбери, как `--privileged` = дыра.
- ✍️ **Задание:** объясни, почему нельзя монтировать `/var/run/docker.sock` в контейнер.
- 🎯 **Проверь себя:** что даёт атакующему root внутри привилегированного контейнера?

### День 184 — Сканирование образов: Trivy, Grype
- 📺 **Теория (1 ч):** сканеры уязвимостей образов, SCA (software composition analysis).
- 💻 **Практика (2,5 ч):** Установи [Trivy](https://github.com/aquasecurity/trivy) и [Grype](https://github.com/anchore/grype). Просканируй свой образ и популярный публичный. Разбери отчёт: CVE, severity, fixed version.
- ✍️ **Задание:** найди уязвимости в старом образе (напр. `python:3.6`), составь список критичных.
- 🎯 **Проверь себя:** что такое CVE и как читать отчёт Trivy?

### День 185 — Хардненинг Docker
- 📺 **Теория (1,5 ч):** [Docker Bench](https://github.com/docker/docker-bench-security), CIS Docker Benchmark, non-root user, read-only fs, capabilities drop.
- 💻 **Практика (2 ч):** Прогони Docker Bench на своём хосте. Перепиши Dockerfile безопасно: non-root, минимальный базовый образ (distroless/alpine), без секретов.
- ✍️ **Задание:** «до/после» — небезопасный и безопасный Dockerfile с комментариями.
- 🎯 **Проверь себя:** назови 4 правила безопасного Dockerfile.

### День 186 — Docker Compose и секреты
- 📺 **Теория (1,5 ч):** docker-compose, volumes, networks, управление секретами (не в env!).
- 💻 **Практика (2 ч):** Подними стек из 2–3 сервисов через compose. Разбери, где утекают секреты и как правильно.
- ✍️ **Задание:** найди секрет, «забытый» в переменных окружения контейнера.
- 🎯 **Проверь себя:** почему секреты в `ENV`/`docker inspect` — плохо?

### День 187 — Повторение недели + мини-проект
- 💻 **Практика (3 ч):** Возьми уязвимый образ, найди проблемы (Trivy + ручной осмотр), исправь, пересобери безопасно.
- ✍️ **Задание (мини-проект):** репозиторий «Docker security audit» на GitHub: находки + исправления.
- 🎯 **Проверь себя:** можешь провести аудит образа от и до?

---

## Неделя 26 — Kubernetes Security

### День 188 — Что такое Kubernetes
- 📺 **Теория (2 ч):** [Kubernetes для начинающих (YouTube, русский)](https://www.youtube.com/results?search_query=kubernetes+для+начинающих+курс). Pod, Node, Namespace, Deployment, Service, control plane.
- 💻 **Практика (1,5 ч):** Установи [minikube](https://minikube.sigs.k8s.io/) или [kind](https://kind.sigs.k8s.io/). `kubectl get pods/nodes/ns`, разверни первый pod.
- ✍️ **Задание:** схема кластера K8s: control plane + worker nodes + что где.
- 🎯 **Проверь себя:** что такое Pod и чем он отличается от контейнера?

### День 189 — kubectl и объекты кластера
- 📺 **Теория (1,5 ч):** Deployments, Services, ConfigMaps, Secrets, Ingress.
- 💻 **Практика (2 ч):** Создавай/смотри объекты через `kubectl`. Прочитай Secret: `kubectl get secret -o yaml` — заметь, что это лишь base64, не шифрование!
- ✍️ **Задание:** извлеки и раскодируй Secret из учебного кластера.
- 🎯 **Проверь себя:** почему K8s Secret по умолчанию — это НЕ безопасное хранилище?

### День 190 — RBAC: контроль доступа
- 📺 **Теория (1,5 ч):** Role, ClusterRole, RoleBinding, ServiceAccount. Принцип наименьших привилегий в K8s.
- 💻 **Практика (2,5 ч):** Разбери RBAC: `kubectl auth can-i`. Найди избыточные права. Инструмент: [rbac-tool](https://github.com/alcideio/rbac-tool).
- ✍️ **Задание:** найди ServiceAccount с лишними правами в учебном кластере.
- 🎯 **Проверь себя:** как проверить, что может конкретный ServiceAccount?

### День 191 — Kubernetes Goat: атаки
- 💻 **Практика (4 ч):** [Kubernetes Goat](https://madhuakula.com/kubernetes-goat/) — пройди сценарии: доступ к metadata, container escape, чтение secrets, RBAC privesc, доступ к kubelet.
- ✍️ **Задание:** write-up 2 атак на кластер.
- 🎯 **Проверь себя:** как из скомпрометированного pod'а добраться до всего кластера?

### День 192 — Container & Pod Escape
- 📺 **Теория (1,5 ч):** побег из контейнера в хост: privileged pod, hostPath, hostPID, capabilities.
- 💻 **Практика (2,5 ч):** Kubernetes Goat / [kube-hunter](https://github.com/aquasecurity/kube-hunter). Выполни pod escape в учебном кластере.
- ✍️ **Задание:** объясни цепочку «pod → node → кластер».
- 🎯 **Проверь себя:** что даёт `hostPath` монтирование атакующему?

### День 193 — Защита кластера: политики
- 📺 **Теория (1,5 ч):** Admission Controllers, [Kyverno](https://kyverno.io/), [OPA/Gatekeeper](https://open-policy-agent.github.io/gatekeeper/), Pod Security Standards, Network Policies.
- 💻 **Практика (2 ч):** Напиши политику, запрещающую privileged-pod'ы. Настрой NetworkPolicy.
- ✍️ **Задание:** политика, блокирующая опасные конфигурации.
- 🎯 **Проверь себя:** как admission controller останавливает опасный pod до запуска?

### День 194 — Обнаружение в кластере: Falco
- 📺 **Теория (1,5 ч):** [Falco](https://falco.org/) — runtime-детект аномалий в контейнерах.
- 💻 **Практика (2 ч):** Установи Falco, вызови подозрительное действие (shell в контейнере), поймай алерт.
- ✍️ **Задание:** правило Falco на подозрительную активность.
- 🎯 **Проверь себя:** что Falco видит, чего не видит статический сканер?

---

## Неделя 27 — AWS Security

### День 195 — Основы AWS и IAM
- 📺 **Теория (2 ч):** [AWS для начинающих (YouTube, русский)](https://www.youtube.com/results?search_query=aws+основы+для+начинающих). IAM: users, roles, policies, principle of least privilege. Заведи Free Tier аккаунт (с осторожностью по биллингу).
- 💻 **Практика (1,5 ч):** Создай IAM-пользователя, роль, политику. Установи и настрой `aws cli`.
- ✍️ **Задание:** объясни разницу IAM user / role / policy.
- 🎯 **Проверь себя:** почему роль безопаснее вшитых ключей?

### День 196 — flaws.cloud
- 💻 **Практика (4 ч):** Пройди [flaws.cloud](http://flaws.cloud/) — легендарный бесплатный AWS-полигон. Учит: открытый S3, утечка ключей, IAM-эскалация, шаг за шагом.
- ✍️ **Задание:** write-up прохождения flaws.cloud.
- 🎯 **Проверь себя:** как один открытый S3-бакет ведёт к захвату аккаунта?

### День 197 — S3 и хранилища
- 📺 **Теория (1,5 ч):** S3 bucket policies, ACL, public access, частые мисконфиги.
- 💻 **Практика (2,5 ч):** Найди публичные бакеты (в своей учебной среде). Инструменты: [S3Scanner](https://github.com/sa7mon/S3Scanner). Настрой безопасный бакет.
- ✍️ **Задание:** чек-лист безопасной настройки S3.
- 🎯 **Проверь себя:** какие 3 настройки чаще всего делают бакет публичным по ошибке?

### День 198 — flaws2.cloud + IAM privesc
- 💻 **Практика (4 ч):** Пройди [flaws2.cloud](http://flaws2.cloud/) (есть трек атакующего и защитника). Изучи [IAM privesc пути](https://github.com/RhinoSecurityLabs/Security-Research/tree/master/tools/aws-pentest-tools).
- ✍️ **Задание:** write-up цепочки повышения привилегий в IAM.
- 🎯 **Проверь себя:** что такое `iam:PassRole` и почему это опасно?

### День 199 — CloudGoat: сценарии атак
- 💻 **Практика (4 ч):** [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) — разверни и пройди сценарий (напр. `iam_privesc_by_rollback`). Инструмент разведки: [Pacu](https://github.com/RhinoSecurityLabs/pacu), [ScoutSuite](https://github.com/nccgroup/ScoutSuite).
- ✍️ **Задание:** write-up сценария CloudGoat.
- 🎯 **Проверь себя:** как Pacu помогает в облачном пентесте?

### День 200 — Cloud Blue Team: логи и детект
- 📺 **Теория (1,5 ч):** [CloudTrail](https://aws.amazon.com/cloudtrail/) (логи API), [GuardDuty](https://aws.amazon.com/guardduty/) (детект угроз), [AWS Config](https://aws.amazon.com/config/).
- 💻 **Практика (2 ч):** Разбери события CloudTrail. Пойми, как обнаружить атаку из недели по логам.
- ✍️ **Задание:** какие события CloudTrail = признак компрометации?
- 🎯 **Проверь себя:** как задетектить создание нового IAM-ключа злоумышленником?

### День 201 — Повторение недели
- 💻 **Практика (3,5 ч):** Ещё один CloudGoat-сценарий или Pwned Labs.
- ✍️ **Задание:** обнови портфолио облачными разборами.
- 🎯 **Проверь себя:** видишь связку «атака в облаке → её след в CloudTrail»?

---

## Неделя 28 — Azure/GCP, аудит и закрепление

### День 202 — Azure security (обзор)
- 📺 **Теория (2 ч):** [Azure security основы](https://www.youtube.com/results?search_query=azure+security+основы). Entra ID (AzureAD), RBAC, Managed Identity, частые мисконфиги.
- 💻 **Практика (1,5 ч):** THM/Pwned Labs комната по Azure.
- ✍️ **Задание:** сравни модель IAM в AWS и Azure.
- 🎯 **Проверь себя:** что такое Managed Identity?

### День 203 — GCP security (обзор)
- 📺 **Теория (1,5 ч):** GCP IAM, service accounts, частые ошибки.
- 💻 **Практика (2 ч):** [GCP Goat](https://github.com/ine-labs/GCPGoat) или обучающая лаба.
- ✍️ **Задание:** заметка по GCP-мисконфигам.
- 🎯 **Проверь себя:** чем service account в GCP похож на IAM role в AWS?

### День 204 — Cloud-аудит автоматом
- 📺 **Теория (1 ч):** [Prowler](https://github.com/prowler-cloud/prowler), [ScoutSuite](https://github.com/nccgroup/ScoutSuite) — автоаудит облака.
- 💻 **Практика (2,5 ч):** Прогони Prowler на своём аккаунте (в рамках Free Tier), разбери находки.
- ✍️ **Задание:** отчёт аудита с приоритизацией.
- 🎯 **Проверь себя:** какие мисконфиги Prowler находит первыми?

### День 205 — Комплексная облачная машина
- 💻 **Практика (4 ч):** Полный сценарий: разведка → доступ (утёкший ключ/открытый бакет) → IAM privesc → захват. Pwned Labs / CloudGoat.
- ✍️ **Задание:** полный write-up.
- 🎯 **Проверь себя:** цепочка облачной атаки уложилась?

### День 206 — Резервный день
- 💻 **Практика (4 ч):** Догоняй хвосты Cloud/K8s.
- ✍️ **Задание:** порядок в портфолио.
- 🎯 **Проверь себя:** долгов нет?

### День 207 — Экзамен месяца (Cloud + K8s)
- 💻 **Практика (4,5 ч), сам:** см. [exams.md](exams.md) → Экзамен 4 (Cloud) и Экзамен 5 (Kubernetes). Найди открытый S3, кривой IAM, лишние права; в кластере — Secret, RBAC-эскалацию, container escape. Отчёт.
- ✍️ **Задание:** отчёт «Итоги месяца 7».
- 🎯 **Проверь себя:** справился — облако и контейнеры больше не чёрный ящик.

### День 208 — Разбор
- 📺 **Разбор (2 ч):** пересмотри облачные разборы, отточи методику облачного пентеста/аудита.
- ✍️ **Задание:** чек-лист облачного аудита.
- 🎯 **Проверь себя:** —

### День 209 — Проект недели
- 💻 **Практика (4 ч):** Начни [проект №8 — Cloud Misconfiguration Scanner](projects.md) (на Python, твоя сильная сторона).
- ✍️ **Задание:** каркас сканера на GitHub.
- 🎯 **Проверь себя:** —

### День 210 — Рефлексия месяца
- ✍️ **Задание:** отметь дни в [progress.md](progress.md). Отдохни.
- 🎯 **Проверь себя:** ты закрыл самый большой пробел рынка.

---

## Итог месяца 7 — что ты теперь умеешь

- ✅ Docker: аудит образов (Trivy/Grype), хардненинг, escape
- ✅ Kubernetes: RBAC, secrets, pod/container escape, политики (Kyverno/OPA), Falco
- ✅ AWS: IAM privesc, S3, CloudGoat/flaws.cloud, аудит (Prowler/ScoutSuite), детект (CloudTrail/GuardDuty)
- ✅ Обзор Azure/GCP
- ✅ Проект: облачный сканер мисконфигов на Python

**Следующий шаг:** [month-08-devsecops-detection.md](month-08-devsecops-detection.md) — DevSecOps, Detection Engineering и EDR.
