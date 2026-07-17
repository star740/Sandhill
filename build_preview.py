#!/usr/bin/env python3
"""Builds preview-reel.html from index.html with proposed additions:
proof reel, testimonial band (FILLER), animated dune divider, illustrated blog cards."""

REEL = '''
<!-- PROOF REEL (preview) -->
<section class="strip">
<div id="sh-v2" style="width:100%;max-width:1100px;margin:0 auto;text-align:center;padding:10px 24px;">
  <div style="font-size:12px;letter-spacing:3px;color:#C99B5F;margin-bottom:26px;font-weight:600;">WHAT WORKING WITH SANDHILL LOOKS LIKE</div>
  <div id="v2-num" style="font-family:'Lora',Georgia,serif;font-size:clamp(64px,10vw,120px);font-weight:600;color:#FAF7F1;line-height:1;transition:opacity 1.1s;">Day 5</div>
  <div id="v2-label" style="font-family:'Lora',Georgia,serif;font-style:italic;font-size:clamp(18px,2.4vw,26px);color:#C99B5F;margin-top:18px;transition:opacity 1.1s;">your books, closed and delivered</div>
  <div id="v2-pips" style="display:flex;gap:10px;justify-content:center;margin-top:34px;"></div>
</div>
<script>
(function () {
  var slides = [
    { n: 'Day 5', l: 'your books, closed and delivered', c: null },
    { n: '100%', l: 'filings on time, every time', c: 100, f: function (v) { return v + '%'; } },
    { n: '$48M', l: 'in client revenue managed', c: 48, f: function (v) { return '$' + v + 'M'; } },
    { n: '1', l: 'clear report a founder can actually read', c: null }
  ];
  var HOLD_MS = 6000;
  var num = document.getElementById('v2-num');
  var label = document.getElementById('v2-label');
  var pips = document.getElementById('v2-pips');
  slides.forEach(function (_, k) {
    var s = document.createElement('span');
    s.style.cssText = 'width:26px;height:3px;border-radius:2px;background:' + (k === 0 ? '#C99B5F' : 'rgba(250,247,241,.25)') + ';transition:background .8s;';
    pips.appendChild(s);
  });
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  function ease(t) { return 1 - Math.pow(1 - t, 3); }
  function count(el, target, dur, fmt) {
    var t0 = performance.now();
    (function f(now) {
      var p = Math.min((now - t0) / dur, 1);
      el.textContent = fmt(Math.round(ease(p) * target));
      if (p < 1) requestAnimationFrame(f);
    })(t0);
  }
  var i = 0;
  function show(idx) {
    num.style.opacity = '0'; label.style.opacity = '0';
    setTimeout(function () {
      var s = slides[idx];
      label.textContent = s.l;
      num.style.opacity = '1'; label.style.opacity = '1';
      if (s.c !== null) { count(num, s.c, 2400, s.f); } else { num.textContent = s.n; }
      for (var k = 0; k < slides.length; k++) pips.children[k].style.background = (k === idx) ? '#C99B5F' : 'rgba(250,247,241,.25)';
    }, 1100);
  }
  var started = false;
  function start() { if (started) return; started = true; setInterval(function () { i = (i + 1) % slides.length; show(i); }, HOLD_MS); }
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (e, o) { if (e[0].isIntersecting) { start(); o.disconnect(); } }, { threshold: 0.3 })
      .observe(document.getElementById('sh-v2'));
  } else { start(); }
})();
</script>
</section>
'''

