/* ETF tahák — the only file to edit before launch. Every page loads it first.
 *
 *   metaPixel  Meta Pixel ID (Events Manager → Data sources → your pixel), digits only, e.g. "1234567890123456"
 *   ga4        GA4 Measurement ID (Admin → Data streams → Web), e.g. "G-ABC123DEF4"
 *   endpoint   URL the e-mail form POSTs to; contract at the top of assets/lead.js.
 *              Empty = demo mode: nothing leaves the browser and the form goes straight to the thank-you page.
 *
 * Pixel and GA4 load only after the visitor clicks "Povolit" in the cookie bar (assets/consent.js).
 * These IDs are public by design (they end up in every visitor's browser), so keeping them in the repo is fine.
 * Never put a secret here (Conversions API token, e-mail service API key): those belong in the endpoint's server settings.
 */
window.LEAD_CONFIG = {
  metaPixel: "",
  ga4: "",
  endpoint: ""
};
