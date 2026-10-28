/* Lead capture shared by all landing page variants.
 *
 * Markup contract:
 *   <form data-lead-form data-placement="hero">
 *     <input type="email" name="email" required>
 *     <input type="text" name="website" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
 *     <button type="submit">…</button>
 *     <p data-lead-msg></p>
 *   </form>
 *   [data-open-sheet]   opens the bottom-sheet form (#lead-sheet)
 *   [data-sticky-cta]   bar shown once no other form is on screen
 *
 * Config (set before this script, all optional):
 *   window.LEAD_CONFIG = { endpoint: "https://…/lead", thankYou: "../dekujeme/", variant: "A" }
 * Without an endpoint the form runs in demo mode (no data leaves the browser).
 */
(function () {
  "use strict";
  var cfg = Object.assign({ endpoint: "", thankYou: "../dekujeme/", variant: "?" }, window.LEAD_CONFIG || {});
  var context = {};

  // Common Czech/global mailbox domains; used only to catch typos like "seznam.cs" or "gmial.com".
  var DOMAINS = ["seznam.cz", "email.cz", "post.cz", "gmail.com", "centrum.cz", "volny.cz", "atlas.cz",
    "outlook.com", "hotmail.com", "icloud.com", "yahoo.com", "tiscali.cz", "quick.cz", "proton.me", "protonmail.com", "outlook.cz"];

  function lev(a, b) {
    var m = a.length, n = b.length, d = [], i, j;
    for (i = 0; i <= m; i++) d[i] = [i];
    for (j = 0; j <= n; j++) d[0][j] = j;
    for (i = 1; i <= m; i++) for (j = 1; j <= n; j++)
      d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
    return d[m][n];
  }

  function suggest(email) {
    var at = email.lastIndexOf("@");
    if (at < 1) return null;
    var dom = email.slice(at + 1).toLowerCase();
    if (DOMAINS.indexOf(dom) > -1) return null;
    var best = null, bestD = 3;
    DOMAINS.forEach(function (c) { var dd = lev(dom, c); if (dd < bestD) { bestD = dd; best = c; } });
    return best ? email.slice(0, at + 1) + best : null;
  }

  function valid(email) { return /^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(email); }

  function utm() {
    var out = {}, q = new URLSearchParams(location.search);
    ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", "fbclid", "gclid", "ad"].forEach(function (k) {
      if (q.get(k)) out[k] = q.get(k).slice(0, 200);
    });
    return out;
  }

  function mask(email) {
    var at = email.indexOf("@");
    return email.charAt(0) + "•••" + email.slice(at);
  }

  function store(key, val) { try { sessionStorage.setItem(key, JSON.stringify(val)); } catch (e) { /* private mode */ } }

  function track(name, params) {
    if (window.Track) window.Track(name, params || {});
  }

  function send(payload) {
    if (!cfg.endpoint) return new Promise(function (r) { setTimeout(function () { r({ ok: true, demo: true }); }, 450); });
    return fetch(cfg.endpoint, {
      method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload), keepalive: true
    }).then(function (res) { if (!res.ok) throw new Error("HTTP " + res.status); return res; });
  }

  function bind(form) {
    var input = form.querySelector('input[type="email"]');
    var btn = form.querySelector('button[type="submit"]');
    var msg = form.querySelector("[data-lead-msg]");
    var started = false;

    function say(html, kind) {
      if (!msg) return;
      msg.innerHTML = html || "";
      msg.dataset.kind = kind || "";
    }

    input.addEventListener("focus", function () {
      if (!started) { started = true; track("lead_form_start", { placement: form.dataset.placement }); }
    });
    input.addEventListener("input", function () { if (msg && msg.dataset.kind === "error") say(""); });
    input.addEventListener("blur", function () {
      var s = suggest(input.value.trim());
      if (s) say('Nemysleli jste <button type="button" class="lead-fix">' + s.replace(/</g, "") + "</button>?", "hint");
    });
    form.addEventListener("click", function (e) {
      if (e.target.classList.contains("lead-fix")) { input.value = e.target.textContent; say(""); input.focus(); }
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var email = input.value.trim();
      var hp = form.querySelector('input[name="website"]');
      if (hp && hp.value) return; // bot
      if (!valid(email)) { say("Zkontrolujte prosím e-mail — vypadá neúplně.", "error"); input.focus(); return; }
      btn.disabled = true;
      form.classList.add("is-sending");
      var payload = Object.assign({
        email: email, variant: cfg.variant, placement: form.dataset.placement || "", context: context,
        page: location.pathname, referrer: document.referrer.slice(0, 300), ts: new Date().toISOString()
      }, utm());
      send(payload).then(function (res) {
        // The endpoint may answer {"id": "..."}; the thank-you page uses it to attach the follow-up answer to this lead.
        return res && res.json ? res.json().catch(function () { return {}; }) : {};
      }).then(function (data) {
        store("lead", { id: (data && data.id) || null, variant: cfg.variant, masked: mask(email), context: context, placement: form.dataset.placement });
        track("generate_lead", { variant: cfg.variant, placement: form.dataset.placement });
        var sep = cfg.thankYou.indexOf("?") > -1 ? "&" : "?";
        setTimeout(function () { location.href = cfg.thankYou + sep + "v=" + encodeURIComponent(cfg.variant); }, 150);
      }).catch(function () {
        btn.disabled = false;
        form.classList.remove("is-sending");
        say("Nepodařilo se odeslat. Zkuste to prosím znovu za chvíli.", "error");
      });
    });
  }

  function sheet() {
    var el = document.getElementById("lead-sheet");
    if (!el) return;
    function open(src) {
      el.hidden = false;
      requestAnimationFrame(function () { el.classList.add("is-open"); });
      var i = el.querySelector('input[type="email"]');
      setTimeout(function () { i && i.focus(); }, 220);
      track("lead_sheet_open", { source: src || "" });
    }
    function close() {
      el.classList.remove("is-open");
      setTimeout(function () { el.hidden = true; }, 220);
    }
    document.addEventListener("click", function (e) {
      var t = e.target.closest("[data-open-sheet]");
      if (t) { e.preventDefault(); open(t.dataset.openSheet); }
      if (e.target.closest("[data-close-sheet]") || e.target === el) close();
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !el.hidden) close(); });
  }

  function sticky() {
    var bar = document.querySelector("[data-sticky-cta]");
    if (!bar || !("IntersectionObserver" in window)) return;
    var visible = new Set();
    var watch = document.querySelectorAll("[data-lead-form]:not(#lead-sheet *), [data-hide-sticky]");
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) visible.add(en.target); else visible.delete(en.target); });
      update();
    }, { threshold: 0.15 });
    watch.forEach(function (w) { io.observe(w); });
    // data-sticky-mode="always": the hero has no form of its own, so the bar is the first-screen CTA.
    var always = bar.dataset.stickyMode === "always";
    function update() {
      var scrolled = always || window.scrollY > window.innerHeight * 0.6;
      bar.classList.toggle("is-shown", scrolled && visible.size === 0 && !document.querySelector(".consent"));
    }
    window.addEventListener("scroll", update, { passive: true });
    document.addEventListener("consent:closed", update);
    update();
  }

  window.Lead = {
    setContext: function (obj) { Object.assign(context, obj); },
    track: track
  };

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-lead-form]").forEach(bind);
    sheet();
    sticky();
    track("lp_view", { variant: cfg.variant });
  });
})();
