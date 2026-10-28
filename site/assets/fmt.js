/* Czech number/date formatting shared by all variants. */
window.Fmt = (function () {
  "use strict";
  var NB = " "; // no-break space before units, as Czech typography requires

  // Percent: keeps every significant decimal of a fee (0.0945 → "0,0945 %"), at least 2 decimals.
  function pct(v, maxDec) {
    if (v === null || v === undefined || isNaN(v)) return "–";
    var d = maxDec === undefined ? 4 : maxDec;
    var s = Number(v).toFixed(d).replace(/0+$/, "");
    var dec = (s.split(".")[1] || "").length;
    if (dec < 2) s = Number(v).toFixed(2);
    return s.replace(".", ",") + NB + "%";
  }

  // Short percent for prose: 2 → "2 %", 0.5 → "0,5 %", 0.03 → "0,03 %".
  function pctS(v) {
    if (v === null || v === undefined || isNaN(v)) return "–";
    return String(Number(Number(v).toFixed(4))).replace(".", ",") + NB + "%";
  }

  // Signed percent for returns, fixed decimals: 14.2 → "14,2 %", -3 → "−3,0 %".
  function ret(v, dec) {
    if (v === null || v === undefined || isNaN(v)) return "–";
    var s = Math.abs(v).toFixed(dec === undefined ? 1 : dec).replace(".", ",");
    return (v < 0 ? "−" : "") + s + NB + "%";
  }

  function num(v, dec) {
    if (v === null || v === undefined || isNaN(v)) return "–";
    return Number(v).toLocaleString("cs-CZ", { minimumFractionDigits: dec || 0, maximumFractionDigits: dec || 0 }).replace(/\s/g, NB);
  }

  function czk(v) { return num(Math.round(v)) + NB + "Kč"; }

  // Billions of USD with Czech wording: 712.4 → "712 mld. USD", 8.43 → "8,4 mld. USD".
  function bn(v, cur) {
    if (v === null || v === undefined) return "–";
    return num(v, v >= 100 ? 0 : 1) + NB + "mld." + NB + (cur || "USD");
  }

  function date(iso) {
    if (!iso) return "";
    var p = iso.split("-");
    return Number(p[2]) + "." + NB + Number(p[1]) + "." + NB + p[0];
  }

  return { pct: pct, pctS: pctS, ret: ret, num: num, czk: czk, bn: bn, date: date, NB: NB };
})();
