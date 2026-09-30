/* Google Analytics 4 for blinkdeal.live.
 *
 * Paste the Measurement ID (G-XXXXXXXXXX, from Analytics -> Admin -> Data
 * streams) into GA_ID. Empty = nothing loads, so the page never breaks on it.
 *
 * Besides page views it records one event, `store_tap`, with the store's
 * name - so Analytics can say which of the four boards people actually open.
 */
(function () {
  "use strict";

  var GA_ID = "";

  if (!GA_ID || location.hostname === "localhost" || location.hostname === "127.0.0.1") return;

  var s = document.createElement("script");
  s.async = true;
  s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_ID;
  document.head.appendChild(s);

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag("js", new Date());
  gtag("config", GA_ID);

  // Which store was tapped - from the wheel, or from the About page's list.
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a.orb-face, a.store");
    if (!a) return;
    var orb = a.closest(".orb");
    var store = orb ? orb.getAttribute("data-id") : (a.querySelector("b") || {}).textContent;
    gtag("event", "store_tap", {
      store: (store || "").toLowerCase(),
      from: orb ? "wheel" : "about",
      link_url: a.href,
      transport_type: "beacon"
    });
  });
})();
