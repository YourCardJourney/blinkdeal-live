/* Light / dark toggle, shared by every page.
 *
 * Dark is the default for everyone, whatever the device is set to. A visitor
 * who switches to light keeps light on that device (localStorage); nobody
 * else is affected. The <head> of each page sets the theme before first paint
 * with the same rule, so there is never a flash of the wrong one.
 */
(function () {
  "use strict";
  var KEY = "bdlive.theme", d = document.documentElement;

  function paint(t) {
    d.setAttribute("data-theme", t);
    var m = document.querySelector('meta[name="theme-color"]');
    if (m) m.setAttribute("content", t === "dark" ? "#0e0c09" : "#fbf8f1");
    var b = document.getElementById("themeBtn");
    if (b) b.setAttribute("aria-label", t === "dark" ? "Switch to light" : "Switch to dark");
  }

  paint(d.getAttribute("data-theme") || "dark");

  var btn = document.getElementById("themeBtn");
  if (btn) btn.addEventListener("click", function () {
    var next = d.getAttribute("data-theme") === "dark" ? "light" : "dark";
    paint(next);
    try { localStorage.setItem(KEY, next); } catch (e) { /* private mode: still switches, just not remembered */ }
  });
})();