TESTIMONIALS = '''
<!-- TESTIMONIALS (preview - FILLER QUOTES, replace before launch) -->
<section class="section" id="sh-testi" style="padding:96px 0">
  <div class="wrap" style="max-width:860px;text-align:center">
    <span class="eyebrow" style="justify-content:center">What clients say</span>
    <div id="t-quote" style="font-family:'Lora',Georgia,serif;font-size:clamp(22px,3vw,32px);line-height:1.4;color:#151B2B;min-height:4.2em;transition:opacity .9s">&ldquo;Filler testimonial: Sandhill took our books from six months behind to closed by the fifth business day. Our Series A diligence was painless.&rdquo;</div>
    <div id="t-name" style="margin-top:22px;font-weight:600;color:#1E2B4F;transition:opacity .9s">[Client Name] &middot; Founder, B2B SaaS <span style="font-weight:400;color:rgba(21,27,43,.5)">(placeholder)</span></div>
    <div id="t-pips" style="display:flex;gap:10px;justify-content:center;margin-top:30px"></div>
  </div>
<script>
(function(){
  var quotes=[
    {q:'\\u201CFiller testimonial: Sandhill took our books from six months behind to closed by the fifth business day. Our Series A diligence was painless.\\u201D',n:'[Client Name] \\u00B7 Founder, B2B SaaS'},
    {q:'\\u201CFiller testimonial: It\\u2019s like having a controller, a bookkeeper, and an accounting team without making a single hire. Board reporting went from dreaded to done.\\u201D',n:'[Client Name] \\u00B7 CEO, Tech Startup'},
    {q:'\\u201CFiller testimonial: They implemented ASC 606 revenue recognition properly the first time. Our auditors had zero findings.\\u201D',n:'[Client Name] \\u00B7 COO, SaaS Platform'}
  ];
  var qe=document.getElementById('t-quote'),ne=document.getElementById('t-name'),pp=document.getElementById('t-pips');
  quotes.forEach(function(_,k){var s=document.createElement('span');s.style.cssText='width:26px;height:3px;border-radius:2px;background:'+(k===0?'#C99B5F':'rgba(21,27,43,.15)')+';transition:background .8s';pp.appendChild(s);});
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  var i=0;
  setInterval(function(){
    i=(i+1)%quotes.length;
    qe.style.opacity='0';ne.style.opacity='0';
    setTimeout(function(){
      qe.innerHTML=quotes[i].q;
      ne.innerHTML=quotes[i].n+' <span style="font-weight:400;color:rgba(21,27,43,.5)">(placeholder)</span>';
      qe.style.opacity='1';ne.style.opacity='1';
      for(var k=0;k<quotes.length;k++)pp.children[k].style.background=(k===i)?'#C99B5F':'rgba(21,27,43,.15)';
    },900);
  },7500);
})();
</script>
</section>
'''

DUNES = '''
<!-- ANIMATED DUNE DIVIDER (preview) -->
<div aria-hidden="true" style="overflow:hidden;line-height:0;background:#FAF7F1">
  <div class="dune-track" style="display:flex;width:200%;animation:duneDrift 38s linear infinite">
    <svg viewBox="0 0 1200 110" preserveAspectRatio="none" style="width:50%;height:96px;flex:none">
      <path d="M0 110 C150 40 320 85 480 60 C640 35 800 80 960 55 C1080 38 1150 55 1200 45 L1200 110 Z" fill="#EDE3D2"/>
      <path d="M0 110 C200 75 380 100 560 82 C740 64 900 95 1200 70 L1200 110 Z" fill="#C99B5F" opacity=".35"/>
      <path d="M0 110 C260 95 520 108 780 96 C980 87 1120 100 1200 92 L1200 110 Z" fill="#1E2B4F" opacity=".16"/>
    </svg>
    <svg viewBox="0 0 1200 110" preserveAspectRatio="none" style="width:50%;height:96px;flex:none">
      <path d="M0 110 C150 40 320 85 480 60 C640 35 800 80 960 55 C1080 38 1150 55 1200 45 L1200 110 Z" fill="#EDE3D2"/>
      <path d="M0 110 C200 75 380 100 560 82 C740 64 900 95 1200 70 L1200 110 Z" fill="#C99B5F" opacity=".35"/>
      <path d="M0 110 C260 95 520 108 780 96 C980 87 1120 100 1200 92 L1200 110 Z" fill="#1E2B4F" opacity=".16"/>
    </svg>
  </div>
</div>
<style>
@keyframes duneDrift{from{transform:translateX(0)}to{transform:translateX(-50%)}}
@media(prefers-reduced-motion:reduce){.dune-track{animation:none}}
</style>
'''

