#!/usr/bin/env python3
import time
VERSION = str(int(time.time()))
"""Generates all Sandhill HQ pages with a shared shell. Run from repo root."""
import os, time
V = str(int(time.time()))

CAL = "https://calendar.app.google/ngdhcYuakQkRgjyx5"

def shell(title, desc, body, prefix="", active="", cta_html=None):
    V = VERSION
    def cls(name):
        return ' class="active"' if name == active else ""
    cta_section = cta_html if cta_html is not None else f"""<section class="cta">
  <h2 class="reveal">Supporting your growth today, preparing you for tomorrow</h2>
  <a class="btn btn-sand reveal" href="{CAL}" target="_blank" rel="noopener">Schedule a call</a>
</section>"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="icon" type="image/png" sizes="64x64" href="{prefix}assets/favicon.png">
<link rel="icon" type="image/png" sizes="192x192" href="{prefix}assets/favicon-192.png">
<link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{prefix}style.css?v={V}">
</head>
<body>

<header>
  <div class="wrap nav">
    <a class="logo" href="{prefix}index.html"><img class="logo-mark" src="{prefix}assets/logo-mark.png" alt="" aria-hidden="true">Sandhill<span>&nbsp;HQ</span></a>
    <nav class="nav-links" id="navLinks">
      <a href="{prefix}index.html"{cls('home')}>Home</a>
      <a href="{prefix}services.html"{cls('services')}>Services</a>
      <a href="{prefix}roadmap.html"{cls('roadmap')}>Roadmap</a>
      <a href="{prefix}about.html"{cls('about')}>About Us</a>
      <a href="{prefix}blog.html"{cls('blog')}>Insights</a>
    </nav>
    <a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener">Schedule a call</a>
    <button class="menu-btn" id="menuBtn" aria-label="Open menu">&#9776;</button>
  </div>
</header>

{body}

{cta_section}

<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="logo" href="{prefix}index.html"><img class="logo-mark" src="{prefix}assets/logo-mark.png" alt="" aria-hidden="true">Sandhill<span>&nbsp;HQ</span></a>
        <p style="font-size:14px;color:rgba(21,27,43,.6);margin-top:14px;max-width:32ch">Outsourced accounting and finance for SaaS startups and growing businesses.</p>
      </div>
      <div>
        <h4>Company</h4>
        <a href="{prefix}about.html">About Us</a>
        <a href="{prefix}roadmap.html">Founder's Roadmap</a>
        <a href="{prefix}faq.html">FAQ</a>
        <a href="{prefix}blog.html">Insights</a>
      </div>
      <div>
        <h4>Services</h4>
        <a href="{prefix}services.html#bookkeeping">Bookkeeping &amp; Operations</a>
        <a href="{prefix}services.html#accounting">Accounting &amp; Reporting</a>
        <a href="{prefix}services.html#controller">Controller Services</a>
      </div>
      <div>
        <h4>Contact</h4>
        <a href="{CAL}" target="_blank" rel="noopener">Book a call</a>
        <a href="mailto:info@sandhillhq.com">info@sandhillhq.com</a>
        <a href="{prefix}contact.html">Contact us</a>
      </div>
    </div>
    <div class="foot-note">
      <span>&copy; 2026 Sandhill HQ. All rights reserved.</span>
      <span><a href="{prefix}legal.html">Legal</a></span>
    </div>
  </div>
</footer>

<script>
document.getElementById('menuBtn').addEventListener('click',()=>{{
  document.getElementById('navLinks').classList.toggle('open');
}});
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}}),{{threshold:.12}});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
</script>
</body>
</html>
"""

pages = {}

