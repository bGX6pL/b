/* Cookie consent + measurement, shared by all variants.
 *
 * Nothing that sets cookies loads before the visitor says yes (CZ: zákon 127/2005 Sb. §89, opt-in since 2022).
 * "Odmítnout" is as easy as "Povolit" — same size, same row.
 *
 * Config (optional, before this script):
 *   window.LEAD_CONFIG = { ga4: "G-XXXX", metaPixel: "1234567890" }
 * Without IDs, consent still works and events only go to window.dataLayer (handy for QA).
 *
 * window.Track(name, params) — the one function pages call. It never receives personal data.
 */
(function () {
  "use strict";
  var cfg = window.LEAD_CONFIG || {};
  var KEY = "consent_v1";
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;

  // Google Consent Mode v2: everything denied until the visitor decides.
  gtag("consent", "default", {
    ad_storage: "denied", analytics_storage: "denied", ad_user_data: "denied", ad_personalization: "denied",
    wait_for_update: 500
  });

  var META_EVENTS = { generate_lead: "Lead", lp_view: "ViewContent", lead_form_start: "InitiateCheckout" };
  var loaded = false;

  function read() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function write(v) { try { localStorage.setItem(KEY, v); } catch (e) { /* storage blocked: ask again next time */ } }

  function script(src) {
    var s = document.createElement("script");
    s.async = true; s.src = src;
    document.head.appendChild(s);
  }

  function loadTags() {
    if (loaded) return;
    loaded = true;
    gtag("consent", "update", {
      ad_storage: "granted", analytics_storage: "granted", ad_user_data: "granted", ad_personalization: "granted"
    });
    if (cfg.ga4) {
      script("https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(cfg.ga4));
      gtag("js", new Date());
      gtag("config", cfg.ga4, { anonymize_ip: true });
    }
    if (cfg.metaPixel) {
      /* Standard Meta Pixel bootstrap */
      !function (f, b, e, v, n, t, s) {
        if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
        if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = "2.0"; n.queue = [];
        t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
      }(window, document, "script", "https://connect.facebook.net/en_US/fbevents.js");
      window.fbq("init", cfg.metaPixel);
      window.fbq("track", "PageView");
    }
    (window.__trackQueue || []).forEach(function (e) { send(e[0], e[1]); });
    window.__trackQueue = [];
  }

  function send(name, params) {
    if (cfg.ga4) gtag("event", name, params);
    if (cfg.metaPixel && window.fbq && META_EVENTS[name]) window.fbq("track", META_EVENTS[name], params);
  }

  window.Track = function (name, params) {
    window.dataLayer.push(Object.assign({ event: name }, params || {}));
    if (loaded) send(name, params);
    else (window.__trackQueue = window.__trackQueue || []).push([name, params]);
  };

  function banner() {
    var el = document.createElement("div");
    el.className = "consent";
    el.setAttribute("role", "region");
    el.setAttribute("aria-label", "Souhlas s cookies");
    el.innerHTML =
      '<p>Cookies pro měření reklamy (Meta, Google) použijeme jen s vaším souhlasem. ' +
      '<a href="../ochrana-udaju/#cookies">Podrobnosti</a></p>' +
      '<div class="consent__btns"><button type="button" data-c="no">Odmítnout</button>' +
      '<button type="button" data-c="yes">Povolit</button></div>';
    el.addEventListener("click", function (e) {
      var c = e.target.getAttribute("data-c");
      if (!c) return;
      write(c === "yes" ? "granted" : "denied");
      if (c === "yes") loadTags();
      el.remove();
      document.dispatchEvent(new CustomEvent("consent:closed"));
    });
    document.body.appendChild(el);
  }

  var state = read();
  if (state === "granted") loadTags();
  document.addEventListener("DOMContentLoaded", function () {
    if (!state && !/[?&]noconsent=1/.test(location.search)) banner();
    document.querySelectorAll("[data-consent-reset]").forEach(function (a) {
      a.addEventListener("click", function (e) { e.preventDefault(); try { localStorage.removeItem(KEY); } catch (x) {} location.reload(); });
    });
  });
})();
