/* ============================================================
   CyberSec Course — app logic
   Прогресс хранится в localStorage. Данные — из data.js (автоген).
   ============================================================ */
(() => {
'use strict';

const DATA = window.COURSE_DATA || {};
const LS = { lang:'csc.lang', days:'csc.days', exams:'csc.exams', projects:'csc.projects', quiz:'csc.quiz' };
const TOTAL_DAYS = 270;

/* ---------- i18n ---------- */
const I18N = {
  ru:{
    skip:'К основному содержанию', nav_roadmap:'Карта', nav_months:'Месяцы', nav_ach:'Достижения',
    search:'Поиск',
    hero_kick:'Бесплатно · Открытый исходный код · RU + TJ',
    hero_h1a:'От нуля до', hero_h1b:'за 270 дней',
    hero_sub:'Полный курс кибербезопасности: сети, Linux, веб, пентест, Active Directory, SOC, облако, DevSecOps и AI Security. Каждый день — теория, практика и задание.',
    cta_start:'Начать с Дня 1', cta_continue:'Продолжить с Дня', cta_map:'Посмотреть карту',
    cta_done:'Курс пройден — открыть заново',
    s_days:'Дней', s_months:'Месяцев', s_exams:'Экзаменов', s_proj:'Проектов',
    t_cmd:'./progress --user me',
    rm_h:'Карта курса', rm_p:'Две фазы: фундамент делает тебя нанимаемым, современный стек — конкурентоспособным.',
    ph1_h:'Фундамент', ph1_m:'Дни 1–180', ph2_h:'Современный стек', ph2_m:'Дни 181–270',
    mo_h:'Девять месяцев', mo_p:'Открой месяц, чтобы увидеть все дни с теорией, практикой и заданиями.',
    ac_h:'Достижения', ac_p:'Ранги за пройденный путь. Diamond требует ещё экзамены и проекты.',
    ac_exams:'Экзамены', ac_projects:'Проекты',
    back:'Все месяцы', prev:'Назад', next:'Вперёд',
    ftr_legal:'Практика только на своих машинах и легальных полигонах. Атака чужих систем без письменного разрешения — уголовное преступление.',
    ftr_free:'Курс бесплатный и открытый',
    theory:'Теория', practice:'Практика', task:'Задание', check:'Проверь себя',
    materials:'Материалы дня', quiz:'Проверка знаний', passed:'сдано',
    video:'Видео к уроку', video_month:'Видеокурс месяца',
    video_month_hint:'Для этого дня отдельного ролика нет — смотри курс месяца целиком.',
    play:'Смотреть', playlist:'плейлист', yt_search:'поиск на YouTube',
    month_materials:'Ресурсы месяца', month_materials_hint:'У этого дня нет отдельных ссылок — работай с основными ресурсами месяца.',
    right:'Верно!', wrong:'Неверно.', retry:'Попробовать снова',
    no_quiz:'Теста для этого дня пока нет — ответь себе честно и двигайся дальше.',
    locked_day:'Сначала пройди проверку', locked_hint:'Ответь правильно на вопрос проверки, чтобы отметить день пройденным',
    done:'Отметить пройденным', undone:'Пройдено — снять отметку',
    day:'День', week:'Неделя', month:'Месяц', days_of:'дней',
    ph1:'ФАЗА 1', ph2:'ФАЗА 2',
    ph_search:'Найти день, тему или инструмент…',
    no_res:'Ничего не найдено. Попробуй другое слово.',
    rank_none:'ранг: не начат', rank_pre:'ранг:',
    next_to:'до следующего ранга:', all_done:'все ранги получены',
    locked:'закрыто', unlocked:'получено',
    note_recap:'День повторения: новой теории нет — работай со своими конспектами, недоделками и журналом.',
    note_no_theory:'Практический день: новой теории нет, всё закрепляем руками.',
    reset:'Сбросить весь прогресс', reset_hint:'Прогресс хранится только в этом браузере',
    reset_confirm:'Сбросить весь прогресс: пройденные дни, тесты, экзамены и проекты? Отменить нельзя.',
    r_bronze:'Bronze', r_silver:'Silver', r_gold:'Gold', r_diamond:'Diamond',
    rq_bronze:'30 дней подряд пройдено', rq_silver:'90 дней — фундамент заложен',
    rq_gold:'180 дней — вся Фаза 1', rq_diamond:'270 дней + 6 экзаменов + 10 проектов',
  },
  tg:{
    skip:'Ба мазмуни асосӣ', nav_roadmap:'Харита', nav_months:'Моҳҳо', nav_ach:'Дастовардҳо',
    search:'Ҷустуҷӯ',
    hero_kick:'Ройгон · Кушода · RU + TJ',
    hero_h1a:'Аз сифр то', hero_h1b:'дар 270 рӯз',
    hero_sub:'Курси пурраи амнияти киберӣ: шабакаҳо, Linux, веб, pentest, Active Directory, SOC, абр, DevSecOps ва AI Security. Ҳар рӯз — назария, амалия ва супориш.',
    cta_start:'Аз Рӯзи 1 оғоз кун', cta_continue:'Идома аз Рӯзи', cta_map:'Харитаро бубин',
    cta_done:'Курс тамом шуд — аз нав кушо',
    s_days:'Рӯз', s_months:'Моҳ', s_exams:'Имтиҳон', s_proj:'Лоиҳа',
    t_cmd:'./progress --user me',
    rm_h:'Харитаи курс', rm_p:'Ду фаза: асос туро қобили киро мекунад, стеки муосир — рақобатпазир.',
    ph1_h:'Асос', ph1_m:'Рӯзҳои 1–180', ph2_h:'Стеки муосир', ph2_m:'Рӯзҳои 181–270',
    mo_h:'Нӯҳ моҳ', mo_p:'Моҳро кушо, то ҳамаи рӯзҳоро бо назария, амалия ва супоришҳо бубинӣ.',
    ac_h:'Дастовардҳо', ac_p:'Рангҳо барои роҳи гузашта. Diamond имтиҳонҳо ва лоиҳаҳоро низ талаб мекунад.',
    ac_exams:'Имтиҳонҳо', ac_projects:'Лоиҳаҳо',
    back:'Ҳамаи моҳҳо', prev:'Қафо', next:'Пеш',
    ftr_legal:'Амалия танҳо дар мошинҳои худат ва майдончаҳои қонунӣ. Ҳамла ба системаҳои бегона бе иҷозати хаттӣ ҷиноят аст.',
    ftr_free:'Курс ройгон ва кушода аст',
    theory:'Назария', practice:'Амалия', task:'Супориш', check:'Худро санҷ',
    materials:'Маводҳои рӯз', quiz:'Санҷиши дониш', passed:'супорида шуд',
    video:'Видео ба дарс', video_month:'Видеокурси моҳ',
    video_month_hint:'Барои ин рӯз видеои алоҳида нест — курси моҳро тамошо кун.',
    play:'Тамошо', playlist:'плейлист', yt_search:'ҷустуҷӯ дар YouTube',
    month_materials:'Захираҳои моҳ', month_materials_hint:'Ин рӯз пайванди алоҳида надорад — бо захираҳои асосии моҳ кор кун.',
    right:'Дуруст!', wrong:'Нодуруст.', retry:'Аз нав кӯшиш кун',
    no_quiz:'Барои ин рӯз ҳанӯз тест нест — ба худат ростқавлона ҷавоб деҳ ва пеш рав.',
    locked_day:'Аввал санҷишро гузар', locked_hint:'Ба саволи санҷиш дуруст ҷавоб деҳ, то рӯзро гузашта қайд кунӣ',
    done:'Гузашта қайд кун', undone:'Гузашт — қайдро бардор',
    day:'Рӯз', week:'Ҳафта', month:'Моҳ', days_of:'рӯз',
    ph1:'ФАЗАИ 1', ph2:'ФАЗАИ 2',
    ph_search:'Рӯз, мавзӯъ ё асбобро ёб…',
    no_res:'Чизе ёфт нашуд. Калимаи дигарро санҷ.',
    rank_none:'ранг: оғоз нашуд', rank_pre:'ранг:',
    next_to:'то ранги навбатӣ:', all_done:'ҳамаи рангҳо гирифта шуд',
    locked:'пӯшида', unlocked:'гирифта шуд',
    note_recap:'Рӯзи такрор: назарияи нав нест — бо конспект, қарзҳо ва дафтарчаи худ кор кун.',
    note_no_theory:'Рӯзи амалӣ: назарияи нав нест, ҳамаро бо даст мустаҳкам мекунем.',
    reset:'Тамоми пешрафтро тоза кун', reset_hint:'Пешрафт танҳо дар ҳамин браузер нигоҳ дошта мешавад',
    reset_confirm:'Тамоми пешрафт тоза шавад: рӯзҳо, тестҳо, имтиҳонҳо ва лоиҳаҳо? Бозгашт нест.',
    r_bronze:'Bronze', r_silver:'Silver', r_gold:'Gold', r_diamond:'Diamond',
    rq_bronze:'30 рӯз гузашт', rq_silver:'90 рӯз — асос гузошта шуд',
    rq_gold:'180 рӯз — тамоми Фазаи 1', rq_diamond:'270 рӯз + 6 имтиҳон + 10 лоиҳа',
  }
};

const EXAMS = {
  ru:['Linux (после месяца 2)','Web (после месяца 3)','Blue Team (после месяца 5/8)','Cloud / AWS (после месяца 7)','Kubernetes (после месяца 7)','AI Security (после месяца 9)'],
  tg:['Linux (баъд аз моҳи 2)','Web (баъд аз моҳи 3)','Blue Team (баъд аз моҳи 5/8)','Cloud / AWS (баъд аз моҳи 7)','Kubernetes (баъд аз моҳи 7)','AI Security (баъд аз моҳи 9)']
};
const PROJECTS = {
  ru:['Мини-SIEM','Log Analyzer','Burp Suite Extension','Nmap Dashboard','Password Audit Tool','IOC Scanner','Docker Security Scanner','Cloud Misconfig Scanner','Prompt Injection Scanner','Полный Pentest Report'],
  tg:['Мини-SIEM','Log Analyzer','Burp Suite Extension','Nmap Dashboard','Password Audit Tool','IOC Scanner','Docker Security Scanner','Cloud Misconfig Scanner','Prompt Injection Scanner','Pentest Report-и пурра']
};

const RANKS = [
  { key:'bronze',  need:30,  color:'var(--bronze)'  },
  { key:'silver',  need:90,  color:'var(--silver)'  },
  { key:'gold',    need:180, color:'var(--gold)'    },
  { key:'diamond', need:270, color:'var(--diamond)', extra:true },
];

const ICONS = {
  theory:'<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2.5" y="3.5" width="15" height="11" rx="2"/><path d="M7 17.5h6" stroke-linecap="round"/></svg>',
  practice:'<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 7l-3 3 3 3M14 7l3 3-3 3M11.5 4l-3 12"/></svg>',
  task:'<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2.5l3.5 3.5L8 15.5l-4.5 1L5 12z"/></svg>',
  check:'<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="10" cy="10" r="7.5"/><path d="M6.8 10.2l2.2 2.2 4.2-4.6"/></svg>',
  tickOn:'<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 10.5l3.5 3.5 7.5-8"/></svg>',
  medal:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="14.5" r="6"/><path d="M12 11.5l1 2.2 2.4.3-1.8 1.7.5 2.4-2.1-1.2-2.1 1.2.5-2.4-1.8-1.7 2.4-.3z"/><path d="M8.5 8.2L6 2h12l-2.5 6.2"/></svg>',
  play:'<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="1.5" y="4" width="17" height="12" rx="2.5"/><path d="M8.5 8.2l4 1.8-4 1.8z" fill="currentColor" stroke="none"/></svg>',
  playFill:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5.5v13l11-6.5z"/></svg>',
  link:'<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M8.5 11.5a3.5 3.5 0 005 0l2.5-2.5a3.5 3.5 0 10-5-5l-1 1"/><path d="M11.5 8.5a3.5 3.5 0 00-5 0L4 11a3.5 3.5 0 105 5l1-1"/></svg>',
};

/* ---------- state ---------- */
const load = (k, def) => { try{ return JSON.parse(localStorage.getItem(k)) ?? def; }catch{ return def; } };
const save = (k, v) => { try{ localStorage.setItem(k, JSON.stringify(v)); }catch{} };

let lang  = load(LS.lang, 'ru');
let done  = new Set(load(LS.days, []));
let exams = new Set(load(LS.exams, []));
let projs = new Set(load(LS.projects, []));
let quizOk = new Set(load(LS.quiz, []));   // дни, где тест сдан
let view  = { name:'home', month:null };
let drawerDay = null;
let lastFocus = null;   // элемент, с которого открыли модалку

const t  = k => (I18N[lang] && I18N[lang][k]) || I18N.ru[k] || k;
const months = () => DATA[lang] || DATA.ru || [];
const $  = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));

