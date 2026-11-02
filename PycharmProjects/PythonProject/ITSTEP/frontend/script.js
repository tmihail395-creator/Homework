const $ = (s, r = document) => r.querySelector(s);
const page = document.body.dataset.page;
const wait = ms => new Promise(r => setTimeout(r, ms));
const esc = s => String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const rnd = a => a[Math.floor(Math.random() * a.length)];

// localStorage с защитой от ошибок
const store = {
  get: k => { try { return localStorage.getItem(k); } catch (e) { return null; } },
  set: (k, v) => { try { localStorage.setItem(k, v); } catch (e) {} }
};

// Печать текста по буквам. **текст** = красный жирный
async function type(el, text, d = 14) {
  let bold = false;
  for (const part of text.split("**")) {
    const span = document.createElement(bold ? "b" : "span");
    el.appendChild(span);
    for (const ch of part) { span.textContent += ch; await wait(d); }
    bold = !bold;
  }
}

/* ---------- Меню и подвал ---------- */
const links = [
  ["home", "index.html", "Главная"],
  ["search", "search.html", "Поиск людей"],
  ["shop", "shop.html", "Доступ"],
  ["watch", "watch.html", "Наблюдение"],
  ["register", "register.html", "Регистрация"]
];
$("#nav").innerHTML = `<nav class="nav">
  <a class="brand" href="index.html"><img src="images%20(1).png" alt=""><b>VOID<i>//</i>NET</b></a>
  <div class="links">${links.map(l =>
    `<a href="${l[1]}" class="${l[0] === page ? "on" : ""} ${l[0] === "register" ? "cta" : ""}">${l[2]}</a>`).join("")}</div>
</nav>`;
$("#foot").innerHTML = `<footer class="foot">Вымышленный учебный проект. Все люди, данные и платежи выдуманы. Ничего никуда не отправляется.</footer>`;

/* ---------- Главная ---------- */
function initHome() {
  document.querySelectorAll("[data-n]").forEach(async el => {
    const end = +el.dataset.n;
    for (let i = 1; i <= 40; i++) { el.textContent = Math.round(end * i / 40).toLocaleString("ru"); await wait(25); }
  });
  const msgs = [
    () => `ghost_${Math.floor(Math.random() * 90 + 10)} вошёл в сеть`,
    () => "добавлено новое досье",
    () => "запрос на поиск: ожидает проверки",
    () => `пользователь ${rnd(["moth","raven","null","echo"])}_${Math.floor(Math.random() * 99)} купил доступ`,
    () => "кто-то смотрит на тебя прямо сейчас",
    () => "резервная копия базы завершена"
  ];
  const ul = $("#ticker");
  const push = () => {
    const li = document.createElement("li");
    const t = new Date().toLocaleTimeString("ru");
    li.textContent = `[${t}] ${rnd(msgs)()}`;
    ul.prepend(li);
    while (ul.children.length > 7) ul.lastChild.remove();
  };
  push(); setInterval(push, 2200);
}

/* ---------- Поиск (выдуманные люди) ---------- */
const DB = [
  {n:"Ирма Вальтер",  a:"Стекло",  c:"Нокс-Харбор", age:34, job:"Архивист",       last:"вчера, 03:12",      note:"Не отвечает на звонки после полуночи."},
  {n:"Кассиан Морн",  a:"Тень",    c:"Серый Мыс",   age:41, job:"Часовой мастер", last:"3 дня назад",       note:"Хранит ключи от закрытой станции."},
  {n:"Дарина Холод",  a:"Иней",    c:"Нокс-Харбор", age:28, job:"Фотограф",       last:"сегодня, 06:40",    note:"На каждом снимке есть лишний силуэт."},
  {n:"Леон Тихий",    a:"Шёпот",   c:"Чёрный Брод", age:52, job:"Библиотекарь",   last:"неделю назад",      note:"Никто не помнит, как он выглядит."},
  {n:"Мара Вексель",  a:"Ворон",   c:"Серый Мыс",   age:37, job:"Нотариус",       last:"2 часа назад",      note:"Подписывает бумаги чужими именами."},
  {n:"Ян Сумрак",     a:"Эхо",     c:"Чёрный Брод", age:30, job:"Радиотехник",    last:"только что",        note:"Слушает частоты, которых не существует."}
];

function personCard(p) {
  const plan = store.get("plan");
  const L = v => plan ? esc(v) : `<span class="blur">${esc(v)}</span>`;
  return `<article class="card">
    <h3>${esc(p.n)} <small>«${esc(p.a)}»</small></h3>
    <p>Город: ${esc(p.c)} · Возраст: ${p.age}</p>
    <p>Место работы: ${L(p.job)}</p>
    <p>Последний сигнал: ${L(p.last)}</p>
    <p>Заметка: ${L(p.note)}</p>
    ${plan ? `<span class="tagr">доступ: ${esc(plan)}</span>` : `<a class="btn sm" href="shop.html">Открыть досье</a>`}
  </article>`;
}

function initSearch() {
  $("#sform").addEventListener("submit", e => {
    e.preventDefault();
    const q = $("#q").value.trim().toLowerCase();
    const res = $("#res");
    if (!q) { res.innerHTML = ""; return; }
    const found = DB.filter(p => (p.n + " " + p.a).toLowerCase().includes(q));
    res.innerHTML = found.length
      ? found.map(personCard).join("")
      : `<div class="card"><h3>Совпадений нет</h3><p class="muted">«${esc(q)}» в базе нет. Пока.</p></div>`;
  });
}

