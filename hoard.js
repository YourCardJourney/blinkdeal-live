/* The gold in the background - WhichBike's rain, turned down to scenery.
 *
 * On arrival a short shower falls through the page; after that coins and
 * 999.9 bars drift down at three depths (far ones small, faint and slow), so
 * the page always has a little gold moving behind the wheel without ever
 * competing with it. The wheel's opaque dial hides whatever passes behind it.
 */
(function () {
  "use strict";

  var canvas = document.getElementById("hoard");
  if (!canvas) return;
  var ctx = canvas.getContext("2d");
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  var W, H, DPR, drops = [], raf, last;
  var LAYERS = [                                   // far → near
    { scale: .45, speed: 55,  alpha: .22, share: .45 },
    { scale: .7,  speed: 90,  alpha: .38, share: .35 },
    { scale: 1,   speed: 135, alpha: .55, share: .20 }
  ];

  function rand(a, b) { return a + Math.random() * (b - a); }

  function layer() {
    var r = Math.random(), acc = 0;
    for (var i = 0; i < LAYERS.length; i++) { acc += LAYERS[i].share; if (r < acc) return LAYERS[i]; }
    return LAYERS[0];
  }

  function makeDrop(burst) {
    var L = burst ? LAYERS[1 + (Math.random() < .5 ? 1 : 0)] : layer();
    var s = L.scale * Math.max(.8, Math.min(1.15, W / 1100));
    var bar = Math.random() < .22;
    return {
      L: L, bar: bar, burst: burst,
      x: rand(-20, W + 20),
      y: burst ? rand(-H * .9, -30) : rand(-160, -30),
      vy: burst ? rand(520, 820) : L.speed * rand(.8, 1.25),
      sway: rand(.4, 1.2), swayAmp: rand(6, 22) * L.scale, t: rand(0, 6.28),
      angle: rand(-1, 1), spin: rand(-1.4, 1.4) * (bar ? 1 : .6),
      flip: rand(1.2, 3.2), phase: rand(0, 6.28),
      r: rand(10, 18) * s, w: rand(34, 50) * s,
      tone: Math.random()
    };
  }

  var GOLD = [
    ["#fff4c9", "#f3cd68", "#d89e2e", "#9f6b17"],
    ["#ffe9a8", "#e8b54a", "#c48722", "#8a5a12"],
    ["#fff8dc", "#f7d77e", "#e0ac40", "#b07a1e"]
  ];
  function pal(d) { return GOLD[d.tone < .45 ? 0 : d.tone < .8 ? 1 : 2]; }

  function coin(d, ry) {
    var r = d.r, col = pal(d), th = Math.max(1.2, r * .2 * (1 - ry / r) + 1);
    ctx.fillStyle = col[3];
    ctx.beginPath(); ctx.ellipse(0, th, r, ry, 0, 0, 6.2832); ctx.fill();
    ctx.fillRect(-r, 0, r * 2, th);
    var f = ctx.createLinearGradient(-r, -ry, r, ry);
    f.addColorStop(0, col[0]); f.addColorStop(.35, col[1]); f.addColorStop(.72, col[2]); f.addColorStop(1, col[3]);
    ctx.fillStyle = f;
    ctx.beginPath(); ctx.ellipse(0, 0, r, ry, 0, 0, 6.2832); ctx.fill();
    if (ry > r * .25) {
      ctx.strokeStyle = "rgba(255,255,255,.5)"; ctx.lineWidth = Math.max(.8, r * .07);
      ctx.beginPath(); ctx.ellipse(0, 0, r * .76, ry * .76, 0, 0, 6.2832); ctx.stroke();
      ctx.fillStyle = "rgba(255,255,255,.5)";
      ctx.beginPath(); ctx.ellipse(-r * .38, -ry * .42, r * .28, ry * .14, -.35, 0, 6.2832); ctx.fill();
    }
  }

  function bar(d) {
    var w = d.w, h = w * .4, col = pal(d), topW = w * .36, lip = -h * .12;
    var f = ctx.createLinearGradient(0, lip, 0, h / 2);
    f.addColorStop(0, col[1]); f.addColorStop(.55, col[2]); f.addColorStop(1, col[3]);
    ctx.fillStyle = f;
    ctx.beginPath();
    ctx.moveTo(-topW, lip); ctx.lineTo(topW, lip); ctx.lineTo(w / 2, h / 2); ctx.lineTo(-w / 2, h / 2);
    ctx.closePath(); ctx.fill();
    var t = ctx.createLinearGradient(-topW, -h / 2, topW, lip);
    t.addColorStop(0, col[0]); t.addColorStop(1, col[1]);
    ctx.fillStyle = t;
    ctx.beginPath();
    ctx.moveTo(-topW * .86, -h / 2); ctx.lineTo(topW * .86, -h / 2); ctx.lineTo(topW, lip); ctx.lineTo(-topW, lip);
    ctx.closePath(); ctx.fill();
    if (w > 30) {
      ctx.fillStyle = "rgba(110,70,8,.45)";
      ctx.font = "700 " + (h * .3).toFixed(1) + "px Inter, system-ui, sans-serif";
      ctx.textAlign = "center"; ctx.textBaseline = "middle";
      ctx.fillText("999.9", 0, h * .2);
    }
  }

  function steady() {                   // how many drift at once, by screen area
    return Math.round(Math.max(14, Math.min(46, W * H / 36000)));
  }

  function frame(now) {
    var dt = Math.min(.05, (now - last) / 1000);
    last = now;
    ctx.clearRect(0, 0, W, H);

    for (var i = drops.length - 1; i >= 0; i--) {
      var d = drops[i];
      d.t += dt; d.y += d.vy * dt; d.angle += d.spin * dt; d.phase += d.flip * dt;
      if (d.y > H + 60) {
        if (d.burst || drops.length > steady()) { drops.splice(i, 1); continue; }
        var n = makeDrop(false); drops[i] = n; continue;
      }
      var x = d.x + Math.sin(d.t * d.sway) * d.swayAmp;
      ctx.save();
      ctx.globalAlpha = d.burst ? .75 : d.L.alpha;
      ctx.translate(x, d.y);
      ctx.rotate(d.angle);
      if (d.bar) bar(d);
      else coin(d, d.r * Math.max(.16, Math.abs(Math.cos(d.phase))));
      ctx.restore();
    }
    raf = requestAnimationFrame(frame);
  }

  function size() {
    DPR = Math.min(2, window.devicePixelRatio || 1);
    W = window.innerWidth; H = window.innerHeight;
    canvas.width = W * DPR; canvas.height = H * DPR;
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  }

  function start() {
    size();
    drops = [];
    // the opening shower
    var burst = Math.round(Math.max(30, Math.min(80, W / 16)));
    for (var i = 0; i < burst; i++) drops.push(makeDrop(true));
    // the steady drift, already spread down the screen so it never starts empty
    for (var k = 0, n = steady(); k < n; k++) {
      var d = makeDrop(false); d.y = rand(-H * .6, H); drops.push(d);
    }
    last = performance.now();
    raf = requestAnimationFrame(frame);
  }

  var rt;
  window.addEventListener("resize", function () {
    clearTimeout(rt);
    rt = setTimeout(size, 150);
  });
  document.addEventListener("visibilitychange", function () {
    if (document.hidden) cancelAnimationFrame(raf);
    else { last = performance.now(); raf = requestAnimationFrame(frame); }
  });

  start();
})();
