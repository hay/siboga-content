"use strict";

const COMMONS_API = "https://commons.wikimedia.org/w/api.php";
const state = {
  photos: [],          // rijen uit siboga_fotos_stations_koppeling.csv
  stations: {},        // stationnummer -> stationgegevens
  decisions: {},       // bestand -> {status, stations, opmerking, tijd}
  view: [],            // gefilterde lijst (indexen in photos)
  current: null,       // index in photos
  draft: new Map(),    // bestand -> {selected:Set, extra:[]} voor nog niet opgeslagen keuzes
  meta: new Map(),     // bestand -> Promise<{thumb, desc}>
};

const $ = (sel, root = document) => root.querySelector(sel);
const splitList = (s) => (s || "").split(";").map((x) => x.trim()).filter(Boolean);

async function fetchData(tries = 5) {
  // de eerste aanvraag kan haperen als de server net start; dan opnieuw proberen
  for (let i = 1; ; i++) {
    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), 8000);
    try {
      const res = await fetch("/api/data", { signal: ctrl.signal, cache: "no-store" });
      if (res.ok) return await res.json();
      throw new Error(`HTTP ${res.status}`);
    } catch (err) {
      if (i >= tries) throw err;
      await new Promise((r) => setTimeout(r, 1000));
    } finally {
      clearTimeout(timer);
    }
  }
}

async function init() {
  const data = await fetchData();
  state.photos = data.photos;
  state.stations = data.stations;
  state.decisions = data.decisions || {};
  // na een filterkeuze de focus loslaten, zodat de sneltoetsen meteen weer werken
  for (const id of ["f-status", "f-zekerheid"]) $("#" + id).addEventListener("change", (e) => { e.target.blur(); applyFilter(true); });
  $("#f-zoek").addEventListener("input", () => applyFilter(true));
  document.addEventListener("keydown", onKey);
  $("#help-open").addEventListener("click", (e) => { e.currentTarget.blur(); $("#help").showModal(); });
  applyFilter(true);
}

function candidates(p) {
  const d = draftFor(p);
  return [...splitList(p.stations), ...d.extra];
}

function draftFor(p) {
  if (!state.draft.has(p.bestand)) {
    const dec = state.decisions[p.bestand];
    const cand = splitList(p.stations);
    const saved = dec ? dec.stations : (cand.length === 1 ? cand : []);
    state.draft.set(p.bestand, { selected: new Set(saved), extra: saved.filter((s) => !cand.includes(s)) });
  }
  return state.draft.get(p.bestand);
}

function statusOf(p) { return state.decisions[p.bestand]?.status || "open"; }

function applyFilter(keepCurrent) {
  const fs = $("#f-status").value, fz = $("#f-zekerheid").value, q = $("#f-zoek").value.trim().toLowerCase();
  state.view = state.photos.map((p, i) => i).filter((i) => {
    const p = state.photos[i], n = splitList(p.stations).length, st = statusOf(p);
    if (fs !== "alle" && st !== fs) return false;
    if (fz === "1" && n !== 1) return false;
    if (fz === "meer" && n < 2) return false;
    if (fz === "geen" && n !== 0) return false;
    if (q && !(p.onderwerp + " " + p.plaatsterm + " " + p.station_remarks).toLowerCase().includes(q)) return false;
    return true;
  });
  if (!keepCurrent || !state.view.includes(state.current)) state.current = state.view[0] ?? null;
  renderList();
  renderDetail();
  renderProgress();
}

function renderProgress() {
  const total = state.photos.length;
  const ok = Object.values(state.decisions).filter((d) => d.status === "goedgekeurd").length;
  const no = Object.values(state.decisions).filter((d) => d.status === "afgewezen").length;
  $("#progress").textContent = `${ok + no} van ${total} beoordeeld · ${ok} goedgekeurd · ${no} afgewezen`;
}

function renderList() {
  const ol = $("#list");
  ol.innerHTML = "";
  $("#list-count").textContent = `${state.view.length} foto's in deze selectie`;
  for (const i of state.view) {
    const p = state.photos[i];
    const li = document.createElement("li");
    li.className = statusOf(p) + (i === state.current ? " active" : "");
    li.dataset.i = i;
    const n = splitList(p.stations).length;
    li.innerHTML = `<span class="t"></span><span class="s"></span>`;
    li.querySelector(".t").textContent = p.onderwerp;
    li.querySelector(".s").textContent = n ? `${n === 1 ? "station" : "stations"} ${p.stations}` : "geen kandidaat";
    li.addEventListener("click", () => select(i));
    ol.appendChild(li);
  }
  $("#list li.active")?.scrollIntoView({ block: "nearest" });
}