/* ---------- Магазин доступа (игровая валюта) ---------- */
const PLANS = [
  {name:"Наблюдатель", price:50,  items:["Поиск по базе","Базовые данные","Поддержка в чате"]},
  {name:"Тень",        price:150, items:["Полные досье","История сигналов","Приоритетный поиск"], hot:true},
  {name:"Пустота",     price:400, items:["Всё из «Тени»","Закрытые разделы","Доступ без ограничений"]}
];

function buy(p) {
  const m = document.createElement("div");
  m.className = "modal";
  m.innerHTML = `<div class="box narrow"><pre class="log" id="mlog"></pre><button class="btn" id="mclose" hidden>Закрыть</button></div>`;
  document.body.appendChild(m);
  const log = $("#mlog", m), close = $("#mclose", m);
  close.onclick = () => { m.remove(); location.reload(); };
  (async () => {
    await type(log, `> тариф: ${p.name}\n> стоимость: ${p.price} VC (игровая валюта)\n> реальные деньги не списываются... `);
    await wait(500);
    await type(log, "**OK**\n> выдача ключа... "); await wait(600);
    await type(log, `**OK**\n\nДОСТУП ОТКРЫТ: **${p.name}**\nЭто учебная демонстрация.\n`);
    store.set("plan", p.name);
    close.hidden = false;
  })();
}

function initShop() {
  const cur = store.get("plan");
  if (cur) $("#plan").textContent = "Ваш текущий доступ: " + cur;
  $("#plans").innerHTML = PLANS.map((p, i) => `<div class="card ${p.hot ? "hot" : ""}">
    <h3>${p.name}</h3><div class="price">${p.price} VC</div>
    <ul>${p.items.map(x => `<li>${x}</li>`).join("")}</ul>
    <button class="btn full" data-i="${i}">Купить доступ</button></div>`).join("");
  $("#plans").addEventListener("click", e => {
    const b = e.target.closest("[data-i]");
    if (b) buy(PLANS[b.dataset.i]);
  });
}

/* ---------- Наблюдение ---------- */
function initWatch() {
  const info = [
    ["Браузер", navigator.userAgent.split(") ").pop() || navigator.userAgent],
    ["Система", navigator.platform || "?"],
    ["Язык", navigator.language],
    ["Экран", screen.width + "×" + screen.height],
    ["Часовой пояс", Intl.DateTimeFormat().resolvedOptions().timeZone],
    ["Ядер процессора", navigator.hardwareConcurrency || "?"]
  ];
  $("#fp").innerHTML = info.map(r => `<tr><td>${r[0]}</td><td>${esc(r[1])}</td></tr>`).join("");

  const lines = ["Мы давно ждали тебя.", "Не оборачивайся.", "Ты уже был здесь раньше.",
                 "Твой экран светится в темноте.", "Мы знаем, который час у тебя.", "Не закрывай вкладку."];
  const w = $("#whisper");
  let i = 0;
  const say = () => { w.textContent = lines[i++ % lines.length]; };
  say(); setInterval(say, 3500);

  let left = 300, t = 0;
  setInterval(() => {
    left = left > 0 ? left - 1 : 300; t++;
    $("#timer").textContent = String(Math.floor(left / 60)).padStart(2, "0") + ":" + String(left % 60).padStart(2, "0");
    $("#since").textContent = t;
  }, 1000);
}

/* ---------- Регистрация ---------- */
function initRegister() {
  const form = $("#form"), log = $("#log");

  $("#code").addEventListener("input", e => {
    const raw = e.target.value.toUpperCase().replace(/[^A-Z0-9]/g, "").slice(0, 12);
    e.target.value = raw.match(/.{1,4}/g)?.join("-") ?? "";
  });
  $("#phone").addEventListener("input", e => {
    const d = e.target.value.replace(/\D/g, "").slice(0, 12);
    e.target.value = d ? "+" + d.replace(/(\d{3})(\d{2})(\d{3})(\d{2})(\d{0,2})/,
      (m, a, b, c, d2, e2) => [a, b, c, d2, e2].filter(Boolean).join(" ")) : "";
  });

  const rules = {
    code:  v => /^[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$/.test(v) || "Формат кода: XXXX-XXXX-XXXX",
    email: v => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)         || "Введите корректную почту",
    phone: v => v.replace(/\D/g, "").length >= 10               || "Введите номер телефона полностью",
    nick:  v => /^[A-Za-z0-9_]{3,16}$/.test(v)                  || "3–16 символов: латиница, цифры, _"
  };
  const validate = () => {
    let ok = true;
    for (const k in rules) {
      const el = $("#" + k), res = rules[k](el.value.trim());
      $("#e-" + k).textContent = res === true ? "" : res;
      el.classList.toggle("bad", res !== true);
      if (res !== true) ok = false;
    }
    return ok;
  };

  form.addEventListener("submit", async e => {
    e.preventDefault();
    if (!validate()) return;
    const btn = form.querySelector(".btn");
    btn.disabled = true; log.hidden = false; log.innerHTML = "";
    const nick = $("#nick").value.trim();
    const id = "VN-" + Math.random().toString(16).slice(2, 8).toUpperCase();

    await type(log, "> проверка авторского кода... "); await wait(500);
    await type(log, "**OK**\n> шифрование канала... "); await wait(500);
    await type(log, "**OK**\n> создание профиля: " + nick + "\n"); await wait(400);
    await type(log, "\n**ЗАПРОС ПРИНЯТ.**\nID: " + id + "\nСтатус: ожидает подтверждения\n");

    store.set("nick", nick);   // только в твоём браузере
    btn.disabled = false; form.reset();
  });
}

/* ---------- Запуск нужной страницы ---------- */
({home: initHome, search: initSearch, shop: initShop, watch: initWatch, register: initRegister})[page]?.();