/* Markdown-ссылки [текст](url) -> кликабельные <a>. Вызывать ТОЛЬКО после esc():
   URL уже экранирован, поэтому в href попадает безопасная строка. Разрешаем только http/https. */
function linkify(escaped){
  return escaped.replace(/\[([^\]]+)\]\((https?:&#x2F;&#x2F;[^)\s]+|https?:\/\/[^)\s]+)\)/g,
    (_m, text, url) => `<a href="${url}" target="_blank" rel="noopener noreferrer">${text}</a>`);
}
const rich = s => linkify(esc(s));

/* В курсе дни пронумерованы сквозно (1..270): месяц 2 начинается с «День 31».
   Поэтому номер дня уже глобальный — арифметика по 30 дней тут не нужна. */
const gDay = (_mNum, dNum) => dNum;

/* ---------- i18n apply ---------- */
function applyI18n(){
  document.documentElement.lang = lang === 'tg' ? 'tg' : 'ru';
  document.documentElement.dataset.lang = lang;
  $$('[data-i18n]').forEach(el => {
    const k = el.dataset.i18n;
    if (I18N[lang] && I18N[lang][k]) el.textContent = I18N[lang][k];
  });
  $('#srchIn').placeholder = t('ph_search');
  $$('[data-setlang]').forEach(b => {
    const on = b.dataset.setlang === lang;
    b.classList.toggle('is-on', on);
    b.setAttribute('aria-pressed', String(on));
  });
}

/* ---------- progress ---------- */
function nextDay(){
  for (let i = 1; i <= TOTAL_DAYS; i++) if (!done.has(i)) return i;
  return TOTAL_DAYS;
}
function currentRank(){
  const n = done.size;
  const allExtra = exams.size >= 6 && projs.size >= 10;
  let cur = null;
  for (const r of RANKS){
    const ok = n >= r.need && (!r.extra || allExtra);
    if (ok) cur = r;
  }
  return cur;
}
function renderProgress(){
  const n = done.size, pct = Math.round(n / TOTAL_DAYS * 100);
  const C = 2 * Math.PI * 52;

  $('#ringFg').style.strokeDashoffset = String(C - (C * n / TOTAL_DAYS));
  $('#ringPct').textContent = pct + '%';
  $('#ringSub').textContent = `${n} / ${TOTAL_DAYS}`;
  $('#hdrProgBar').style.width = pct + '%';

  const r = currentRank();
  $('#termRank').textContent = r ? `${t('rank_pre')} ${t('r_' + r.key)}` : t('rank_none');

  const nxt = RANKS.find(x => n < x.need);
  $('#termNext').textContent = nxt
    ? `${t('next_to')} ${t('r_' + nxt.key)} — ${nxt.need - n} ${t('days_of')}`
    : t('all_done');

  const cta = $('#ctaLabel'), nd = nextDay();
  cta.textContent = n === 0 ? t('cta_start')
                  : n >= TOTAL_DAYS ? t('cta_done')
                  : `${t('cta_continue')} ${nd}`;

  renderRanks();
  renderChains();
  if (view.name === 'home') renderCards();
  if (view.name === 'month') paintMonthView();
}

/* ---------- ranks ---------- */
function renderRanks(){
  const n = done.size, allExtra = exams.size >= 6 && projs.size >= 10;
  $('#ranks').innerHTML = RANKS.map(r => {
    const on = n >= r.need && (!r.extra || allExtra);
    return `<article class="rank${on ? ' is-on' : ''}" style="--c:${r.color}">
      <div class="rank__medal">${ICONS.medal}</div>
      <p class="rank__n">${t('r_' + r.key)}</p>
      <p class="rank__req">${esc(t('rq_' + r.key))}</p>
      <p class="rank__state">${on ? t('unlocked') : t('locked')}</p>
    </article>`;
  }).join('');
}

/* ---------- roadmap chains ---------- */
function renderChains(){
  const ms = months();
  const build = (list) => list.map(m => {
    const total = m.days.length;
    const cnt = m.days.filter(d => done.has(gDay(m.num, d.num))).length;
    const full = total > 0 && cnt === total;
    return `<li class="${full ? 'is-done' : ''}">
      <span class="chain__n">${String(m.num).padStart(2,'0')}</span>
      <span class="chain__t">${esc(m.title.split('(')[0].trim())}</span>
      <span class="chain__badge">${cnt}/${total}</span>
    </li>`;
  }).join('');
  $('#chain1').innerHTML = build(ms.filter(m => m.num <= 6));
  $('#chain2').innerHTML = build(ms.filter(m => m.num >= 7));
}

/* ---------- month cards ---------- */
function renderCards(){
  $('#monthCards').innerHTML = months().map(m => {
    const total = m.days.length;
    const cnt = m.days.filter(d => done.has(gDay(m.num, d.num))).length;
    const pct = total ? Math.round(cnt / total * 100) : 0;
    return `<button class="card rv${cnt === total && total ? ' is-complete' : ''}" data-month="${m.num}">
      <span class="card__top">
        <span class="card__num">M${String(m.num).padStart(2,'0')}</span>
        <span class="card__phase">${m.num <= 6 ? t('ph1') : t('ph2')}</span>
      </span>
      <span class="card__h">${esc(m.title)}</span>
      <span class="card__goal">${esc(m.goal || '')}</span>
      <span class="card__ft">
        <span class="bar"><span style="width:${pct}%"></span></span>
        <span class="card__cnt">${cnt}/${total}</span>
      </span>
    </button>`;
  }).join('');
  revealAll();
}

/* ---------- month view ---------- */
function openMonth(num){
  view = { name:'month', month:num };
  $('#monthView').hidden = false;
  ['#roadmap','#months','#achievements'].forEach(s => $(s).hidden = true);
  $('.hero').hidden = true;
  paintMonthView();
  window.scrollTo({ top:0, behavior:'auto' });
}
function goHome(){
  view = { name:'home', month:null };
  $('#monthView').hidden = true;
  ['#roadmap','#months','#achievements'].forEach(s => $(s).hidden = false);
  $('.hero').hidden = false;
  renderCards();
}
function paintMonthView(){
  const m = months().find(x => x.num === view.month);
  if (!m) return goHome();
  const total = m.days.length;
  const cnt = m.days.filter(d => done.has(gDay(m.num, d.num))).length;

  $('#mvNum').textContent = 'M' + String(m.num).padStart(2,'0');
  $('#mvTitle').textContent = m.title;
  $('#mvGoal').textContent = m.goal || '';
  $('#mvBar').innerHTML = `<span style="width:${total ? Math.round(cnt/total*100) : 0}%"></span>`;

  const byWeek = new Map();
  m.days.forEach(d => {
    const w = d.week ?? 0;
    if (!byWeek.has(w)) byWeek.set(w, []);
    byWeek.get(w).push(d);
  });

  $('#mvWeeks').innerHTML = [...byWeek.entries()].map(([w, days]) => {
    const wk = m.weeks.find(x => x.num === w);
    return `<section class="wk">
      <h3 class="wk__h">${t('week')} ${w}${wk ? ' — ' + esc(wk.title) : ''}</h3>
      <div class="days">${days.map(d => {
        const g = gDay(m.num, d.num);
        return `<button class="day${done.has(g) ? ' is-done' : ''}" data-day="${g}">
          <span class="day__chk">${done.has(g) ? ICONS.tickOn : d.num}</span>
          <span class="day__t">${esc(d.title)}</span>
        </button>`;
      }).join('')}</div>
    </section>`;
  }).join('');
}

/* ---------- day lookup ---------- */
function findDay(g){
  for (const m of months()){
    const d = m.days.find(x => x.num === g);
    if (d) return { m, d, g };
  }
  return null;
}

/* ---------- drawer ---------- */
function openDay(g){
  const found = findDay(g);
  if (!found) return;
  if ($('#drawer').hidden) lastFocus = document.activeElement;
  drawerDay = g;
  const { m, d } = found;

  $('#dEyebrow').textContent = `M${String(m.num).padStart(2,'0')} · ${t('day')} ${d.num} / ${TOTAL_DAYS}`;
  $('#dTitle').textContent = d.title;

  const blocks = [
    ['theory','theory',''],
    ['practice','practice',''],
    ['task','task','blk--task'],
  ];
  let html = blocks.map(([key, ico, mod]) => {
    if (!d[key]) return '';
    return `<section class="blk ${mod}">
      <h3 class="blk__h">${ICONS[ico]}<span>${t(key)}</span></h3>
      <p class="blk__p">${rich(d[key])}</p>
    </section>`;
  }).join('');

  // День повторения/резерва: теории нет намеренно — объясняем это студенту,
  // иначе выглядит так, будто контент потеряли.
  if (!d.theory && !d.practice){
    html = `<p class="daynote">${t('note_recap')}</p>` + html;
  } else if (!d.theory){
    html = `<p class="daynote">${t('note_no_theory')}</p>` + html;
  }

  // Видео прямо на странице: сначала ролики дня, иначе — плейлисты месяца
  const dayVids = d.videos || [];
  const vids = dayVids.length ? dayVids : (m.videos || []);
  if (vids.length){
    html += `<section class="blk blk--video">
      <h3 class="blk__h">${ICONS.play}
        <span>${dayVids.length ? t('video') : t('video_month')}</span></h3>
      ${dayVids.length ? '' : `<p class="quiz__note">${t('video_month_hint')}</p>`}
      <div class="vids">${vids.map(v => videoCard(v)).join('')}</div>
    </section>`;
  }

  // Материалы: ссылки самого дня, иначе — ресурсы месяца (чтобы студент всегда знал, куда идти)
  const own = d.links && d.links.length ? d.links : [];
  const mats = own.length ? own : (m.resources || []);
  if (mats.length){
    html += `<section class="blk blk--links">
      <h3 class="blk__h">${ICONS.link}
        <span>${own.length ? t('materials') : t('month_materials')}</span></h3>
      ${own.length ? '' : `<p class="quiz__note">${t('month_materials_hint')}</p>`}
      <ul class="mats">${mats.map(l =>
        `<li><a class="${l.search ? 'is-search' : ''}" href="${esc(l.url)}" target="_blank" rel="noopener noreferrer">
           <span class="mats__t">${esc(l.title)}</span>
           <span class="mats__u">${l.search ? esc(t('yt_search')) : esc(hostOf(l.url))}</span>
         </a></li>`).join('')}</ul>
    </section>`;
  }

  // Исходный вопрос дня из курса — раньше пропадал, если для дня есть тест
  if (d.check){
    html += `<section class="blk blk--check">
      <h3 class="blk__h">${ICONS.check}<span>${t('check')}</span></h3>
      <p class="blk__p">${rich(d.check)}</p>
    </section>`;
  }

  // Проверка знаний
  html += renderQuiz(d, g);

  $('#dBody').innerHTML = html;
  paintDoneBtn();
  $('#dPrev').disabled = g <= 1;
  $('#dNext').disabled = g >= TOTAL_DAYS;

  $('#drawer').hidden = false;
  document.body.classList.add('is-locked');
  $('#dDone').focus();
}
function hostOf(url){
  try { return new URL(url).hostname.replace(/^www\./, ''); }
  catch { return url.slice(0, 40); }
}

/* ---------- видео ----------
   Плеер встраивается на страницу (youtube-nocookie). iframe создаётся ТОЛЬКО по клику:
   до этого никаких запросов к Google, страница грузится быстро.
   Копии чужих видео мы не размещаем — это нарушение авторских прав. */
function videoCard(v){
  const id = String(v.yt).replace(/[^\w-]/g, '');   // защита от инъекции в атрибут
  const isPl = v.kind === 'playlist';
  const dur = v.min ? (v.min >= 60 ? `${Math.floor(v.min/60)} ч ${v.min%60 ? v.min%60+' мин' : ''}` : `${v.min} мин`) : '';
  const thumb = isPl ? '' : `https://i.ytimg.com/vi/${id}/hqdefault.jpg`;
  return `<figure class="vid" data-yt="${id}" data-kind="${isPl ? 'playlist' : 'video'}">
    <button class="vid__play" aria-label="${esc(t('play'))}: ${esc(v.t)}">
      ${thumb ? `<img class="vid__thumb" src="${thumb}" alt="" loading="lazy" decoding="async">` : '<span class="vid__thumb vid__thumb--pl"></span>'}
      <span class="vid__btn">${ICONS.playFill}</span>
      ${dur ? `<span class="vid__dur">${esc(dur)}</span>` : ''}
      ${isPl ? `<span class="vid__badge">${esc(t('playlist'))}</span>` : ''}
    </button>
    <figcaption class="vid__cap">
      <span class="vid__t">${esc(v.t)}</span>
      ${v.a ? `<span class="vid__a">${esc(v.a)}</span>` : ''}
    </figcaption>
  </figure>`;
}

function playVideo(fig){
  const id = fig.dataset.yt;
  const isPl = fig.dataset.kind === 'playlist';
  const src = isPl
    ? `https://www.youtube-nocookie.com/embed/videoseries?list=${id}&autoplay=1&rel=0`
    : `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0`;
  const holder = fig.querySelector('.vid__play');
  if (!holder) return;
  holder.outerHTML = `<div class="vid__frame">
    <iframe src="${src}" title="${esc(t('video'))}" loading="lazy"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture"
      referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  </div>`;
}

/* ---------- проверка знаний ---------- */
function renderQuiz(d, g){
  if (!d.quiz) return '';   // тест не написан — остаётся только вопрос курса выше
  const passed = quizOk.has(g);
  return `<section class="blk blk--quiz${passed ? ' is-passed' : ''}" id="quizBox">
    <h3 class="blk__h">${ICONS.check}<span>${t('quiz')}</span>
      ${passed ? `<span class="quiz__badge">${t('passed')}</span>` : ''}</h3>
    <p class="quiz__q">${esc(d.quiz.q)}</p>
    <div class="quiz__opts" role="radiogroup" aria-label="${esc(d.quiz.q)}">
      ${d.quiz.o.map((opt, i) => `
        <button class="qopt" data-qopt="${i}" role="radio" aria-checked="false">
          <span class="qopt__k">${String.fromCharCode(65 + i)}</span>
          <span class="qopt__t">${esc(opt)}</span>
        </button>`).join('')}
    </div>
    <p class="quiz__fb" id="quizFb" role="status" aria-live="polite" hidden></p>
  </section>`;
}

function answerQuiz(idx){
  const f = findDay(drawerDay);
  if (!f || !f.d.quiz) return;
  const correct = f.d.quiz.a;
  const fb = $('#quizFb');
  const opts = $$('.qopt');

  opts.forEach((b, i) => {
    b.classList.toggle('is-right', i === correct);
    b.classList.toggle('is-wrong', i === idx && i !== correct);
    b.setAttribute('aria-checked', String(i === idx));
    b.disabled = true;
  });

  if (idx === correct){
    quizOk.add(drawerDay);
    save(LS.quiz, [...quizOk]);
    fb.className = 'quiz__fb is-ok';
    fb.innerHTML = `<b>${t('right')}</b> ${esc(f.d.quiz.e)}`;
    $('#quizBox').classList.add('is-passed');
  } else {
    fb.className = 'quiz__fb is-bad';
    fb.innerHTML = `<b>${t('wrong')}</b> ${esc(f.d.quiz.e)}
      <button class="quiz__retry" id="quizRetry">${t('retry')}</button>`;
  }
  fb.hidden = false;
  paintDoneBtn();
}

function paintDoneBtn(){
  const b = $('#dDone');
  const f = findDay(drawerDay);
  const needQuiz = !!(f && f.d.quiz);
  const passed = quizOk.has(drawerDay);
  const on = done.has(drawerDay);

  // Гейт: пока тест не сдан, день нельзя отметить пройденным
  const locked = needQuiz && !passed && !on;
  b.disabled = locked;
  b.textContent = locked ? t('locked_day') : (on ? t('undone') : t('done'));
  b.classList.toggle('btn--pri', !on && !locked);
  b.classList.toggle('btn--gho', on || locked);
  b.title = locked ? t('locked_hint') : '';
}
function closeDrawer(){
  if ($('#drawer').hidden) return;
  $('#drawer').hidden = true;
  document.body.classList.remove('is-locked');
  drawerDay = null;
  // вернуть фокус туда, откуда открыли — иначе он теряется в начале страницы
  if (lastFocus && document.contains(lastFocus)) lastFocus.focus();
  lastFocus = null;
}
function toggleDay(g){
  done.has(g) ? done.delete(g) : done.add(g);
  save(LS.days, [...done]);
  renderProgress();
}

/* ---------- checklists ---------- */
function renderTicks(){
  const mk = (arr, set, kind) => arr.map((label, i) =>
    `<li><button class="tick${set.has(i) ? ' is-on' : ''}" data-tick="${kind}" data-i="${i}" aria-pressed="${set.has(i)}">
      <span class="tick__box">${ICONS.tickOn}</span>
      <span class="tick__t">${esc(label)}</span>
    </button></li>`).join('');

  $('#examList').innerHTML = mk(EXAMS[lang] || EXAMS.ru, exams, 'exam');
  $('#projList').innerHTML = mk(PROJECTS[lang] || PROJECTS.ru, projs, 'proj');
  $('#examCount').textContent = `${exams.size}/6`;
  $('#projCount').textContent = `${projs.size}/10`;
}

/* ---------- search ---------- */
let srchSel = 0, srchHits = [];
function openSearch(){
  $('#srch').hidden = false;
  document.body.classList.add('is-locked');
  $('#srchIn').value = '';
  runSearch('');
  $('#srchIn').focus();
}
function closeSearch(){
  $('#srch').hidden = true;
  document.body.classList.remove('is-locked');
}
function runSearch(q){
  const query = q.trim().toLowerCase();
  const box = $('#srchRes');
  srchSel = 0;

  if (!query){
    // подсказка: следующие 6 дней от текущего
    const start = nextDay();
    srchHits = [];
    for (let g = start; g < start + 6 && g <= TOTAL_DAYS; g++){
      const f = findDay(g); if (f) srchHits.push({ ...f, score:0 });
    }
  } else {
    const hits = [];
    for (const m of months()){
      for (const d of m.days){
        const qz = d.quiz ? `${d.quiz.q} ${d.quiz.e}` : '';
        const hay = `${d.title} ${d.theory} ${d.practice} ${d.task} ${d.check} ${qz}`.toLowerCase();
        const inTitle = d.title.toLowerCase().includes(query);
        if (inTitle || hay.includes(query)){
          hits.push({ m, d, g:gDay(m.num, d.num), score: inTitle ? 2 : 1 });
        }
      }
    }
    hits.sort((a,b) => b.score - a.score || a.g - b.g);
    srchHits = hits.slice(0, 40);
  }

  if (!srchHits.length){
    box.innerHTML = `<p class="srch__empty">${t('no_res')}</p>`;
    return;
  }

  const hi = (text) => {
    const s = esc(text);
    if (!query) return s;
    const i = s.toLowerCase().indexOf(query);
    if (i < 0) return s;
    return s.slice(0,i) + '<mark>' + s.slice(i, i+query.length) + '</mark>' + s.slice(i+query.length);
  };

  box.innerHTML = srchHits.map((h, idx) => `
    <button class="sres${idx === 0 ? ' is-sel' : ''}" data-day="${h.g}" role="option">
      <span class="sres__n">${String(h.g).padStart(3,'0')}</span>
      <span>
        <span class="sres__t">${hi(h.d.title)}</span>
        <span class="sres__m">M${String(h.m.num).padStart(2,'0')} · ${esc(h.m.title.split('—')[0].trim())}</span>
      </span>
    </button>`).join('');
}
function moveSel(dir){
  const items = $$('.sres');
  if (!items.length) return;
  items[srchSel]?.classList.remove('is-sel');
  srchSel = (srchSel + dir + items.length) % items.length;
  const el = items[srchSel];
  el.classList.add('is-sel');
  el.scrollIntoView({ block:'nearest' });
}

/* ---------- reveal on scroll ---------- */
let io;
function revealAll(){
  if (!('IntersectionObserver' in window)){
    $$('.rv').forEach(el => el.classList.add('is-in'));
    return;
  }
  io ||= new IntersectionObserver((entries) => {
    entries.forEach((e, i) => {
      if (e.isIntersecting){
        setTimeout(() => e.target.classList.add('is-in'), Math.min(i * 40, 200));
        io.unobserve(e.target);
      }
    });
  }, { rootMargin:'0px 0px -40px 0px' });
  $$('.rv:not(.is-in)').forEach(el => io.observe(el));
}

/* ---------- events ---------- */
document.addEventListener('click', (e) => {
  const langBtn = e.target.closest('[data-setlang]');
  if (langBtn){
    const next = langBtn.dataset.setlang;
    if (next === lang) return;
    langBtn.disabled = true;
    loadLangData(next).then(() => {
      lang = next;
      save(LS.lang, lang);
      renderAll();
      if (drawerDay) openDay(drawerDay);
    }).finally(() => { langBtn.disabled = false; });
    return;
  }

  const nav = e.target.closest('[data-nav]');
  if (nav){
    e.preventDefault();
    if (nav.dataset.nav === 'home') goHome();
    if (nav.dataset.nav === 'continue') openDay(nextDay());
    return;
  }

  const card = e.target.closest('[data-month]');
  if (card){ openMonth(+card.dataset.month); return; }

  const dayBtn = e.target.closest('[data-day]');
  if (dayBtn){
    if (dayBtn.classList.contains('sres')) closeSearch();
    openDay(+dayBtn.dataset.day);
    return;
  }

  const tick = e.target.closest('[data-tick]');
  if (tick){
    const isExam = tick.dataset.tick === 'exam';
    const i = +tick.dataset.i;
    const set = isExam ? exams : projs;
    set.has(i) ? set.delete(i) : set.add(i);
    save(isExam ? LS.exams : LS.projects, [...set]);
    // точечно, без перерисовки списка — иначе теряется фокус клавиатуры
    tick.classList.toggle('is-on', set.has(i));
    tick.setAttribute('aria-pressed', String(set.has(i)));
    $('#examCount').textContent = `${exams.size}/6`;
    $('#projCount').textContent = `${projs.size}/10`;
    renderProgress();
    return;
  }

  const vid = e.target.closest('.vid__play');
  if (vid){ playVideo(vid.closest('.vid')); return; }

  const qopt = e.target.closest('[data-qopt]');
  if (qopt && !qopt.disabled){ answerQuiz(+qopt.dataset.qopt); return; }

  if (e.target.closest('#quizRetry')){
    const f = findDay(drawerDay);
    if (f){
      const box = $('#quizBox');
      if (box) box.outerHTML = renderQuiz(f.d, drawerDay);
    }
    return;
  }

  if (e.target.closest('#resetBtn')){
    if (confirm(t('reset_confirm'))){
      done.clear(); exams.clear(); projs.clear(); quizOk.clear();
      [LS.days, LS.exams, LS.projects, LS.quiz].forEach(k => save(k, []));
      renderTicks(); renderProgress();
    }
    return;
  }

  if (e.target.closest('[data-close]')){ closeDrawer(); closeSearch(); return; }
  if (e.target.closest('#searchBtn')){ openSearch(); return; }
});

$('#dDone').addEventListener('click', () => { toggleDay(drawerDay); paintDoneBtn(); });
$('#dPrev').addEventListener('click', () => { if (drawerDay > 1) openDay(drawerDay - 1); });
$('#dNext').addEventListener('click', () => { if (drawerDay < TOTAL_DAYS) openDay(drawerDay + 1); });

$('#srchIn').addEventListener('input', (e) => runSearch(e.target.value));
$('#srchIn').addEventListener('keydown', (e) => {
  if (e.key === 'ArrowDown'){ e.preventDefault(); moveSel(1); }
  else if (e.key === 'ArrowUp'){ e.preventDefault(); moveSel(-1); }
  else if (e.key === 'Enter'){
    const h = srchHits[srchSel];
    if (h){ closeSearch(); openDay(h.g); }
  }
});

/* Фокус не должен уходить за пределы открытой модалки — иначе пользователь
   клавиатуры «проваливается» на фон и теряет контекст (WCAG 2.4.3). */
function trapFocus(e){
  const modal = !$('#drawer').hidden ? $('.drawer__pnl')
              : (!$('#srch').hidden ? $('.srch__box') : null);
  if (!modal || e.key !== 'Tab') return;
  const items = [...modal.querySelectorAll(
    'a[href], button:not([disabled]), input, select, textarea, [tabindex]:not([tabindex="-1"])'
  )].filter(el => el.offsetParent !== null);
  if (!items.length) return;
  const first = items[0], last = items[items.length - 1];
  if (e.shiftKey && document.activeElement === first){ e.preventDefault(); last.focus(); }
  else if (!e.shiftKey && document.activeElement === last){ e.preventDefault(); first.focus(); }
  else if (!modal.contains(document.activeElement)){ e.preventDefault(); first.focus(); }
}

document.addEventListener('keydown', (e) => {
  const typing = /^(INPUT|TEXTAREA)$/.test(e.target.tagName);
  trapFocus(e);
  if (e.key === 'Escape'){ closeDrawer(); closeSearch(); return; }
  if (!typing && (e.key === '/' || ((e.metaKey || e.ctrlKey) && e.key === 'k'))){
    e.preventDefault(); openSearch(); return;
  }
  if (!$('#drawer').hidden && !typing){
    if (e.key === 'ArrowLeft' && drawerDay > 1) openDay(drawerDay - 1);
    if (e.key === 'ArrowRight' && drawerDay < TOTAL_DAYS) openDay(drawerDay + 1);
  }
});

/* ---------- загрузка данных языка ---------- */
const loadedLangs = new Set();
function loadLangData(code){
  if (loadedLangs.has(code) || (DATA[code] && DATA[code].length)){
    loadedLangs.add(code);
    return Promise.resolve();
  }
  return new Promise((resolve, reject) => {
    const s = document.createElement('script');
    s.src = `data-${code}.js`;
    s.onload = () => { loadedLangs.add(code); resolve(); };
    s.onerror = () => reject(new Error(`data-${code}.js не загрузился`));
    document.head.appendChild(s);
  });
}

/* ---------- init ---------- */
function renderAll(){
  applyI18n();
  renderTicks();
  renderProgress();
  if (view.name === 'month') paintMonthView(); else renderCards();
  revealAll();
}

function init(){
  const langs = window.COURSE_LANGS || ['ru'];
  if (!langs.includes(lang)) lang = langs[0];
  loadLangData(lang).then(renderAll).catch(err => {
    $('#monthCards').innerHTML =
      '<p class="srch__empty">Данные не загрузились. Запусти: python site/build-data.py</p>';
    console.error(err);
  });
}
init();

})();