POSTS = '''
    <div class="posts">
      <a class="post post-img reveal" href="blog/asc-606-saas-revenue-recognition.html" style="background:#fff;color:#151B2B;padding:0;overflow:hidden;border:1px solid rgba(21,27,43,.14)">
        <svg viewBox="0 0 400 150" preserveAspectRatio="none" style="width:100%;height:150px;display:block" aria-hidden="true">
          <rect width="400" height="150" fill="#1E2B4F"/>
          <path d="M0 150 C80 90 160 120 240 80 C300 50 360 70 400 40 L400 150 Z" fill="#C99B5F" opacity=".5"/>
          <path d="M0 150 C120 120 220 140 400 95 L400 150 Z" fill="#EDE3D2" opacity=".35"/>
          <path d="M40 105 L110 70 L180 88 L260 45 L330 60 L385 28" stroke="#FAF7F1" stroke-width="3" fill="none" stroke-linecap="round"/>
          <circle cx="385" cy="28" r="5" fill="#C99B5F"/>
        </svg>
        <span style="display:flex;flex-direction:column;gap:12px;padding:26px 28px">
          <span class="cat">GAAP Accounting</span>
          <h3 style="color:#151B2B">ASC 606 and SaaS: What Startup Founders Actually Need to Know about Recognizing Revenue</h3>
          <span class="read">Read article &rarr;</span>
        </span>
      </a>
      <a class="post post-img reveal" href="blog/cash-vs-accrual-accounting.html" style="background:#fff;color:#151B2B;padding:0;overflow:hidden;border:1px solid rgba(21,27,43,.14)">
        <svg viewBox="0 0 400 150" preserveAspectRatio="none" style="width:100%;height:150px;display:block" aria-hidden="true">
          <rect width="400" height="150" fill="#1E2B4F"/>
          <path d="M0 150 C100 100 200 130 400 70 L400 150 Z" fill="#EDE3D2" opacity=".3"/>
          <g stroke="#FAF7F1" stroke-width="3" stroke-linecap="round">
            <line x1="70" y1="120" x2="70" y2="82"/><line x1="130" y1="120" x2="130" y2="64"/>
            <line x1="190" y1="120" x2="190" y2="94"/><line x1="250" y1="120" x2="250" y2="50"/>
            <line x1="310" y1="120" x2="310" y2="72"/>
          </g>
          <line x1="40" y1="120" x2="360" y2="120" stroke="#C99B5F" stroke-width="3" stroke-linecap="round"/>
        </svg>
        <span style="display:flex;flex-direction:column;gap:12px;padding:26px 28px">
          <span class="cat">GAAP Accounting</span>
          <h3 style="color:#151B2B">Cash vs. Accrual Accounting: Why the Switch Hurts and How to Get Ahead of It</h3>
          <span class="read">Read article &rarr;</span>
        </span>
      </a>
    </div>'''

import re
c = open('index.html').read()

# 1) reel between software section and insights section
marker = '<section class="section" style="padding-top:0">'
assert marker in c
c = c.replace(marker, REEL + '\n' + marker, 1)

# 2) testimonial band between services (sand) and software sections
tools_marker = '<section class="section">\n  <div class="wrap">\n    <div class="section-head center reveal">\n      <span class="eyebrow">Software we know</span>'
assert tools_marker in c
c = c.replace(tools_marker, TESTIMONIALS + '\n' + tools_marker, 1)

# 3) animated dune divider above the closing CTA
cta_marker = '<section class="cta">'
assert cta_marker in c
c = c.replace(cta_marker, DUNES + '\n' + cta_marker, 1)

# 4) illustrated blog cards
posts_re = re.compile(r'    <div class="posts">.*?</div>\n', re.S)
assert posts_re.search(c)
c = posts_re.sub(POSTS + '\n', c, count=1)

# preview metadata
c = c.replace('<title>', '<title>PREVIEW - ', 1)
c = c.replace('<meta name="description"', '<meta name="robots" content="noindex"><meta name="description"', 1)
# post h3 color fix for white cards
c = c.replace('</head>', '<style>.post-img:hover{transform:translateY(-4px)}.post-img .cat{color:#C99B5F}.post-img .read{color:#1E2B4F}</style></head>', 1)

open('preview-reel.html','w').write(c)
print('preview rebuilt with reel + testimonials + dunes + illustrated cards')
