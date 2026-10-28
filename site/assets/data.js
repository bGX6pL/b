/* PROVISIONAL layout data — overwritten by tools/build_data.py from data/etfs.json. Do not ship. */
window.ETF_DATA = {
  meta: { compiled: "2026-10-29", returns_as_of: "2026-09-30", provisional: true },
  fx: { usd_czk: 21.0, eur_czk: 24.3, date: "2026-10-28" },
  us: [
    { t: "VOO", name: "Vanguard S&P 500 ETF", issuer: "Vanguard", ex: "NYSE Arca", index: "S&P 500", ter: 0.03, aum: 700, n: 504, dist: "čtvrtletně", yld: 1.2, r5: 15, r10: 14, twin: "sp500", cat: "usa" },
    { t: "SPY", name: "SPDR S&P 500 ETF Trust", issuer: "State Street", ex: "NYSE Arca", index: "S&P 500", ter: 0.0945, aum: 650, n: 503, dist: "čtvrtletně", yld: 1.1, r5: 15, r10: 14, twin: "sp500", cat: "usa" },
    { t: "IVV", name: "iShares Core S&P 500 ETF", issuer: "iShares", ex: "NYSE Arca", index: "S&P 500", ter: 0.03, aum: 650, n: 503, dist: "čtvrtletně", yld: 1.2, r5: 15, r10: 14, twin: "sp500", cat: "usa" },
    { t: "QQQ", name: "Invesco QQQ Trust", issuer: "Invesco", ex: "Nasdaq", index: "Nasdaq-100", ter: 0.20, aum: 380, n: 101, dist: "čtvrtletně", yld: 0.5, r5: 17, r10: 18, twin: "ndx", cat: "usa", ref: true },
    { t: "VTI", name: "Vanguard Total Stock Market ETF", issuer: "Vanguard", ex: "NYSE Arca", index: "CRSP US Total Market", ter: 0.03, aum: 500, n: 3500, dist: "čtvrtletně", yld: 1.2, r5: 14, r10: 13, twin: "usall", cat: "usa" },
    { t: "VT", name: "Vanguard Total World Stock ETF", issuer: "Vanguard", ex: "NYSE Arca", index: "FTSE Global All Cap", ter: 0.06, aum: 60, n: 9800, dist: "čtvrtletně", yld: 1.8, r5: 11, r10: 10, twin: "world", cat: "svet" },
    { t: "SCHD", name: "Schwab US Dividend Equity ETF", issuer: "Schwab", ex: "NYSE Arca", index: "Dow Jones US Dividend 100", ter: 0.06, aum: 70, n: 103, dist: "čtvrtletně", yld: 3.8, r5: 11, r10: 11, twin: "usdiv", cat: "dividendy" },
    { t: "VUG", name: "Vanguard Growth ETF", issuer: "Vanguard", ex: "NYSE Arca", index: "CRSP US Large Cap Growth", ter: 0.04, aum: 180, n: 170, dist: "čtvrtletně", yld: 0.5, r5: 16, r10: 16, twin: "usgrowth", cat: "usa" },
    { t: "GLD", name: "SPDR Gold Shares", issuer: "State Street", ex: "NYSE Arca", index: "LBMA Gold Price PM", ter: 0.40, aum: 100, n: null, dist: "nevyplácí", yld: 0, r5: 12, r10: 10, twin: "gold", cat: "zlato" }
  ],
  twins: {
    sp500: { label: "S&P 500", match: "exact", pick: { name: "SPDR S&P 500 UCITS ETF (Acc)", isin: "IE000XZSV718", ticker: "SPYL", ex: "Xetra", ter: 0.03, dist: "acc", size_eur_bn: 10 },
      alt: [{ name: "iShares Core S&P 500 UCITS ETF (Acc)", isin: "IE00B5BMR087", ticker: "SXR8", ex: "Xetra", ter: 0.07, dist: "acc" }, { name: "Vanguard S&P 500 UCITS ETF (Acc)", isin: "IE00BFMXXD54", ticker: "VUAA", ex: "Xetra", ter: 0.07, dist: "acc" }] },
    ndx: { label: "Nasdaq-100", match: "exact", pick: { name: "iShares Nasdaq 100 UCITS ETF (Acc)", isin: "IE00B53SZB19", ticker: "SXRV", ex: "Xetra", ter: 0.30, dist: "acc", size_eur_bn: 15 }, alt: [] },
    usall: { label: "celý trh USA", match: "close", pick: { name: "SPDR MSCI USA UCITS ETF", isin: "IE000XXXXXXX", ticker: "—", ex: "Xetra", ter: 0.05, dist: "acc", size_eur_bn: 1 }, alt: [] },
    world: { label: "celý svět", match: "close", pick: { name: "Vanguard FTSE All-World UCITS ETF (Acc)", isin: "IE00BK5BQT80", ticker: "VWCE", ex: "Xetra", ter: 0.19, dist: "acc", size_eur_bn: 20 }, alt: [] },
    usdiv: { label: "dividendové akcie USA", match: "close", pick: { name: "provisional", isin: "—", ticker: "—", ex: "Xetra", ter: 0.3, dist: "dist", size_eur_bn: 1 }, alt: [] },
    usgrowth: { label: "růstové akcie USA", match: "close", pick: { name: "provisional", isin: "—", ticker: "—", ex: "Xetra", ter: 0.2, dist: "acc", size_eur_bn: 1 }, alt: [] },
    gold: { label: "zlato", match: "close", pick: { name: "provisional gold ETC", isin: "—", ticker: "—", ex: "Xetra", ter: 0.12, dist: "acc", size_eur_bn: 1 }, alt: [] }
  },
  brokers: [],
  bank: { entry_pct: 3, ter_pct: 2.0, label: "typický akciový fond banky (provisional)" }
};
