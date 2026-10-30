/* ETF tahák — the public keys for the live site. Every page loads it first. (Secret keys: Vercel environment variables, see api/lead.mjs.)
 *
 *   metaPixel  Meta Pixel ID (Events Manager → Data sources → your pixel), digits only, e.g. "1234567890123456"
 *   ga4        GA4 Measurement ID (Admin → Data streams → Web), e.g. "G-ABC123DEF4"
 *   endpoint   where the e-mail form POSTs: the site's own function /api/lead (api/lead.mjs). It needs the Ecomail
 *              keys in Vercel → Settings → Environment Variables; without them it answers 503 and the form says "try again".
 *              On localhost it stays empty = demo mode: nothing leaves the browser, the form goes straight to the thank-you page.
 *
 * Pixel and GA4 load only after the visitor clicks "Povolit" in the cookie bar (assets/consent.js).
 * These IDs are public by design (they end up in every visitor's browser), so keeping them in the repo is fine.
 * Never put a secret here (Conversions API token, e-mail service API key): those belong in the endpoint's server settings.
 */
window.LEAD_CONFIG = {
  metaPixel: "",
  ga4: "",
  endpoint: /^(localhost|127\.0\.0\.1|\[::1\])$/.test(location.hostname) ? "" : "/api/lead"
};
