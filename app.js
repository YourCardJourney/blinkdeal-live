/* BlinkDeal.live - the front door to the four gold boards. Each store on the
 * wheel is labelled by the store's own name and opens that store's board. */
(function () {
  "use strict";

  /* Each store's icon is its board's own top-bar mark, with the same motion
     that board plays on hover: BlinkDeal's bolt strikes its coin, AmazonGold's
     coin rolls in over the smile, FlipkartGold's coin drops into the bag, and
     AjioGold's coin settles into its bag. */
  var PORTALS = [
    { id: "myntra", name: "Myntra", board: "BlinkDeal",
      url: "https://blinkdeal.yourcardjourney.store",
      c1: "#f13ab1", c2: "#fd913c",
      mark: '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">' +
            '<circle class="my-rim" cx="12" cy="12" r="9.2" fill="#fff" fill-opacity=".2"/>' +
            '<circle class="my-rim" cx="12" cy="12" r="6.2" opacity=".45"/>' +
            '<path class="my-bolt" d="M13.6 5.4 8.5 13.2h3.1l-.8 5.6 5.1-7.9h-3.1l.8-5.5z" fill="#fff" stroke-width="1.1"/></svg>' },
    { id: "amazon", name: "Amazon", board: "AmazonGold",
      url: "https://amazongold.yourcardjourney.store",
      c1: "#ffc266", c2: "#e47911",
      mark: '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">' +
            '<g class="am-roll"><circle cx="12" cy="9.2" r="6.4" fill="#fff" fill-opacity=".28"/>' +
            '<circle cx="12" cy="9.2" r="3.6" opacity=".7"/><path d="M12 2.8v1.9M12 13.7v1.9" opacity=".7"/></g>' +
            '<path class="am-smile" d="M4.8 18.4c3.9 2.6 10.5 2.6 14.4 0" stroke-width="2.1"/>' +
            '<path class="am-tip" d="M17.6 16.7l1.9 1.6-2.4 1" stroke-width="2.1"/></svg>' },
    { id: "flipkart", name: "Flipkart", board: "FlipkartGold",
      url: "https://flipkartgold.yourcardjourney.store",
      c1: "#5b9cff", c2: "#1a5dcc",
      mark: '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">' +
            '<g class="fk-bag"><path d="M5.5 9.5h13l-1 10.5a1.5 1.5 0 0 1-1.5 1.3H8a1.5 1.5 0 0 1-1.5-1.3z" fill="#fff" fill-opacity=".22"/>' +
            '<path d="M9 9.5V8a3 3 0 0 1 6 0v1.5" opacity=".85"/></g>' +
            '<g class="fk-coin"><circle cx="12" cy="5.2" r="3.1" fill="#ffe500" stroke="#ffe500" stroke-width="1"/>' +
            '<circle cx="12" cy="5.2" r="1.5" stroke="#2874f0" stroke-width="1.1"/></g></svg>' },
    { id: "ajio", name: "Ajio", board: "AjioGold",
      url: "https://ajiogold.yourcardjourney.store",
      c1: "#4a6684", c2: "#1f2f3c",
      mark: '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">' +
            '<g class="aj-coin"><circle cx="12" cy="6.4" r="4.2" fill="#f1d9a0" fill-opacity=".9" stroke="#f1d9a0"/>' +
            '<circle cx="12" cy="6.4" r="2.1" stroke="#866528" opacity=".7"/></g>' +
            '<g class="aj-bag"><path d="M5.2 10.6h13.6l-1.1 9.2a1.6 1.6 0 0 1-1.6 1.4H7.9a1.6 1.6 0 0 1-1.6-1.4z" fill="#fff" fill-opacity=".16" stroke-width="1.8"/>' +
            '<path d="M8.9 10.6V9.4a3.1 3.1 0 0 1 6.2 0v1.2" stroke-width="1.8"/></g></svg>' }
  ];

  /* BlinkDeal.live's own mark: a struck gold coin, milled edge, bolt through it. */
  var HUB_MARK =
    '<svg viewBox="0 0 100 100">' +
      '<circle cx="50" cy="50" r="48" fill="url(#coinRim)"/>' +
      '<circle cx="50" cy="50" r="42" fill="url(#coinFace)"/>' +
      '<circle class="hb-mill" cx="50" cy="50" r="45" fill="none" stroke="#fff6d6" stroke-opacity=".6" stroke-width="2.4" stroke-dasharray="1.6 3.1"/>' +
      '<circle class="hb-ring" cx="50" cy="50" r="33" fill="none" stroke="#fff" stroke-opacity=".65" stroke-width="2.2"/>' +
      '<path class="hb-bolt" d="M56.5 19 33.5 55h14l-4 26L67 45H53l3.5-26z" fill="#fff" stroke="#a36c16" stroke-opacity=".4" stroke-width="1.6" stroke-linejoin="round"/>' +
      '<ellipse cx="35" cy="29" rx="13" ry="5.5" fill="#fff" opacity=".45" transform="rotate(-34 35 29)"/>' +
    '</svg>';

  var $ = function (id) { return document.getElementById(id); };
  var NS = "http://www.w3.org/2000/svg";

  function el(tag, attrs, parent) {
    var n = tag.indexOf("svg:") === 0
      ? document.createElementNS(NS, tag.slice(4))
      : document.createElement(tag);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
  }

  /* ---- The dial: one coloured quadrant per store, ticks round the rim. */
  function polar(r, deg) {
    var a = (deg - 90) * Math.PI / 180;
    return [200 + r * Math.cos(a), 200 + r * Math.sin(a)];
  }
  function arc(r0, r1, a0, a1) {
    var p0 = polar(r1, a0), p1 = polar(r1, a1), p2 = polar(r0, a1), p3 = polar(r0, a0);
    var big = a1 - a0 > 180 ? 1 : 0;
    return "M" + p0 + "A" + r1 + "," + r1 + " 0 " + big + " 1 " + p1 +
           "L" + p2 + "A" + r0 + "," + r0 + " 0 " + big + " 0 " + p3 + "Z";
  }

  function drawDial() {
    var defs = $("grads");
    var segs = document.querySelector(".dial .segs");
    var ticks = document.querySelector(".dial .ticks");
    var step = 360 / PORTALS.length;

    PORTALS.forEach(function (p, i) {
      var g = el("svg:linearGradient", { id: "g-" + p.id, x1: 0, y1: 0, x2: 1, y2: 1 }, defs);
      el("svg:stop", { offset: 0, "stop-color": p.c1 }, g);
      el("svg:stop", { offset: 1, "stop-color": p.c2 }, g);
      el("svg:path", {
        d: arc(96, 190, i * step + 1.2, (i + 1) * step - 1.2),
        fill: "url(#g-" + p.id + ")", "class": "seg", "data-id": p.id
      }, segs);
    });

    for (var t = 0; t < 72; t++) {
      var a = polar(193, t * 5), b = polar(t % 6 === 0 ? 186 : 189.5, t * 5);
      el("svg:line", { x1: a[0], y1: a[1], x2: b[0], y2: b[1], "class": t % 6 ? "tick" : "tick major" }, ticks);
    }
  }

  var ARROW = '<svg class="go" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>';

  function drawPortals() {
    var orbs = $("orbs");
    var step = 360 / PORTALS.length;
    PORTALS.forEach(function (p, i) {
      var orb = el("div", { "class": "orb", "data-id": p.id }, orbs);
      orb.style.setProperty("--a", (i * step + step / 2) + "deg");
      orb.style.setProperty("--c1", p.c1);
      orb.style.setProperty("--c2", p.c2);
      var face = el("a", { "class": "orb-face", href: p.url,
                           "aria-label": "Open " + p.name + " gold deals (" + p.board + ")" }, orb);
      face.innerHTML =
        '<span class="orb-icon">' + p.mark + '</span>' +
        '<span class="orb-name">' + p.name + ARROW + '</span>';
      p.orb = orb;
    });
    document.querySelectorAll("[data-mark]").forEach(function (n) { n.innerHTML = HUB_MARK; });
  }

  /* ---- The spotlight: one store at a time plays its animation and shows its
   * arrow, so the wheel keeps saying "these are buttons". It stands aside while
   * a visitor is pointing at a store themselves. */
  var spot = -1, spotTimer;
  function spotlight() {
    var wheel = $("wheel");
    if (!wheel.matches(":hover") && !wheel.matches(":focus-within")) {
      PORTALS.forEach(function (p) { p.orb.classList.remove("play"); });
      document.querySelectorAll(".seg.lit").forEach(function (s) { s.classList.remove("lit"); });
      spot = (spot + 1) % PORTALS.length;
      var p = PORTALS[spot];
      void p.orb.offsetWidth;                          // restart the animation
      p.orb.classList.add("play");
      var seg = document.querySelector('.seg[data-id="' + p.id + '"]');
      if (seg) seg.classList.add("lit");
    }
    spotTimer = setTimeout(spotlight, 2600);
  }

  drawDial();
  drawPortals();
  setTimeout(spotlight, 1600);
})();
