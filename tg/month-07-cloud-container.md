# Моҳи 7 — Cloud & Container Security (Фазаи 2)

**Мақсади моҳ:** пӯшонидани холигии бузургтарини бозор — абр (cloud) ва контейнерҳо. Қариб ҳар ширкат дар соли 2026 дар AWS/Azure/GCP зиндагӣ мекунад ва Docker + Kubernetes-ро мегардонад. Junior-е ки метавонад S3-и кушода, IAM-и нодуруст ва container escape-ро ёбад, ба таври назаррас гаронтар меарзад.

**Пешшарт:** моҳҳои 1–6 гузашта. Ту аллакай ҳамла ва ҳифзи классикаро медонӣ — акнун маҳоратро ба абр мекӯчонем.

**Захираҳои асосии моҳ:**
- ☁️ [flaws.cloud](http://flaws.cloud/) ва [flaws2.cloud](http://flaws2.cloud/) — майдончаҳои ройгони AWS
- 🐐 [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat), [AWSGoat](https://github.com/ine-labs/AWSGoat), [Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat)
- 🎓 [Pwned Labs](https://pwnedlabs.io/) — лабҳои абрии ройгон
- 🐳 [Docker](https://docs.docker.com/), [Trivy](https://github.com/aquasecurity/trivy), [Docker Bench](https://github.com/docker/docker-bench-security)

> ⚠️ Дар аккаунти AWS-и худат billing-alert ва Free Tier дошта бош — абр метавонад барои захираҳои фаромӯшшуда пул гирад. Ҳамаро баъди лаб хомӯш кун.

---

## Ҳафтаи 25 — Docker Security

### Рӯзи 181 — Асосҳои контейнерҳо
- 📺 **Назария (1,5 соат):** Docker аз сифр. Образ (image), контейнер, қабатҳо, реестр, фарқи VM vs контейнер.
- 💻 **Амалия (2 соат):** Docker-ро насб кун. `docker run`, `docker ps`, `docker exec -it`, `docker images`. nginx-ро оғоз кун, ба дохили контейнер даро.
- ✍️ **Супориш:** фарқи «образ vs контейнер» ва «контейнер vs виртуалка»-ро шарҳ деҳ.
- 🎯 **Худро санҷ:** чаро контейнер аз виртуалка сабуктар аст?

### Рӯзи 182 — Dockerfile ва чӣ тавр образҳо сохта мешаванд
- 📺 **Назария (1,5 соат):** Dockerfile, `docker build`, қабатҳо, кэш, multi-stage build.
- 💻 **Амалия (2 соат):** Образи худро бо барномаи Python соз. Таҳлил кун, аз чӣ иборат аст: `docker history`.
- ✍️ **Супориш:** Dockerfile барои скрипти содда нависон.
- 🎯 **Худро санҷ:** дар ҳар қабат чӣ ба образ меафтад?

### Рӯзи 183 — Осебпазириҳои контейнерҳо
- 📺 **Назария (1,5 соат):** Docker security. Сирҳо дар образҳо, контейнери имтиёзнок, монтажи docker.sock, root дар дохили контейнер.
- 💻 **Амалия (2,5 соат):** [Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat) сенарияҳои Docker дорад; ё лабҳои алоҳидаи Docker-escape. Таҳлил кун, ки чаро `--privileged` = сӯрох.
- ✍️ **Супориш:** шарҳ деҳ, чаро монтажи `/var/run/docker.sock` ба контейнер мумкин нест.
- 🎯 **Худро санҷ:** root дар дохили контейнери имтиёзнок ба ҳамлакунанда чӣ медиҳад?

### Рӯзи 184 — Сканкунии образҳо: Trivy, Grype
- 📺 **Назария (1 соат):** сканерҳои осебпазирии образҳо, SCA (software composition analysis).
- 💻 **Амалия (2,5 соат):** [Trivy](https://github.com/aquasecurity/trivy) ва [Grype](https://github.com/anchore/grype)-ро насб кун. Образи худ ва як образи оммавиро скан кун. Ҳисоботро таҳлил кун: CVE, severity, fixed version.
- ✍️ **Супориш:** дар образи куҳна (масалан `python:3.6`) осебпазириҳо ёб, рӯйхати критикӣ тартиб деҳ.
- 🎯 **Худро санҷ:** CVE чист ва чӣ тавр ҳисоботи Trivy-ро хондан?

### Рӯзи 185 — Хардненинги Docker
- 📺 **Назария (1,5 соат):** [Docker Bench](https://github.com/docker/docker-bench-security), CIS Docker Benchmark, non-root user, read-only fs, capabilities drop.
- 💻 **Амалия (2 соат):** Docker Bench-ро дар хости худ иҷро кун. Dockerfile-ро бехатар нависон: non-root, образи асосии минималӣ (distroless/alpine), бе сирҳо.
- ✍️ **Супориш:** «то/баъд» — Dockerfile-и нобехатар ва бехатар бо шарҳҳо.
- 🎯 **Худро санҷ:** 4 қоидаи Dockerfile-и бехатарро ном бар.

### Рӯзи 186 — Docker Compose ва сирҳо
- 📺 **Назария (1,5 соат):** docker-compose, volumes, networks, идоракунии сирҳо (на дар env!).
- 💻 **Амалия (2 соат):** Стеки 2–3 хидматро тавассути compose боло кун. Таҳлил кун, дар куҷо сирҳо мерезанд ва чӣ тавр дуруст.
- ✍️ **Супориш:** сиреро ки дар тағйирёбандаҳои муҳити контейнер «фаромӯш» шудааст ёб.
- 🎯 **Худро санҷ:** чаро сирҳо дар `ENV`/`docker inspect` — бад аст?

### Рӯзи 187 — Такрори ҳафта + лоиҳаи хурд
- 💻 **Амалия (3 соат):** Образи осебпазирро гир, мушкилотро ёб (Trivy + аз назар гузаронӣ), ислоҳ кун, аз нав бехатар соз.
- ✍️ **Супориш (лоиҳаи хурд):** репозиторийи «Docker security audit» дар GitHub: ёфтаҳо + ислоҳҳо.
- 🎯 **Худро санҷ:** аудити образро аз аввал то охир гузаронда метавонӣ?

---

## Ҳафтаи 26 — Kubernetes Security

### Рӯзи 188 — Kubernetes чист
- 📺 **Назария (2 соат):** Kubernetes барои навомӯзон. Pod, Node, Namespace, Deployment, Service, control plane.
- 💻 **Амалия (1,5 соат):** [minikube](https://minikube.sigs.k8s.io/) ё [kind](https://kind.sigs.k8s.io/)-ро насб кун. `kubectl get pods/nodes/ns`, аввалин pod-ро паҳн кун.
- ✍️ **Супориш:** нақшаи кластери K8s: control plane + worker nodes + чӣ куҷо.
- 🎯 **Худро санҷ:** Pod чист ва аз контейнер чӣ фарқ дорад?

### Рӯзи 189 — kubectl ва объектҳои кластер
- 📺 **Назария (1,5 соат):** Deployments, Services, ConfigMaps, Secrets, Ingress.
- 💻 **Амалия (2 соат):** Объектҳоро тавассути `kubectl` соз/бубин. Secret-ро хон: `kubectl get secret -o yaml` — қайд кун, ки ин танҳо base64 аст, на рамзгузорӣ!
- ✍️ **Супориш:** Secret-ро аз кластери таълимӣ гир ва рамзкушоӣ кун.
- 🎯 **Худро санҷ:** чаро K8s Secret ба таври пешфарз анбори бехатар НЕСТ?

### Рӯзи 190 — RBAC: назорати дастрасӣ
- 📺 **Назария (1,5 соат):** Role, ClusterRole, RoleBinding, ServiceAccount. Принсипи камтарин имтиёз дар K8s.
- 💻 **Амалия (2,5 соат):** RBAC-ро таҳлил кун: `kubectl auth can-i`. Ҳуқуқи зиёдатиро ёб. Асбоб: [rbac-tool](https://github.com/alcideio/rbac-tool).
- ✍️ **Супориш:** ServiceAccount-и дорои ҳуқуқи зиёдатиро дар кластери таълимӣ ёб.
- 🎯 **Худро санҷ:** чӣ тавр санҷидан, ки ServiceAccount-и мушаххас чӣ карда метавонад?

### Рӯзи 191 — Kubernetes Goat: ҳамлаҳо
- 💻 **Амалия (4 соат):** [Kubernetes Goat](https://madhuakula.com/kubernetes-goat/) — сенарияҳоро гузар: дастрасӣ ба metadata, container escape, хондани secrets, RBAC privesc, дастрасӣ ба kubelet.
- ✍️ **Супориш:** write-up-и 2 ҳамла ба кластер.
- 🎯 **Худро санҷ:** чӣ тавр аз pod-и компрометатсияшуда ба тамоми кластер расидан?

### Рӯзи 192 — Container & Pod Escape
- 📺 **Назария (1,5 соат):** гурез аз контейнер ба хост: privileged pod, hostPath, hostPID, capabilities.
- 💻 **Амалия (2,5 соат):** Kubernetes Goat / [kube-hunter](https://github.com/aquasecurity/kube-hunter). Pod escape-ро дар кластери таълимӣ иҷро кун.
- ✍️ **Супориш:** занҷири «pod → node → кластер»-ро шарҳ деҳ.
- 🎯 **Худро санҷ:** монтажи `hostPath` ба ҳамлакунанда чӣ медиҳад?

### Рӯзи 193 — Ҳифзи кластер: сиёсатҳо
- 📺 **Назария (1,5 соат):** Admission Controllers, [Kyverno](https://kyverno.io/), [OPA/Gatekeeper](https://open-policy-agent.github.io/gatekeeper/), Pod Security Standards, Network Policies.
- 💻 **Амалия (2 соат):** Сиёсате нависон, ки privileged-pod-ҳоро манъ мекунад. NetworkPolicy танзим кун.
- ✍️ **Супориш:** сиёсате ки конфигуратсияҳои хатарнокро блок мекунад.
- 🎯 **Худро санҷ:** admission controller чӣ тавр pod-и хатарнокро то оғоз бозмедорад?

### Рӯзи 194 — Ошкор дар кластер: Falco
- 📺 **Назария (1,5 соат):** [Falco](https://falco.org/) — детекти runtime-и аномалияҳо дар контейнерҳо.
- 💻 **Амалия (2 соат):** Falco-ро насб кун, амали шубҳанокро (shell дар контейнер) даъват кун, алертро гир.
- ✍️ **Супориш:** қоидаи Falco дар фаъолияти шубҳанок.
- 🎯 **Худро санҷ:** Falco чиро мебинад, ки сканери статикӣ намебинад?

---

## Ҳафтаи 27 — AWS Security

### Рӯзи 195 — Асосҳои AWS ва IAM
- 📺 **Назария (2 соат):** AWS барои навомӯзон. IAM: users, roles, policies, принсипи камтарин имтиёз. Аккаунти Free Tier соз (бо эҳтиёт оид ба биллинг).
- 💻 **Амалия (1,5 соат):** IAM-корбар, роль, сиёсат соз. `aws cli`-ро насб ва танзим кун.
- ✍️ **Супориш:** фарқи IAM user / role / policy-ро шарҳ деҳ.
- 🎯 **Худро санҷ:** чаро роль аз калидҳои вшитӣ бехатартар аст?

### Рӯзи 196 — flaws.cloud
- 💻 **Амалия (4 соат):** [flaws.cloud](http://flaws.cloud/)-ро гузар — майдончаи ройгони афсонавии AWS. Меомӯзонад: S3-и кушода, ихроҷи калидҳо, IAM-эскалатсия, қадам ба қадам.
- ✍️ **Супориш:** write-up-и гузариши flaws.cloud.
- 🎯 **Худро санҷ:** чӣ тавр як бакети S3-и кушода ба забти аккаунт мебарад?

### Рӯзи 197 — S3 ва анборҳо
- 📺 **Назария (1,5 соат):** S3 bucket policies, ACL, public access, мисконфигҳои маъмул.
- 💻 **Амалия (2,5 соат):** Бакетҳои оммавиро ёб (дар муҳити таълимии худ). Асбобҳо: [S3Scanner](https://github.com/sa7mon/S3Scanner). Бакети бехатар танзим кун.
- ✍️ **Супориш:** чек-листи танзими бехатари S3.
- 🎯 **Худро санҷ:** кадом 3 танзим бештар бакетро тасодуфан оммавӣ мекунанд?

### Рӯзи 198 — flaws2.cloud + IAM privesc
- 💻 **Амалия (4 соат):** [flaws2.cloud](http://flaws2.cloud/)-ро гузар (роҳи ҳамлакунанда ва ҳифзкунанда дорад). [Роҳҳои IAM privesc](https://github.com/RhinoSecurityLabs/Security-Research/tree/master/tools/aws-pentest-tools)-ро омӯз.
- ✍️ **Супориш:** write-up-и занҷири баланд бардоштани имтиёзҳо дар IAM.
- 🎯 **Худро санҷ:** `iam:PassRole` чист ва чаро хатарнок аст?

### Рӯзи 199 — CloudGoat: сенарияҳои ҳамла
- 💻 **Амалия (4 соат):** [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) — сенарияро паҳн ва гузар (масалан `iam_privesc_by_rollback`). Асбоби иктишоф: [Pacu](https://github.com/RhinoSecurityLabs/pacu), [ScoutSuite](https://github.com/nccgroup/ScoutSuite).
- ✍️ **Супориш:** write-up-и сенарияи CloudGoat.
- 🎯 **Худро санҷ:** Pacu дар pentest-и абрӣ чӣ тавр кӯмак мекунад?

### Рӯзи 200 — Cloud Blue Team: логҳо ва детект
- 📺 **Назария (1,5 соат):** [CloudTrail](https://aws.amazon.com/cloudtrail/) (логҳои API), [GuardDuty](https://aws.amazon.com/guardduty/) (детекти таҳдидҳо), [AWS Config](https://aws.amazon.com/config/).
- 💻 **Амалия (2 соат):** Ҳодисаҳои CloudTrail-ро таҳлил кун. Бифаҳм, ки чӣ тавр ҳамлаи ҳафтаро аз рӯи логҳо ошкор кардан.
- ✍️ **Супориш:** кадом ҳодисаҳои CloudTrail = аломати компрометатсия?
- 🎯 **Худро санҷ:** чӣ тавр сохтани калиди нави IAM аз ҷониби бадкор детект кардан?

### Рӯзи 201 — Такрори ҳафта
- 💻 **Амалия (3,5 соат):** Боз як сенарияи CloudGoat ё Pwned Labs.
- ✍️ **Супориш:** портфолиоро бо таҳлилҳои абрӣ нав кун.
- 🎯 **Худро санҷ:** пайванди «ҳамла дар абр → осораш дар CloudTrail»-ро мебинӣ?

---

## Ҳафтаи 28 — Azure/GCP, аудит ва мустаҳкамкунӣ

### Рӯзи 202 — Azure security (шарҳ)
- 📺 **Назария (2 соат):** Асосҳои Azure security. Entra ID (AzureAD), RBAC, Managed Identity, мисконфигҳои маъмул.
- 💻 **Амалия (1,5 соат):** Комнатаи THM/Pwned Labs оид ба Azure.
- ✍️ **Супориш:** модели IAM-ро дар AWS ва Azure муқоиса кун.
- 🎯 **Худро санҷ:** Managed Identity чист?

### Рӯзи 203 — GCP security (шарҳ)
- 📺 **Назария (1,5 соат):** GCP IAM, service accounts, хатоҳои маъмул.
- 💻 **Амалия (2 соат):** [GCP Goat](https://github.com/ine-labs/GCPGoat) ё лаби таълимӣ.
- ✍️ **Супориш:** қайд оид ба GCP-мисконфигҳо.
- 🎯 **Худро санҷ:** service account дар GCP ба IAM role дар AWS чӣ монандӣ дорад?

### Рӯзи 204 — Аудити абр ба таври худкор
- 📺 **Назария (1 соат):** [Prowler](https://github.com/prowler-cloud/prowler), [ScoutSuite](https://github.com/nccgroup/ScoutSuite) — аудити худкори абр.
- 💻 **Амалия (2,5 соат):** Prowler-ро дар аккаунти худ иҷро кун (дар доираи Free Tier), ёфтаҳоро таҳлил кун.
- ✍️ **Супориш:** ҳисоботи аудит бо афзалиятбандӣ.
- 🎯 **Худро санҷ:** кадом мисконфигҳоро Prowler аввал меёбад?

### Рӯзи 205 — Мошини комплексии абрӣ
- 💻 **Амалия (4 соат):** Сенарияи пурра: иктишоф → дастрасӣ (калиди ихроҷшуда/бакети кушода) → IAM privesc → забт. Pwned Labs / CloudGoat.
- ✍️ **Супориш:** write-up-и пурра.
- 🎯 **Худро санҷ:** занҷири ҳамлаи абрӣ ҷой гирифт?

### Рӯзи 206 — Рӯзи захиравӣ
- 💻 **Амалия (4 соат):** Қарзҳои Cloud/K8s-ро гир.
- ✍️ **Супориш:** портфолиоро ба тартиб ор.
- 🎯 **Худро санҷ:** қарз нест?

### Рӯзи 207 — Имтиҳони моҳ (Cloud + K8s)
- 💻 **Амалия (4,5 соат), худат:** нигаред [exams](exams.md) → Имтиҳони 4 (Cloud) ва Имтиҳони 5 (Kubernetes). S3-и кушода, IAM-и нодуруст, ҳуқуқи зиёдатӣ ёб; дар кластер — Secret, RBAC-эскалатсия, container escape. Ҳисобот.
- ✍️ **Супориш:** ҳисобот «Натиҷаҳои моҳи 7».
- 🎯 **Худро санҷ:** гузаштӣ — абр ва контейнерҳо дигар қуттии сиёҳ нестанд.

### Рӯзи 208 — Таҳлил
- 📺 **Таҳлил (2 соат):** таҳлилҳои абриро аз нав бубин, методикаи pentest/аудити абриро тез кун.
- ✍️ **Супориш:** чек-листи аудити абрӣ.
- 🎯 **Худро санҷ:** —

### Рӯзи 209 — Лоиҳаи ҳафта
- 💻 **Амалия (4 соат):** [Лоиҳаи №8 — Cloud Misconfiguration Scanner](projects.md)-ро оғоз кун (дар Python, ҷониби қавии ту).
- ✍️ **Супориш:** каркаси сканер дар GitHub.
- 🎯 **Худро санҷ:** —

### Рӯзи 210 — Мулоҳизаи моҳ
- ✍️ **Супориш:** рӯзҳоро дар [progress](progress.md) қайд кун. Истироҳат кун.
- 🎯 **Худро санҷ:** ту бузургтарин холигии бозорро пӯшондӣ.

---

## Натиҷаи моҳи 7 — ту акнун чӣ метавонӣ

- ✅ Docker: аудити образҳо (Trivy/Grype), хардненинг, escape
- ✅ Kubernetes: RBAC, secrets, pod/container escape, сиёсатҳо (Kyverno/OPA), Falco
- ✅ AWS: IAM privesc, S3, CloudGoat/flaws.cloud, аудит (Prowler/ScoutSuite), детект (CloudTrail/GuardDuty)
- ✅ Шарҳи Azure/GCP
- ✅ Лоиҳа: сканери абрии мисконфигҳо дар Python

**Қадами навбатӣ:** Моҳи 8 ([month-08](month-08-devsecops-detection.md)) — DevSecOps, Detection Engineering ва EDR.

> ✅ Ҳамаи 9 моҳ ва файлҳои курс бо тоҷикӣ тайёранд.