function select(i) {
  state.current = i;
  for (const li of document.querySelectorAll("#list li")) li.classList.toggle("active", +li.dataset.i === i);
  $("#list li.active")?.scrollIntoView({ block: "nearest" });
  renderDetail();
}

function move(step) {
  const pos = state.view.indexOf(state.current);
  const next = state.view[Math.min(state.view.length - 1, Math.max(0, pos + step))];
  if (next !== undefined) select(next);
}

function commonsMeta(title) {
  if (!state.meta.has(title)) {
    const url = `${COMMONS_API}?action=query&format=json&formatversion=2&origin=*&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=1200&titles=${encodeURIComponent(title)}`;
    state.meta.set(title, fetch(url).then((r) => r.json()).then((j) => {
      const ii = j.query.pages[0].imageinfo?.[0] || {};
      const html = ii.extmetadata?.ImageDescription?.value || "";
      const text = new DOMParser().parseFromString(html, "text/html").body.textContent
        .replace(/Academische Collecties:\s*\S+/g, "")
        .replace(/1899-1900, Siboga-expeditie naar Nederlands Oost-Indië, onder leiding van Max Wilhelm Carl Weber/g, "")
        .trim();
      return { thumb: ii.thumburl || ii.url, desc: text };
    }).catch(() => ({ thumb: null, desc: "" })));
  }
  return state.meta.get(title);
}

function stationLine(num, idx, d, isManual) {
  const s = state.stations[num];
  const li = document.createElement("li");
  li.classList.toggle("checked", d.selected.has(num));
  const label = document.createElement("label");
  const cb = document.createElement("input");
  cb.type = "checkbox";
  cb.checked = d.selected.has(num);
  cb.addEventListener("change", () => { toggleStation(num); });
  const body = document.createElement("span");
  if (!s) {
    body.innerHTML = `<span class="num">Station ${num}</span> <span class="sub">onbekend stationnummer</span>`;
  } else {
    const q = s.wikidata_uri.split("/").pop();
    const dates = s.end_date ? `${s.start_date} – ${s.end_date}` : s.start_date;
    const map = s.latitude ? ` · <a href="https://www.openstreetmap.org/?mlat=${s.latitude}&mlon=${s.longitude}#map=9/${s.latitude}/${s.longitude}" target="_blank" rel="noopener">kaart</a>` : "";
    body.innerHTML = `<span class="num">Station ${num}</span> ${idx < 9 ? `<span class="key">[${idx + 1}]</span>` : ""} ${isManual ? '<span class="manual">handmatig toegevoegd</span>' : ""}
      <span class="rem"></span>
      <span class="sub">${dates} · <a href="https://www.wikidata.org/wiki/${q}" target="_blank" rel="noopener">${q}</a>${map}</span>`;
    body.querySelector(".rem").textContent = s.remarks || "(geen omschrijving)";
  }
  label.append(cb, body);
  li.appendChild(label);
  return li;
}