TESTI_REEL = '''
<!-- TESTIMONIAL -->
<section class="section" id="sh-testi" style="padding:96px 0">
  <div class="wrap" style="max-width:860px;text-align:center">
    <span class="eyebrow" style="justify-content:center">What clients say</span>
    <div class="reveal" style="font-family:'Lora',Georgia,serif;font-size:clamp(22px,3vw,32px);line-height:1.4;color:#151B2B">&ldquo;Sandhill was a fantastic partner - reliable, proactive, and skilled across the board. They supported us with month-end close, reporting, ad hoc projects, financial analysis and much more. The work was accurate and thoughtful, and they adapted quickly to our needs. Highly recommend!&rdquo;</div>
    <div class="reveal" style="margin-top:22px;font-weight:600;color:#1E2B4F">Anthony &middot; CFO, Technology Company</div>
  </div>
</section>

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


home_cta = f"""<section class="cta cta-insights">
  <div class="wrap">
    <span class="eyebrow eyebrow-light reveal">Insights &amp; resources</span>
    <h2 class="reveal">From the Sandhill <em>desk</em></h2>
    <div class="posts posts-light">
      <a class="post post-white reveal" href="blog/asc-606-saas-revenue-recognition.html">
        <svg viewBox="0 0 400 150" preserveAspectRatio="none" style="width:100%;height:150px;display:block" aria-hidden="true">
          <rect width="400" height="150" fill="#EDE3D2"/>
          <path d="M0 150 C80 100 160 128 240 92 C300 66 360 84 400 56 L400 150 Z" fill="#C99B5F" opacity=".45"/>
          <path d="M40 105 L110 70 L180 88 L260 45 L330 60 L385 28" stroke="#1E2B4F" stroke-width="3" fill="none" stroke-linecap="round"/>
          <circle cx="385" cy="28" r="5" fill="#1E2B4F"/>
        </svg>
        <span class="post-body">
          <span class="cat">GAAP Accounting</span>
          <h3>ASC 606 and SaaS: What Startup Founders Actually Need to Know about Recognizing Revenue</h3>
          <span class="read">Read article &rarr;</span>
        </span>
      </a>
      <a class="post post-white reveal" href="blog/cash-vs-accrual-accounting.html">
        <svg viewBox="0 0 400 150" preserveAspectRatio="none" style="width:100%;height:150px;display:block" aria-hidden="true">
          <rect width="400" height="150" fill="#C99B5F"/>
          <path d="M0 150 C100 112 220 136 400 92 L400 150 Z" fill="#EDE3D2" opacity=".5"/>
          <g stroke="#1E2B4F" stroke-width="3" stroke-linecap="round">
            <line x1="70" y1="120" x2="70" y2="82"/><line x1="130" y1="120" x2="130" y2="64"/>
            <line x1="190" y1="120" x2="190" y2="94"/><line x1="250" y1="120" x2="250" y2="50"/>
            <line x1="310" y1="120" x2="310" y2="72"/>
          </g>
          <line x1="40" y1="120" x2="360" y2="120" stroke="#FAF7F1" stroke-width="3" stroke-linecap="round"/>
        </svg>
        <span class="post-body">
          <span class="cat">GAAP Accounting</span>
          <h3>Cash vs. Accrual Accounting: Why the Switch Hurts and How to Get Ahead of It</h3>
          <span class="read">Read article &rarr;</span>
        </span>
      </a>
    </div>
    <a class="btn btn-sand reveal" href="{CAL}" target="_blank" rel="noopener">Schedule a call</a>
  </div>
</section>"""

# ---------------- HOME ----------------
pages["index.html"] = dict(
    cta_html=home_cta,
    title="Outsourced Accounting & Bookkeeping Services | Sandhill HQ",
    desc="Outsourced accounting for SaaS startups and growing businesses. Expert bookkeeping, GAAP financial reporting, ASC 606 revenue recognition, and controller services.",
    active="",
    body=f"""
<section class="hero hero-c">
  <div class="wrap">
    <span class="eyebrow">Outsourced accounting &amp; finance</span>
    <h1>Your scalable accounting<br class="br-lg"> &amp;&nbsp;finance <em>department</em></h1>
    <p>From bookkeeping and monthly close to compliance, investor reporting, and strategic guidance, we become your complete finance team.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener">Schedule a call</a>
      <a class="btn btn-ghost" href="services.html">Explore our services</a>
    </div>
  </div>
</section>

<section class="strip">
  <div class="wrap">
    <h2 class="reveal strip-c">We work with SaaS companies, tech startups and founder-led businesses looking to grow</h2>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Why outsource</span>
      <h2>The <em>advantages</em> of an outsourced finance team</h2>
    </div>
    <div class="cards">
      <div class="card reveal">
        <div class="mark"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3.2"/><path d="M3.5 19c.6-3 2.9-4.6 5.5-4.6s4.9 1.6 5.5 4.6"/><circle cx="17" cy="9.5" r="2.4"/><path d="M16.2 14.6c2.2.2 3.9 1.6 4.3 4"/></svg></div>
        <h3>A Complete Finance Team</h3>
        <p>Instead of relying on one person to do it all, you gain access to specialized expertise across bookkeeping, accounting, and strategic finance.</p>
      </div>
      <div class="card reveal">
        <div class="mark"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 12a8 8 0 1 1-2.3-5.6"/><path d="M20 3v4h-4"/></svg></div>
        <h3>Built-In Continuity</h3>
        <p>No disruption from turnover, vacations, or staffing changes. Our team-based approach ensures your financial operations stay consistent and on track.</p>
      </div>
      <div class="card reveal">
        <div class="mark"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20V14"/><path d="M10 20V10"/><path d="M16 20V6"/><path d="M15 3.5h5v5" fill="none"/><path d="M20 3.5 13 10.5"/></svg></div>
        <h3>A Solution That Scales</h3>
        <p>From early-stage growth to investor readiness, our support evolves alongside your business without the need to hire additional finance staff.</p>
      </div>
    </div>
  </div>
</section>

<section class="section services-bg">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">What we do</span>
      <h2>Finance as a <em>Service</em></h2>
    </div>
    <div class="pillars">
      <div class="pillar reveal">
        <div class="tag">01 &middot; Foundation</div>
        <h3>Bookkeeping &amp; Operations</h3>
        <p>The day-to-day financial foundation that keeps your business running smoothly.</p>
        <ul>
          <li>Accounts Payable (AP)</li>
          <li>Accounts Receivable (AR)</li>
          <li>Payroll Administration</li>
          <li>Expense Management</li>
          <li>Bank &amp; Credit Card Reconciliations</li>
          <li>Sales Tax Filings</li>
          <li>Vendor Management</li>
          <li>Financial System Implementation</li>
          <li>Transaction Categorization</li>
        </ul>
      </div>
      <div class="pillar reveal">
        <div class="tag">02 &middot; Clarity</div>
        <h3>Accounting &amp; Reporting</h3>
        <p>Accurate financial reporting built to support growth and decision-making.</p>
        <ul>
          <li>Monthly Financial Statements</li>
          <li>Month-End Close</li>
          <li>Accrual Accounting</li>
          <li>Revenue Recognition (ASC 606)</li>
          <li>Journal Entries &amp; Adjustments</li>
          <li>General Ledger Management</li>
          <li>Fixed Asset Accounting</li>
          <li>GAAP Compliance</li>
          <li>Audit Support</li>
          <li>Financial Reporting</li>
        </ul>
      </div>
      <div class="pillar reveal">
        <div class="tag">03 &middot; Oversight</div>
        <h3>Controller Services</h3>
        <p>Financial oversight and process management designed to scale with your business.</p>
        <ul>
          <li>Cash Flow Monitoring</li>
          <li>Budget vs. Actual Reporting</li>
          <li>KPI &amp; SaaS Metrics Reporting</li>
          <li>Financial Process Improvement</li>
          <li>Internal Controls</li>
          <li>Board Reporting Support</li>
          <li>Audit Readiness</li>
          <li>Accounting Team Management</li>
          <li>Strategic Accounting Guidance</li>
        </ul>
      </div>
    </div>
    <div class="reveal" style="text-align:center">
      <a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener">Schedule a call</a>
    </div>
  </div>
</section>

{TESTI_REEL}

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Software we know</span>
      <h2>Certified <em>experts</em> in the finance tools that power modern businesses</h2>
    </div>
    <div class="tools-grid reveal">
      <div class="tool"><img src="assets/logos/quickbooks.svg" alt="QuickBooks logo" loading="lazy"><small>QuickBooks</small></div>
      <div class="tool"><span class="wordmark">NetSuite</span><small>Oracle NetSuite</small></div>
      <div class="tool"><img src="assets/logos/xero.svg" alt="Xero logo" loading="lazy"><small>Xero</small></div>
      <div class="tool"><img src="assets/logos/sage.svg" alt="Sage logo" loading="lazy"><small>Sage Intacct</small></div>
      <div class="tool"><img src="assets/logos/brex.svg" alt="Brex logo" loading="lazy"><small>Brex</small></div>
      <div class="tool"><span class="wordmark">ramp</span><small>Ramp</small></div>
      <div class="tool"><span class="wordmark">BILL</span><small>BILL</small></div>
      <div class="tool"><img src="assets/logos/gusto.svg" alt="Gusto logo" loading="lazy"><small>Gusto</small></div>
      <div class="tool"><img src="assets/logos/zoho.svg" alt="Zoho logo" loading="lazy"><small>Zoho</small></div>
      <div class="tool"><img src="assets/logos/expensify.svg" alt="Expensify logo" loading="lazy"><small>Expensify</small></div>
      <div class="tool"><img src="assets/logos/adp.svg" alt="ADP logo" loading="lazy"><small>ADP</small></div>
      <div class="tool"><span class="wordmark">TriNet</span><small>TriNet</small></div>
    </div>
  </div>
</section>

""")

# ---------------- SERVICES ----------------
pages["services.html"] = dict(
    title="Services | Sandhill HQ - Outsourced Accounting & Finance",
    desc="Bookkeeping and financial operations, GAAP accounting and reporting, and controller services for SaaS startups and growing businesses.",
    active="services",
    body=f"""
<section class="page-hero">
  <div class="wrap page-hero-grid">
    <div>
      <span class="eyebrow">Our services</span>
      <h1>Finance as a <em>Service</em></h1>
      <p>Three layers of support that work together as one finance function, from daily transactions to controller-level oversight. Engage the full stack or just the layer you need today, and scale as you grow.</p>
    </div>
    <img src="assets/dashboard-1.jpg" alt="Financial dashboard with cash flow, revenue, and reporting on a laptop beside a Sandhill notebook" width="1400" height="1051" loading="eager">
  </div>
</section>

<section class="section services-bg" style="padding-top:64px">
  <div class="wrap">
    <div class="pillars">
      <div class="pillar reveal" id="bookkeeping">
        <div class="tag">01 &middot; Foundation</div>
        <h3>Bookkeeping &amp; Operations</h3>
        <p>The day-to-day financial foundation that keeps your business running smoothly: every transaction captured, categorized, and reconciled, every vendor and bill handled on time.</p>
        <ul>
          <li>Accounts Payable (AP)</li>
          <li>Accounts Receivable (AR)</li>
          <li>Payroll Administration</li>
          <li>Expense Management</li>
          <li>Bank &amp; Credit Card Reconciliations</li>
          <li>Sales Tax Filings</li>
          <li>Vendor Management</li>
          <li>Financial System Implementation</li>
          <li>Transaction Categorization</li>
        </ul>
      </div>
      <div class="pillar reveal" id="accounting">
        <div class="tag">02 &middot; Clarity</div>
        <h3>Accounting &amp; Reporting</h3>
        <p>Accurate, GAAP-compliant financial reporting built to support growth and decision-making, built to hold up under investor, lender, and auditor scrutiny.</p>
        <ul>
          <li>Monthly Financial Statements</li>
          <li>Month-End Close</li>
          <li>Accrual Accounting</li>
          <li>Revenue Recognition (ASC 606)</li>
          <li>Journal Entries &amp; Adjustments</li>
          <li>General Ledger Management</li>
          <li>Fixed Asset Accounting</li>
          <li>GAAP Compliance</li>
          <li>Audit Support</li>
          <li>Financial Reporting</li>
        </ul>
      </div>
      <div class="pillar reveal" id="controller">
        <div class="tag">03 &middot; Oversight</div>
        <h3>Controller Services</h3>
        <p>Financial oversight and process management designed to scale with your business: the controller-level judgment growing companies need without the full-time hire.</p>
        <ul>
          <li>Cash Flow Monitoring</li>
          <li>Budget vs. Actual Reporting</li>
          <li>KPI &amp; SaaS Metrics Reporting</li>
          <li>Financial Process Improvement</li>
          <li>Internal Controls</li>
          <li>Board Reporting Support</li>
          <li>Audit Readiness</li>
          <li>Accounting Team Management</li>
          <li>Strategic Accounting Guidance</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">How we work</span>
      <h2>Getting started is <em>simple</em></h2>
    </div>
    <div class="steps">
      <div class="step reveal">
        <div class="num">Step 01</div>
        <h3>Discovery &amp; Assessment</h3>
        <p>We start with a call to understand your business, your current setup, and where the gaps are, then review your books and systems to scope the right level of support.</p>
      </div>
      <div class="step reveal">
        <div class="num">Step 02</div>
        <h3>Cleanup &amp; Onboarding</h3>
        <p>We get your books current and accurate, implement or optimize your financial systems, and establish the processes for a reliable monthly rhythm.</p>
      </div>
      <div class="step reveal">
        <div class="num">Step 03</div>
        <h3>Ongoing Partnership</h3>
        <p>Your finance function runs on schedule: transactions handled daily, books closed monthly, reporting delivered consistently, and controller-level guidance whenever you need it.</p>
      </div>
    </div>
  </div>
</section>

<section class="strip">
  <div class="wrap" style="display:flex;flex-wrap:wrap;gap:28px;align-items:center;justify-content:space-between">
    <h2 class="reveal" style="max-width:22ch">Not sure which level of support you need?</h2>
    <a class="btn btn-sand reveal" href="{CAL}" target="_blank" rel="noopener">Schedule a call</a>
  </div>
</section>
""")

# ---------------- WHO WE HELP ----------------
pages["faq.html"] = dict(
    title="FAQ | Sandhill HQ",
    desc="Sandhill HQ works with SaaS companies, tech startups, professional service firms, and founder-led businesses. Answers to common questions about outsourced accounting.",
    active="who",
    body="""
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h1><em>Questions?</em> We're glad you asked.</h1>
    <p>We work with startups, SaaS companies, professional service firms, and growing businesses that need reliable accounting, financial reporting, and strategic financial oversight.</p>
  </div>
</section>

<section class="section" style="padding-top:32px">
  <div class="wrap">
    <div class="faq-list">
      <details class="reveal" open>
        <summary>What types of businesses do you work with?</summary>
        <p>We work with startups, SaaS companies, professional service firms, and growing businesses that need reliable accounting, financial reporting, and strategic financial oversight.</p>
      </details>
      <details class="reveal">
        <summary>Do you specialize in SaaS accounting?</summary>
        <p>Yes. We support SaaS companies with subscription-based business models, including revenue recognition (ASC 606), deferred revenue, recurring revenue reporting, and SaaS-specific metrics.</p>
      </details>
      <details class="reveal">
        <summary>What accounting software do you support?</summary>
        <p>Our team has experience with leading financial platforms including QuickBooks Online, NetSuite, Sage Intacct, Xero, BILL, Ramp, Brex, and Gusto. We are also certified in these software programs.</p>
      </details>
      <details class="reveal">
        <summary>Can you handle ASC 606 revenue recognition?</summary>
        <p>Yes. We help companies implement and maintain ASC 606-compliant revenue recognition processes to ensure accurate financial reporting and audit readiness.</p>
      </details>
      <details class="reveal">
        <summary>Can you replace an internal accounting hire?</summary>
        <p>Many of our clients use Sandhill as their outsourced accounting department. Our team provides bookkeeping, accounting, and controller-level support without the cost and complexity of building an internal finance team.</p>
      </details>
      <details class="reveal">
        <summary>Do you work with my existing CPA or tax firm?</summary>
        <p>Absolutely. We regularly collaborate with tax professionals, auditors, and fractional CFOs to ensure everyone has the information they need.</p>
      </details>
      <details class="reveal">
        <summary>Why outsource accounting instead of hiring internally?</summary>
        <p>Outsourcing provides access to specialized expertise, built-in continuity, and a scalable support model. Rather than relying on a single hire, you gain an experienced team capable of supporting your business through every stage of growth.</p>
      </details>
    </div>
  </div>
</section>
""")

# ---------------- ABOUT ----------------
pages["about.html"] = dict(
    title="About Us | Sandhill HQ",
    desc="Sandhill was founded to give growing companies the expertise, structure, and financial oversight they need, without the cost and complexity of an internal accounting department.",
    active="about",
    body="""
<section class="page-hero center">
  <div class="wrap">
    <span class="eyebrow">About us</span>
    <h1 class="h1-sm">Meet your finance &amp; accounting <em>team</em></h1>
  </div>
</section>

<section class="strip strip-light">
  <div class="wrap strip-grid">
    <div>
      <span class="eyebrow">Who we are</span>
      <p class="statement reveal">As businesses grow, so do the demands on their accounting function. Sandhill was founded to provide companies with the expertise, structure, and financial oversight they need, without the cost and complexity of building an internal accounting department.</p>
      <p class="reveal" style="max-width:60ch;margin-top:24px;color:rgba(21,27,43,.75)">Our team brings specialized expertise to every layer of the accounting function, from day-to-day bookkeeping to controller-level oversight.</p>
    </div>
    <figure class="team-photo team-photo-side reveal">
      <img src="assets/team.jpg" alt="The Sandhill HQ team of three accounting professionals" width="1000" height="854" loading="lazy">
      <figcaption>The Sandhill HQ Team</figcaption>
    </figure>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">From the founder</span>
      <h2>Why Sandhill <em>exists</em></h2>
    </div>
    <div class="founder-grid">
    <figure class="team-photo founder-photo reveal">
      <img src="assets/founder.jpg" alt="Star, Founder and Outsourced Controller of Sandhill HQ" width="800" height="1200" loading="lazy">
      <figcaption>Star, Founder &amp; Outsourced Controller</figcaption>
    </figure>
    <div class="founder reveal">
      <p>After years supporting the accounting for growing businesses at a CPA firm and then in corporate finance, I saw firsthand the back-office challenges companies face as they scale. Many had outgrown basic bookkeeping but weren't ready for a full internal finance team. Sandhill was built to bridge that gap by providing experienced accounting professionals who become an extension of each client's business.</p>
      <p>That's why I founded Sandhill.</p>
      <p>Today, I work closely with every client to ensure they receive not only accurate accounting, but a trusted partner who understands their business and is invested in their long-term success.</p>
      <p class="sig">Star, Founder &amp; Outsourced Controller</p>
    </div>
    </div>
  </div>
</section>
""")

# ---------------- BLOG INDEX ----------------
pages["blog.html"] = dict(
    title="Insights & Resources | Sandhill HQ",
    desc="Practical accounting and finance guidance for SaaS founders and growing businesses, from the Sandhill HQ team.",
    active="blog",
    body="""
<section class="page-hero">
  <div class="wrap page-hero-grid">
    <div>
      <span class="eyebrow">Insights &amp; resources</span>
      <h1>From the Sandhill <em>desk</em></h1>
      <p>Practical accounting and finance guidance for founders, written from the trenches, not the textbook.</p>
    </div>
    <img src="assets/dashboard-2.jpg" alt="Financial performance dashboard with revenue and profit charts on a laptop" width="1400" height="1050" loading="eager">
  </div>
</section>

<section class="section services-bg" style="padding-top:64px">
  <div class="wrap">
    <div class="posts">
      <a class="post reveal" href="blog/cash-vs-accrual-accounting.html">
        <span class="cat">GAAP Accounting</span>
        <h3>Cash vs. Accrual Accounting: Why the Switch Hurts and How to Get Ahead of It</h3>
        <span class="date">June 22, 2026</span>
        <span class="read">Read article &rarr;</span>
      </a>
      <a class="post reveal" href="blog/asc-606-saas-revenue-recognition.html">
        <span class="cat">GAAP Accounting</span>
        <h3>ASC 606 and SaaS: What Startup Founders Actually Need to Know about Recognizing Revenue</h3>
        <span class="date">February 10, 2026</span>
        <span class="read">Read article &rarr;</span>
      </a>
    </div>
  </div>
</section>
""")

RM_GATE_JS = """<script>
(function(){
  var f=document.getElementById('rmForm');
  if(!f)return;
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var email=f.email.value;
    var btn=document.getElementById('rmBtn');
    btn.disabled=true;btn.textContent='One moment...';
    function done(){
      f.hidden=true;
      var n=document.getElementById('rmGateNote'); if(n)n.hidden=true;
      document.getElementById('rmDone').hidden=false;
      var a=document.createElement('a');
      a.href='assets/sandhill-founders-finance-roadmap.pdf';a.download='';
      document.body.appendChild(a);a.click();a.remove();
    }
    fetch('https://formsubmit.co/ajax/star@sandhillhq.com',{
      method:'POST',
      headers:{'Content-Type':'application/json','Accept':'application/json'},
      body:JSON.stringify({
        email:email,
        _subject:'New Roadmap download on sandhillhq.com',
        message:'This email just downloaded the Founders Finance Roadmap: '+email,
        _template:'table'
      })
    }).then(done).catch(done);
  });
})();
</script>"""

pages["roadmap.html"] = dict(
    title="The Founder's Finance Roadmap | Sandhill HQ",
    desc="A free two-page roadmap for founders: what to have in place at every stage of growth, the reports that matter, and the benchmarks worth watching. From Sandhill HQ.",
    active="roadmap",
    body=f"""
<section class="page-hero">
  <div class="wrap page-hero-grid">
    <div>
      <span class="eyebrow">Free resource</span>
      <h1>The Founder's Finance <em>Roadmap</em></h1>
      <p>What to have in place at every stage of growth, from first dollar to investor-ready. A two-page reference built for founders: the checklist for each stage, the reports that matter, and the benchmarks worth watching.</p>
      <div id="get-roadmap" style="margin-top:32px">
        <form id="rmForm" class="rm-gate">
          <input type="email" name="email" required placeholder="you@company.com" aria-label="Work email">
          <button id="rmBtn" class="btn btn-primary" type="submit">Get the roadmap (PDF)</button>
        </form>
        <p class="rm-gate-note" id="rmGateNote">Enter your email and the download starts instantly.</p>
        <div id="rmDone" hidden><p class="rm-gate-done">Your download is starting. <a href="assets/sandhill-founders-finance-roadmap.pdf" download>Click here</a> if it doesn't.</p></div>
      </div>
{RM_GATE_JS}
    </div>
    <div class="rm-cover reveal">
      <div class="rm-cover-card">
        <span>SANDHILL HQ &middot; FINANCE AS A SERVICE</span>
        <strong>The Founder's Finance Roadmap</strong>
        <div class="rm-cover-stages"><b>01</b> Foundation &middot; <b>02</b> Traction &middot; <b>03</b> Growth &middot; <b>04</b> Scale</div>
      </div>
    </div>
  </div>
</section>

<section class="section services-bg" style="padding-top:64px">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">The four stages</span>
      <h2>Where are <em>you</em> on the roadmap?</h2>
    </div>
    <div class="rm-grid">
      <div class="pillar reveal">
        <div class="tag">01 &middot; Foundation &middot; Pre-revenue to first customers</div>
        <h3>Build a foundation clean enough that growth never means cleanup</h3>
        <ul>
          <li>Separate business banking and credit</li>
          <li>Entity, EIN, and state registrations in order</li>
          <li>Accounting system set up correctly from day one</li>
          <li>Books reconciled monthly, not at tax time</li>
          <li>Runway and burn tracked every month</li>
        </ul>
        <a class="rm-tie" href="services.html#bookkeeping">Sandhill covers this: Bookkeeping &amp; Operations &rarr;</a>
      </div>
      <div class="pillar reveal">
        <div class="tag">02 &middot; Traction &middot; Early revenue to $1M ARR</div>
        <h3>Know your numbers well enough to trust them</h3>
        <ul>
          <li>Monthly close, done on a schedule</li>
          <li>Payroll and contractor compliance (W-2 vs. 1099)</li>
          <li>Sales tax nexus reviewed as you sell across states</li>
          <li>Deferred revenue tracked, not lumped into income</li>
          <li>Baseline unit economics: gross margin and CAC</li>
        </ul>
        <a class="rm-tie" href="services.html#accounting">Sandhill covers this: Accounting &amp; Reporting &rarr;</a>
      </div>
      <div class="pillar reveal">
        <div class="tag">03 &middot; Growth &middot; $1M to $5M ARR</div>
        <h3>Financials that drive decisions, not just tax returns</h3>
        <ul>
          <li>Move from cash to accrual accounting</li>
          <li>Revenue recognition aligned to ASC 606</li>
          <li>Budget vs. actual reporting, reviewed monthly</li>
          <li>SaaS metrics: NRR, churn, burn multiple, LTV:CAC</li>
          <li>A documented month-end close process</li>
        </ul>
        <a class="rm-tie" href="services.html#accounting">Sandhill covers this: Accounting &amp; Controller support &rarr;</a>
      </div>
      <div class="pillar reveal">
        <div class="tag">04 &middot; Scale &middot; $5M+ or raising capital</div>
        <h3>Numbers that stand up to diligence</h3>
        <ul>
          <li>GAAP-compliant financial statements</li>
          <li>Audit-ready support and documentation</li>
          <li>Board-ready monthly reporting package</li>
          <li>Forecasting and scenario modeling</li>
          <li>Data room prepared for due diligence</li>
        </ul>
        <a class="rm-tie" href="services.html#controller">Sandhill covers this: Controller Services &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">From page two</span>
      <h2>The metrics worth <em>benchmarking</em></h2>
      <p style="max-width:56ch;margin:18px auto 0;color:rgba(21,27,43,.72)">If these aren't on a dashboard somewhere, they're running your business without you. The full roadmap includes the complete reporting stack for every stage.</p>
    </div>
    <div class="rm-table-wrap reveal">
      <table class="rm-table">
        <thead><tr><th>Metric</th><th>What it tells you</th><th>Healthy target</th></tr></thead>
        <tbody>
          <tr><td>Gross margin</td><td>Whether the product can fund growth</td><td>70&ndash;80%+</td></tr>
          <tr><td>Net revenue retention</td><td>Growth from customers you already have</td><td>100%+ &middot; best-in-class 110%+</td></tr>
          <tr><td>CAC payback period</td><td>How fast sales &amp; marketing pays for itself</td><td>Under 12&ndash;18 months</td></tr>
          <tr><td>LTV : CAC</td><td>Return on acquiring a customer</td><td>3:1 or better</td></tr>
          <tr><td>Burn multiple</td><td>Cash burned per $1 of net new ARR</td><td>Under 2x &middot; elite under 1x</td></tr>
          <tr><td>Rule of 40</td><td>Balance of growth and profitability</td><td>Growth % + margin % &ge; 40</td></tr>
          <tr><td>Runway</td><td>Months of cash at current burn</td><td>12&ndash;18+ months</td></tr>
        </tbody>
      </table>
    </div>
    <p class="reveal" style="text-align:center;font-size:13.5px;color:rgba(21,27,43,.55);margin-top:16px">Benchmarks are directional and vary by stage, market, and model. The point is to know yours and watch the trend.</p>
    <div class="reveal" style="text-align:center;margin-top:36px">
      <a class="btn btn-primary" href="#get-roadmap">Get the full roadmap (PDF)</a>
    </div>
  </div>
</section>

<section class="strip">
  <div class="wrap" style="display:flex;flex-wrap:wrap;gap:28px;align-items:center;justify-content:space-between">
    <h2 class="reveal" style="max-width:24ch">Wherever you are on the roadmap, you don't have to build the finance function alone</h2>
    <a class="btn btn-sand reveal" href="{CAL}" target="_blank" rel="noopener">Schedule a call</a>
  </div>
</section>
""")

# ---------------- CONTACT ----------------
pages["contact.html"] = dict(
    title="Contact Us | Sandhill HQ",
    desc="Get in touch with Sandhill HQ. Schedule a call to talk through your accounting and finance needs.",
    active="",
    body=f"""
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Contact</span>
    <h1>Let's <em>talk</em></h1>
    <p>The fastest way to reach us is to book time directly on our calendar. Prefer email? Send us a note and we'll get back to you within 1&ndash;2 business days.</p>
  </div>
</section>

<section class="section" style="padding-top:32px">
  <div class="wrap">
    <div class="contact-grid">
      <div class="contact-card reveal">
        <h3>Schedule a call</h3>
        <p>Pick a time that works for you and we'll talk through your current setup, your goals, and whether we're the right fit. No pressure, no obligation.</p>
        <a class="btn btn-primary" href="{CAL}" target="_blank" rel="noopener">Book a time &rarr;</a>
        <p style="margin:22px 0 0">Prefer email? Write to us at <a href="mailto:info@sandhillhq.com" style="color:var(--navy);font-weight:600;text-decoration:underline">info@sandhillhq.com</a></p>
      </div>
      <div class="contact-card reveal">
        <h3>What to expect</h3>
        <div class="detail">A 30-minute conversation about your business</div>
        <div class="detail">An honest assessment of what support you need</div>
        <div class="detail">A clear proposal if we're a good fit</div>
        <div class="detail">Referrals to trusted partners if we're not</div>
      </div>
    </div>
  </div>
</section>
""")

# ---------------- LEGAL ----------------
pages["legal.html"] = dict(
    title="Legal | Sandhill HQ",
    desc="Legal information, terms of use, and privacy policy for Sandhill HQ.",
    active="",
    body="""
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Legal</span>
    <h1>Terms &amp; <em>privacy</em></h1>
  </div>
</section>

<section class="article" style="padding-top:0">
  <div class="wrap-narrow">
    <h2>Terms of Use</h2>
    <p>The content on this website is provided for general informational purposes only and does not constitute accounting, tax, legal, or investment advice. You should consult a qualified professional regarding your specific circumstances before making financial decisions.</p>
    <h2>Privacy</h2>
    <p>This website does not use tracking cookies and does not collect personal information unless you choose to contact us. Information you share with us in the course of an inquiry or engagement is kept confidential and is never sold to third parties.</p>
    <h2>Contact</h2>
    <p>Questions about these terms? <a href="contact.html" style="text-decoration:underline">Contact us</a>.</p>
  </div>
</section>
""")

# ---------------- 404 ----------------
pages["404.html"] = dict(
    title="Page Not Found | Sandhill HQ",
    desc="The page you're looking for doesn't exist.",
    active="",
    body="""
<section class="page-hero" style="padding:140px 0 120px;text-align:center">
  <div class="wrap">
    <span class="eyebrow" style="justify-content:center">404</span>
    <h1 style="margin:0 auto">This page doesn't <em>reconcile</em></h1>
    <p style="margin:24px auto 36px">The page you're looking for doesn't exist or has moved. Let's get you back on the books.</p>
    <a class="btn btn-primary" href="/Sandhill/">Back to home</a>
  </div>
</section>
""")

# ---------------- ARTICLE: ASC 606 ----------------
ASC = """
<div class="article-head">
  <div class="wrap-narrow">
    <span class="cat">GAAP Accounting</span>
    <h1>ASC 606 and SaaS: What Startup Founders Actually Need to Know about Recognizing Revenue</h1>
    <div class="date">February 10, 2026 &middot; Sandhill HQ</div>
  </div>
</div>
<article class="article">
  <div class="wrap-narrow">
    <p class="lead">Most SaaS founders hear "ASC 606" for the first time from an auditor, a VC in due diligence, or an acquirer's finance team. By then, the scramble to clean things up is expensive, stressful, and avoidable.</p>
    <p>Here's what you should understand before you get there.</p>

    <h2>What ASC 606 Actually Is</h2>
    <p>ASC 606 is the revenue recognition standard that governs when and how companies can record revenue. For SaaS businesses, this matters enormously because the timing of when you <em>receive cash</em> and when you can <em>recognize revenue</em> are often very different things.</p>
    <p>The standard is built around a single principle: <strong>recognize revenue when you transfer control of a promised good or service to a customer, in an amount that reflects what you're entitled to receive in exchange.</strong></p>
    <p>In practice, this plays out through a five-step framework:</p>
    <ol>
      <li>Identify the contract with a customer</li>
      <li>Identify the performance obligations in the contract</li>
      <li>Determine the transaction price</li>
      <li>Allocate the transaction price to the performance obligations</li>
      <li>Recognize revenue when (or as) each obligation is satisfied</li>
    </ol>
    <p>For a pure subscription SaaS business with a simple monthly plan, this isn't complicated. But SaaS models rarely stay simple.</p>

    <h2>Where It Gets Complicated for SaaS</h2>
    <h3>1. Bundled Offerings and Performance Obligations</h3>
    <p>If your contract includes a subscription <em>plus</em> implementation services, onboarding, training, or professional services, you likely have multiple performance obligations. Each one needs to be identified separately, priced on a standalone basis (what you'd charge for it alone), and recognized on its own timeline.</p>
    <p>Lumping it all together as one revenue stream is one of the most common errors we see, and it's exactly what auditors look for.</p>
    <h3>2. Annual vs. Monthly Contracts</h3>
    <p>If a customer pays you $12,000 upfront for an annual subscription, you can't recognize all $12,000 on day one. That cash sits on your balance sheet as <strong>deferred revenue</strong>, a liability, and gets recognized ratably as you deliver the service each month ($1,000/month over 12 months).</p>
    <p>This is why your cash flow and your revenue on the income statement can look dramatically different, and why investors who understand SaaS metrics pay close attention to deferred revenue trends.</p>
    <h3>3. Variable Consideration</h3>
    <p>Usage-based pricing, volume discounts, credits, refunds, and performance bonuses all create variable consideration. Under ASC 606, you can only include variable amounts in your transaction price to the extent it's highly probable that a significant revenue reversal won't occur. This requires estimates and documentation, not guesswork.</p>
    <h3>4. Contract Modifications</h3>
    <p>When a customer upgrades, downgrades, or adds seats mid-contract, you have a contract modification. The accounting treatment depends on whether the modification is effectively a new contract or a continuation of the old one. This is an area where getting it wrong is easy and the downstream effects on your financials can compound quickly.</p>
    <h3>5. Free Trials and Discounts</h3>
    <p>Extended free trials or deeply discounted intro periods can create a material right: essentially an option the customer has to purchase future services at a discount. Material rights are their own performance obligation under ASC 606 and need to be accounted for accordingly.</p>

    <h2>The SaaS Metrics That Depend on Getting This Right</h2>
    <p>Your revenue recognition policy directly affects how your financials read to investors, lenders, and acquirers. If your ARR, MRR, and recognized revenue don't tell a coherent story, the credibility of your entire financial model comes into question.</p>
    <p>A few places where messy ASC 606 treatment shows up:</p>
    <ul>
      <li><strong>Deferred revenue</strong> that doesn't reconcile to your subscription data</li>
      <li><strong>Revenue spikes</strong> around contract start dates that don't reflect economic reality</li>
      <li><strong>Gross margin</strong> that looks artificially high or low depending on where you're booking implementation costs</li>
      <li><strong>Churn metrics</strong> that conflict with what your income statement shows</li>
    </ul>
    <p>In a fundraise or M&amp;A process, a financial diligence team will reconstruct your revenue recognition from contracts. If your books don't hold up, you're looking at restatements, re-audits, or a reduction in your valuation multiple. None of those are cheap.</p>

    <h2>When You Need to Start Caring About This</h2>
    <p>The honest answer: earlier than you think.</p>
    <ul>
      <li><strong>Pre-revenue:</strong> Structure your contracts and pricing with recognition in mind. A few intentional decisions now will save significant cleanup costs later.</li>
      <li><strong>Seed to Series A:</strong> At minimum, have clean, consistent policies documented and applied. Your first audit will test them.</li>
      <li><strong>Series A and beyond:</strong> You need a formal revenue recognition policy, a methodology for each contract type, and ideally automation or tooling that tracks performance obligation satisfaction.</li>
      <li><strong>Preparing for exit:</strong> Any sophisticated buyer or their auditors will reconstruct your revenue recognition from the contract level. Your job is to make sure what they find matches your books.</li>
    </ul>

    <h2>What Good Looks Like</h2>
    <p>A well-run SaaS finance function has:</p>
    <ul>
      <li>A <strong>written revenue recognition policy</strong> aligned to ASC 606</li>
      <li>A <strong>contract review process</strong> that flags non-standard terms before they create accounting complexity</li>
      <li>Clean separation of <strong>deferred revenue by cohort</strong> so you can track and project recognition schedules</li>
      <li><strong>Reconciliation between your billing system and your books</strong>, every month, not just at audit time</li>
      <li>Documentation for any estimates (variable consideration, standalone selling prices, etc.)</li>
    </ul>

    <h2>A Note on Tools</h2>
    <p>Revenue recognition automation tools (Maxio, Zuora Revenue, and others) can help as you scale, but they're not a substitute for understanding the underlying accounting. We've seen companies implement expensive tools on top of incorrect policies and end up with very elegant, very wrong financials.</p>
    <p>Get the policy right first. Then automate it.</p>

    <h2>The Bottom Line</h2>
    <p>ASC 606 exists because the old rules allowed too much discretion in timing revenue, and that discretion got abused. The current standard is more principles-based, which means it requires judgment, and documentation of that judgment.</p>
    <p>For SaaS founders, the goal isn't to become an expert in the standard. It's to understand enough to ask the right questions of your finance team, structure your contracts thoughtfully, and avoid the expensive surprises that come from treating revenue recognition as someone else's problem.</p>
    <p>It isn't. It's yours.</p>
    <div class="outro">Sandhill HQ helps SaaS companies build the financial infrastructure to grow with confidence. If you're approaching your first audit or preparing for a fundraise and want a second set of eyes on your revenue recognition setup we would love to help!</div>

    <h2 style="margin-top:64px">Read more</h2>
    <div class="posts">
      <a class="post" href="cash-vs-accrual-accounting.html">
        <span class="cat">GAAP Accounting</span>
        <h3>Cash vs. Accrual Accounting: Why the Switch Hurts and How to Get Ahead of It</h3>
        <span class="read">Read article &rarr;</span>
      </a>
    </div>
  </div>
</article>
"""

# ---------------- ARTICLE: CASH VS ACCRUAL ----------------
CVA = """
<div class="article-head">
  <div class="wrap-narrow">
    <span class="cat">GAAP Accounting</span>
    <h1>Cash vs. Accrual Accounting: Why the Switch Hurts and How to Get Ahead of It</h1>
    <div class="date">June 22, 2026 &middot; Sandhill HQ</div>
  </div>
</div>
<article class="article">
  <div class="wrap-narrow">
    <p class="lead">Most SaaS founders start with cash basis accounting because their bookkeeper set it up that way, or because it felt intuitive. Cash in, cash out. Easy to follow, easy to explain.</p>
    <p>Then a Series A investor asks for GAAP financials, or an acquirer requests audited statements, and suddenly "easy" becomes a six-figure cleanup project.</p>
    <p>Here's what you need to understand before you get there.</p>

    <h2>The Core Difference</h2>
    <p><strong>Cash basis accounting</strong> records revenue when you receive payment and expenses when you actually pay them. If a customer wires you $12,000 in January for an annual subscription, you record $12,000 of revenue in January.</p>
    <p><strong>Accrual basis accounting</strong> records revenue when it's earned and expenses when they're incurred, regardless of when cash moves. That same $12,000 annual subscription gets recognized at $1,000 per month as you deliver the service.</p>
    <p>The difference sounds administrative. It isn't. It fundamentally changes what your financials show and how your business looks to anyone evaluating it.</p>

    <h2>Why Founders Default to Cash Basis</h2>
    <p>Cash basis is simpler to maintain, easier to reconcile to your bank account, and perfectly adequate when you're early and small. If you're pre-revenue or just getting started, it doesn't create meaningful distortion.</p>
    <p>The IRS also allows cash basis for businesses under certain revenue thresholds, which means many early-stage companies end up on it by default, set up by a bookkeeper optimizing for tax simplicity rather than investor readiness.</p>
    <p>None of that is wrong. The problem is staying on cash basis too long.</p>

    <h2>Where Cash Basis Breaks Down for SaaS</h2>
    <h3>Your Revenue Isn't What Your Bank Account Says</h3>
    <p>When a customer pays you annually upfront, cash basis makes that month look exceptionally strong. The following 11 months look artificially weak. Your revenue chart becomes a series of spikes and valleys that reflect billing cycles rather than business performance.</p>
    <p>Investors and operators looking at your financials can't distinguish growth from billing timing noise, and neither can you.</p>
    <h3>Your Expenses Don't Match Your Revenue</h3>
    <p>Under cash basis, if you prepay for annual software licenses or pay a contractor for a six-month project upfront, that entire cost hits your books immediately. Your margins look terrible that month and artificially clean the next. You lose the ability to understand your true cost of delivering each dollar of revenue.</p>
    <h3>You Can't See Your Real Liabilities</h3>
    <p>Accrual accounting forces you to recognize deferred revenue, the cash you've collected but haven't yet earned, as a liability on your balance sheet. On cash basis, that obligation is invisible. You might look at your bank account and feel flush while carrying significant service delivery obligations you haven't accounted for.</p>
    <h3>GAAP Requires Accrual</h3>
    <p>Any institutional investor, lender, or acquirer will want GAAP-compliant financials. GAAP requires accrual. The longer you stay on cash basis, the more historical periods will need to be restated when you finally make the switch, and restatements are expensive, time-consuming, and occasionally embarrassing.</p>

    <h2>The Real Cost of Switching Late</h2>
    <p>The transition from cash to accrual isn't just a settings change in QuickBooks. It requires:</p>
    <ul>
      <li>Reconstructing deferred revenue balances from historical contracts</li>
      <li>Identifying and properly accruing unpaid expenses and prepaid assets</li>
      <li>Restating prior period financials if lenders or investors need comparative data</li>
      <li>Potentially re-filing taxes depending on the IRS method change rules (Form 3115)</li>
    </ul>
    <p>For a company that's been on cash basis for three or four years with hundreds of contracts, this can run tens of thousands of dollars in accounting fees, and that's before the audit. We've seen it delay fundraising closes and create last-minute surprises in M&amp;A diligence.</p>
    <p>The earlier you make the switch, the cheaper and cleaner it is.</p>

    <h2>When to Make the Move</h2>
    <p>There's no universal trigger, but here are the moments when staying on cash basis starts costing you more than it saves:</p>
    <ul>
      <li><strong>You're approaching your first institutional raise.</strong> Investors will want GAAP financials, and you want time to clean things up before you're under the pressure of a live deal.</li>
      <li><strong>You're hitting $1&ndash;2M ARR.</strong> At this scale, billing timing distortions start to meaningfully obscure your financial picture.</li>
      <li><strong>You're adding complexity.</strong> Multi-year contracts, implementation fees, usage-based components, or significant prepaid expenses all create scenarios where cash basis gives you a misleading view.</li>
      <li><strong>You're planning to hire finance leadership.</strong> Any experienced CFO or Controller will want to operate on accrual. Don't hand them a cleanup project on day one.</li>
    </ul>

    <h2>What Accrual Unlocks</h2>
    <p>Beyond compliance, accrual accounting gives you a cleaner operating picture:</p>
    <ul>
      <li><strong>Gross margin by cohort</strong>: you can see what it actually costs to serve each customer segment</li>
      <li><strong>Accurate MRR/ARR</strong>: recognized revenue that reconciles to your subscription data</li>
      <li><strong>Deferred revenue trends</strong>: a leading indicator of future recognized revenue and a signal investors pay attention to</li>
      <li><strong>Expense matching</strong>: costs aligned to the period they support, so you can evaluate ROI on spend decisions</li>
    </ul>
    <p>In short, accrual accounting gives you financials you can actually manage a business with, not just report to the IRS.</p>

    <h2>A Note on Hybrid Situations</h2>
    <p>Some early-stage companies run accrual for their internal management reporting while staying on cash basis for taxes. This is a legitimate approach that preserves tax simplicity while giving leadership a cleaner operating view. It requires maintaining two sets of books (or a clean reconciliation between them), but for the right company at the right stage, it's worth the effort.</p>
    <p>Talk to your accountant about whether a hybrid approach makes sense for you before making any changes.</p>

    <h2>The Bottom Line</h2>
    <p>Cash basis accounting isn't wrong, it's just limited. It works fine early, and then it stops working. The mistake most founders make is waiting until external pressure forces the switch, rather than getting ahead of it.</p>
    <p>If you're building a SaaS company with any ambition to raise institutional capital, get acquired, or simply understand your own business, you'll end up on accrual eventually. The only question is whether you make that transition on your timeline or someone else's.</p>
    <div class="outro">Sandhill HQ helps SaaS companies build the financial infrastructure to grow with confidence. If you're not sure whether your current accounting setup will hold up under investor or acquirer scrutiny, we would love to help!</div>

    <h2 style="margin-top:64px">Read more</h2>
    <div class="posts">
      <a class="post" href="asc-606-saas-revenue-recognition.html">
        <span class="cat">GAAP Accounting</span>
        <h3>ASC 606 and SaaS: What Startup Founders Actually Need to Know about Recognizing Revenue</h3>
        <span class="read">Read article &rarr;</span>
      </a>
    </div>
  </div>
</article>
"""

articles = {
    "blog/asc-606-saas-revenue-recognition.html": dict(
        title="ASC 606 and SaaS: What Startup Founders Need to Know | Sandhill HQ",
        desc="Most SaaS founders learn about ASC 606 the hard way. Here's what to know before an auditor, investor, or an acquisition forces the conversation.",
        active="blog", body=ASC),
    "blog/cash-vs-accrual-accounting.html": dict(
        title="Cash vs. Accrual Accounting for SaaS Founders | Sandhill HQ",
        desc="Cash basis is simple until it isn't. What changes with accrual accounting, why switching late is painful, and how to get ahead of it.",
        active="blog", body=CVA),
}

os.makedirs("blog", exist_ok=True)
for path, p in pages.items():
    with open(path, "w") as f:
        f.write(shell(p["title"], p["desc"], p["body"], prefix="", active=p["active"], cta_html=p.get("cta_html")))
for path, p in articles.items():
    with open(path, "w") as f:
        f.write(shell(p["title"], p["desc"], p["body"], prefix="../", active=p["active"]))
print("Generated:", ", ".join(list(pages) + list(articles)))