function renderDetail() {
  const box = $("#detail");
  if (state.current === null) { box.innerHTML = `<p class="empty">Geen foto's in deze selectie.</p>`; return; }
  const p = state.photos[state.current];
  const d = draftFor(p);
  box.innerHTML = "";
  box.appendChild($("#tpl-detail").content.cloneNode(true));

  const st = statusOf(p), dec = state.decisions[p.bestand];
  const badge = $(".status-badge", box);
  badge.className = "status-badge " + st;
  badge.textContent = st === "open" ? "nog niet beoordeeld" : `${st} (${dec.tijd.replace("T", " ")})`;
  $(".subject", box).textContent = p.onderwerp;
  $(".meta", box).textContent = [
    p.koppeling_via && `gekoppeld via ${p.koppeling_via}: ${p.plaatsterm}`,
    p.foto_datum_commons && `datum op Commons: ${p.foto_datum_commons.replace(/\{\{other date\|between\|(.*?)\|(.*?)\}\}/, "tussen $1 en $2")}`,
  ].filter(Boolean).join(" · ");
  $(".img-link", box).href = p.commons_url;
  $(".note", box).value = dec?.opmerking || "";

  const img = $("img", box), imgStatus = $(".img-status", box);
  imgStatus.textContent = "Afbeelding laden…";
  const forIdx = state.current;
  commonsMeta(p.bestand).then((m) => {
    if (state.current !== forIdx) return;
    if (m.thumb) { img.src = m.thumb; img.alt = p.onderwerp; imgStatus.textContent = "Klik op de foto om hem op Commons te openen."; }
    else imgStatus.textContent = "Afbeelding kon niet geladen worden.";
    $(".desc", box).textContent = m.desc;
  });
  // volgende foto alvast ophalen
  const nxt = state.view[state.view.indexOf(state.current) + 1];
  if (nxt !== undefined) commonsMeta(state.photos[nxt].bestand).then((m) => { if (m.thumb) new Image().src = m.thumb; });

  const ul = $(".stations", box);
  const cand = splitList(p.stations);
  const all = candidates(p);
  if (!all.length) ul.innerHTML = `<li>Geen kandidaat gevonden. Voeg hieronder zelf een station toe, of wijs af.</li>`;
  all.forEach((num, idx) => ul.appendChild(stationLine(num, idx, d, !cand.includes(num))));

  $(".add-station", box).addEventListener("submit", (e) => {
    e.preventDefault();
    const input = $("input", e.target), num = input.value.trim().toLowerCase();
    if (!num) return;
    if (!state.stations[num]) return showMsg(`Station ${num} bestaat niet in de stationslijst.`, true);
    if (!all.includes(num)) d.extra.push(num);
    d.selected.add(num);
    renderDetail();
  });
  for (const b of box.querySelectorAll("[data-act]")) b.addEventListener("click", () => decide(b.dataset.act));
  for (const b of box.querySelectorAll("[data-nav]")) b.addEventListener("click", () => move(+b.dataset.nav));
}

function toggleStation(num) {
  const p = state.photos[state.current], d = draftFor(p);
  d.selected.has(num) ? d.selected.delete(num) : d.selected.add(num);
  const note = $(".note")?.value;
  renderDetail();
  if (note !== undefined) $(".note").value = note;
}

function showMsg(text, isErr) {
  const m = $(".msg");
  if (!m) return;
  m.textContent = text;
  m.classList.toggle("err", !!isErr);
}

async function decide(act) {
  const p = state.photos[state.current], d = draftFor(p);
  const status = act === "wis" ? null : act;
  const stations = candidates(p).filter((s) => d.selected.has(s));
  if (status === "goedgekeurd" && !stations.length) return showMsg("Kies eerst minstens één station om goed te keuren.", true);
  const body = { bestand: p.bestand, status, stations: status === "afgewezen" ? [] : stations, opmerking: $(".note")?.value || "" };
  const res = await fetch("/api/decision", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
  const j = await res.json();
  if (!res.ok) return showMsg(j.error || "Opslaan mislukt.", true);
  if (status === null) { delete state.decisions[p.bestand]; state.draft.delete(p.bestand); }
  else state.decisions[p.bestand] = j.decision;
  renderProgress();
  // in de filter "nog te beoordelen" verdwijnt de foto; ga dan naar de volgende
  const pos = state.view.indexOf(state.current);
  const leaving = status !== null && $("#f-status").value === "open";
  if (leaving) {
    state.view.splice(pos, 1);
    state.current = state.view[Math.min(pos, state.view.length - 1)] ?? null;
    renderList(); renderDetail();
  } else {
    renderList(); renderDetail();
    showMsg(status ? `Opgeslagen als ${status}.` : "Beslissing gewist.");
    if (status) move(1);
  }
}

function onKey(e) {
  if (e.target.closest("input, textarea, select") || e.ctrlKey || e.metaKey || e.altKey) return;
  if ($("#help").open) return;
  if (e.key === "?" || e.key === "/") { $("#help").showModal(); e.preventDefault(); return; }
  if (state.current === null) return;
  const k = e.key.toLowerCase();
  if (k === "arrowright" || k === "j") { move(1); e.preventDefault(); }
  else if (k === "arrowleft" || k === "k") { move(-1); e.preventDefault(); }
  else if (k === "g") decide("goedgekeurd");
  else if (k === "a") decide("afgewezen");
  else if (k === "u") decide("wis");
  else if (/^[1-9]$/.test(k)) {
    const num = candidates(state.photos[state.current])[+k - 1];
    if (num) toggleStation(num);
  }
}

init().catch((err) => { $("#detail").innerHTML = `<p class="empty">Kon de gegevens niet laden: ${err}</p>`; });
