#!/usr/bin/env python3
"""Builds the designed Founder's Finance Roadmap PDF (v2). Run from repo root."""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Lora', 'assets/fonts/Lora.ttf'))
pdfmetrics.registerFont(TTFont('Inter', 'assets/fonts/Inter.ttf'))

PAPER = HexColor('#FAF7F1'); NAVY = HexColor('#1E2B4F'); NAVY_D = HexColor('#131E3A')
SAND = HexColor('#C99B5F'); SAND_SOFT = HexColor('#EDE3D2'); INK = HexColor('#151B2B')
GREY = HexColor('#5A6072'); WHITE = HexColor('#FFFFFF'); LINE = HexColor('#DDD6C8')
LOGO_DARK = HexColor('#DCC8A0'); LOGO_LIGHT = HexColor('#ECDCB9')

W, H = letter
M = 44  # margin
CAL = "https://calendar.app.google/ngdhcYuakQkRgjyx5"
SITE = "https://sandhillhq.com"

c = canvas.Canvas('assets/sandhill-founders-finance-roadmap.pdf', pagesize=letter)
c.setTitle("The Founder's Finance Roadmap | Sandhill HQ")
c.setAuthor("Sandhill HQ")

def bg():
    c.setFillColor(PAPER); c.rect(0, 0, W, H, fill=1, stroke=0)

def logo(x, y, w=44):
    c.drawImage('assets/logo-mark.png', x, y, width=w, height=w*515/900, mask='auto')

def rrect(x, y, w, h, r, fill, stroke=None):
    c.setFillColor(fill)
    if stroke: c.setStrokeColor(stroke); c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, r, fill=1, stroke=1 if stroke else 0)

def text(x, y, s, font='Inter', size=9, color=INK, tracking=0):
    c.setFont(font, size); c.setFillColor(color)
    if tracking:
        cx = x
        for ch in s:
            c.drawString(cx, y, ch); cx += c.stringWidth(ch, font, size) + tracking
    else:
        c.drawString(x, y, s)

def ctext(x, y, s, font='Inter', size=9, color=INK):
    c.setFont(font, size); c.setFillColor(color); c.drawCentredString(x, y, s)

def wrap(s, font, size, maxw):
    words, lines, cur = s.split(), [], ''
    for w_ in words:
        t = (cur + ' ' + w_).strip()
        if c.stringWidth(t, font, size) <= maxw: cur = t
        else: lines.append(cur); cur = w_
    if cur: lines.append(cur)
    return lines

def checkbox(x, y, size=7):
    c.setStrokeColor(SAND); c.setLineWidth(1.1); c.setFillColor(WHITE)
    c.roundRect(x, y, size, size, 1.5, fill=1, stroke=1)

def footer_band(page_label):
    bh = 64
    c.setFillColor(NAVY_D); c.rect(0, 0, W, bh, fill=1, stroke=0)
    ctext(W/2, 40, "Wherever you are on the roadmap, you don't have to build the finance function alone.", 'Lora', 11.5, PAPER)
    line = "Sandhill HQ  ·  Bookkeeping, Accounting & Controller Services  ·  sandhillhq.com  ·  Book a call"
    ctext(W/2, 20, line, 'Inter', 8.5, HexColor('#C9AF7E'))
    lw = c.stringWidth(line, 'Inter', 8.5); x0 = W/2 - lw/2
    pre_site = "Sandhill HQ  ·  Bookkeeping, Accounting & Controller Services  ·  "
    site_s = "sandhillhq.com"
    x_site = x0 + c.stringWidth(pre_site, 'Inter', 8.5)
    c.linkURL(SITE, (x_site, 15, x_site + c.stringWidth(site_s, 'Inter', 8.5), 30), relative=0)
    pre_call = pre_site + site_s + "  ·  "
    x_call = x0 + c.stringWidth(pre_call, 'Inter', 8.5)
    c.linkURL(CAL, (x_call, 15, x0 + lw, 30), relative=0)
    text(W - M - c.stringWidth(page_label, 'Inter', 7.5), 8, page_label, 'Inter', 7.5, HexColor('#5E6B8F'))

# ================= PAGE 1 =================
bg()

# header
logo(M, H - 82, 52)
text(M + 66, H - 52, "S A N D H I L L  H Q   ·   F I N A N C E  A S  A  S E R V I C E", 'Inter', 7.5, SAND, tracking=0.4)
text(M + 66, H - 76, "The Founder's Finance Roadmap", 'Lora', 25, NAVY)
text(M, H - 102, "What to have in place at every stage of growth, from first dollar to investor-ready.", 'Inter', 10, GREY)

# diagnostic strip
dy = H - 168; dh = 52
rrect(M, dy, W - 2*M, dh, 8, SAND_SOFT)
text(M + 16, dy + dh - 18, "WHICH STAGE ARE YOU IN?", 'Inter', 8, NAVY, tracking=0.6)
opts = [("Pre-revenue", "Stage 01"), ("Under $1M ARR", "Stage 02"), ("$1M to $5M ARR", "Stage 03"), ("$5M+ or raising", "Stage 04")]
slot = (W - 2*M - 32) / 4
for i, (label, stage) in enumerate(opts):
    ox = M + 16 + i * slot
    checkbox(ox, dy + 11)
    text(ox + 12, dy + 12, label, 'Inter', 8, INK)
    lw_ = c.stringWidth(label, 'Inter', 8)
    text(ox + 12 + lw_ + 4, dy + 12, "· " + stage, 'Inter', 8, SAND)

# stage cards 2x2
stages = [
    ("01", "FOUNDATION", "PRE-REVENUE TO FIRST CUSTOMERS",
     "Build a foundation clean enough that growth never means cleanup.",
     ["Separate business banking & credit", "Entity, EIN & state registrations in order",
      "Accounting system set up correctly from day one", "Books reconciled monthly, not at tax time",
      "Runway & burn tracked every month"]),
    ("02", "TRACTION", "EARLY REVENUE TO $1M ARR",
     "Know your numbers well enough to trust them.",
     ["Monthly close, done on a schedule", "Payroll & contractor compliance (W-2 vs. 1099)",
      "Sales tax nexus reviewed as you sell across states", "Deferred revenue tracked, not lumped into income",
      "Baseline unit economics: gross margin & CAC"]),
    ("03", "GROWTH", "$1M TO $5M ARR",
     "Financials that drive decisions, not just tax returns.",
     ["Move from cash to accrual accounting", "Revenue recognition aligned to ASC 606",
      "Budget vs. actual reporting, reviewed monthly", "SaaS metrics: NRR, churn, burn multiple, LTV:CAC",
      "A documented month-end close process"]),
    ("04", "SCALE", "$5M+ OR RAISING CAPITAL",
     "Numbers that stand up to diligence.",
     ["GAAP-compliant financial statements", "Audit-ready support & documentation",
      "Board-ready monthly reporting package", "Forecasting & scenario modeling",
      "Data room prepared for due diligence"]),
]
gw = (W - 2*M - 16) / 2; gh = 196
gx0, gy0 = M, H - 188 - gh
for i, (num, name, sub, lead, items) in enumerate(stages):
    gx = gx0 + (i % 2) * (gw + 16)
    gy = gy0 - (i // 2) * (gh + 14)
    rrect(gx, gy, gw, gh, 10, WHITE, LINE)
    # number chip
    rrect(gx + 16, gy + gh - 34, 24, 18, 4, NAVY)
    ctext(gx + 28, gy + gh - 29, num, 'Inter', 9, PAPER)
    text(gx + 47, gy + gh - 29, name, 'Inter', 10.5, NAVY, tracking=0.8)
    text(gx + 16, gy + gh - 48, sub, 'Inter', 6.8, SAND, tracking=0.5)
    ly = gy + gh - 66
    for ln in wrap(lead, 'Lora', 10.5, gw - 32):
        text(gx + 16, ly, ln, 'Lora', 10.5, INK); ly -= 13
    ly -= 4
    for item in items:
        checkbox(gx + 16, ly - 1)
        lines = wrap(item, 'Inter', 8.3, gw - 44)
        text(gx + 30, ly, lines[0], 'Inter', 8.3, HexColor('#3A4058'))
        ly -= 12
        for extra in lines[1:]:
            text(gx + 30, ly, extra, 'Inter', 8.3, HexColor('#3A4058')); ly -= 12
        ly -= 3.5

# how sandhill helps strip
hy = 88; hh = 76
rrect(M, hy, W - 2*M, hh, 8, WHITE, LINE)
text(M + 16, hy + hh - 20, "HOW SANDHILL HELPS AT EVERY STAGE", 'Inter', 8, NAVY, tracking=0.6)
text(M + 16, hy + hh - 36, "Stages 01-02: Bookkeeping & Financial Operations   ·   Stages 02-03: Accounting & Reporting (ASC 606, GAAP)", 'Inter', 8.2, HexColor('#3A4058'))
text(M + 16, hy + hh - 49, "Stages 03-04: Controller Services", 'Inter', 8.2, HexColor('#3A4058'))
text(M + 16, hy + 12, "Every unchecked box on this page is something we take off a founder's plate.", 'Lora', 9.5, HexColor('#8A6A38'))

footer_band("Page 1 of 2  ·  sandhillhq.com")
c.showPage()

# ================= PAGE 2 =================
bg()
logo(M, H - 74, 42)
text(M + 56, H - 48, "S A N D H I L L  H Q   ·   F I N A N C E  A S  A  S E R V I C E", 'Inter', 7.5, SAND, tracking=0.4)
text(M + 56, H - 70, "Reports & Metrics That Matter", 'Lora', 21, NAVY)
text(M, H - 92, "The reporting stack, and the benchmarks, that separate managed finances from monitored ones.", 'Inter', 9.5, GREY)

# three report columns
cols = [
    ("THE CORE REPORTS", "Monthly, every business",
     ["P&L with budget vs. actual", "Balance sheet", "Statement of cash flows", "13-week cash forecast", "AR & AP aging"]),
    ("THE SAAS LAYER", "Monthly, recurring revenue",
     ["MRR / ARR schedule", "Deferred revenue rollforward", "Cohort & retention view", "SaaS metrics dashboard", "Pipeline-to-revenue view"]),
    ("THE BOARD LAYER", "Monthly or quarterly, funded",
     ["Board reporting package", "Variance commentary", "Rolling forecast & runway", "KPI summary vs. plan", "Cap table & headcount view"]),
]
cw = (W - 2*M - 28) / 3; ch = 148
cy = H - 110 - ch
for i, (title, sub, items) in enumerate(cols):
    cx = M + i * (cw + 14)
    rrect(cx, cy, cw, ch, 10, WHITE, LINE)
    text(cx + 14, cy + ch - 22, title, 'Inter', 8.5, NAVY, tracking=0.6)
    text(cx + 14, cy + ch - 35, sub, 'Inter', 7.2, SAND)
    ly = cy + ch - 54
    for item in items:
        checkbox(cx + 14, ly - 1, 6.5)
        text(cx + 27, ly, item, 'Inter', 8, HexColor('#3A4058'))
        ly -= 17

# metrics table
ty_top = cy - 34
text(M, ty_top, "The metrics worth benchmarking", 'Lora', 15, NAVY)
text(M, ty_top - 15, "If these aren't on a dashboard somewhere, they're running your business without you.", 'Inter', 8.5, GREY)
rows = [
    ("Gross margin", "Whether the product can fund growth", "70-80%+"),
    ("Net revenue retention", "Growth from customers you already have", "100%+ · best-in-class 110%+"),
    ("CAC payback period", "How fast sales & marketing pays for itself", "Under 12-18 months"),
    ("LTV : CAC", "Return on acquiring a customer", "3 : 1 or better"),
    ("Burn multiple", "Cash burned per $1 of net new ARR", "Under 2x · elite under 1x"),
    ("Rule of 40", "Balance of growth and profitability", "Growth % + margin % of 40+"),
    ("Runway", "Months of cash at current burn", "12-18+ months"),
]
tw = W - 2*M; rh = 23; th_ = 20
ty = ty_top - 30 - th_
col1, col2 = 130, 240
# header
c.setFillColor(SAND_SOFT); c.roundRect(M, ty, tw, th_, 6, fill=1, stroke=0)
c.rect(M, ty, tw, th_/2, fill=1, stroke=0)
text(M + 12, ty + 6, "METRIC", 'Inter', 7.5, NAVY, tracking=0.6)
text(M + 12 + col1, ty + 6, "WHAT IT TELLS YOU", 'Inter', 7.5, NAVY, tracking=0.6)
text(M + 12 + col1 + col2, ty + 6, "HEALTHY TARGET", 'Inter', 7.5, NAVY, tracking=0.6)
ry = ty
c.setFillColor(WHITE); c.rect(M, ty - len(rows)*rh, tw, len(rows)*rh, fill=1, stroke=0)
for name, what, target in rows:
    ry -= rh
    c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(M, ry + rh, M + tw, ry + rh)
    text(M + 12, ry + 6.5, name, 'Inter', 8.6, NAVY)
    text(M + 12 + col1, ry + 6.5, what, 'Inter', 8.6, HexColor('#3A4058'))
    text(M + 12 + col1 + col2, ry + 6.5, target, 'Inter', 8.6, HexColor('#8A6A38'))
c.setStrokeColor(LINE); c.setLineWidth(0.8)
c.roundRect(M, ty - len(rows)*rh, tw, len(rows)*rh + th_, 6, fill=0, stroke=1)
ctext(W/2, ty - len(rows)*rh - 16, "Benchmarks are directional and vary by stage, market, and model. The point is to know yours and watch the trend.", 'Inter', 7.8, GREY)

# closing CTA card
qy = 92; qh = 84; qw = W - 2*M
rrect(M, qy, qw, qh, 10, NAVY)
btn = "Book an intro call"
bw = c.stringWidth(btn, 'Inter', 9) + 28
text(M + 20, qy + qh - 24, "WANT THIS STACK BUILT FOR YOU?", 'Inter', 8, HexColor('#C9AF7E'), tracking=0.6)
cta_copy = "Sandhill sets up the core, SaaS, and board reporting layers as part of Finance as a Service, then runs them every month so your numbers are always current, compliant, and board-ready."
ly = qy + qh - 42
for ln in wrap(cta_copy, 'Lora', 10.5, qw - 40 - bw - 30):
    text(M + 20, ly, ln, 'Lora', 10.5, PAPER); ly -= 14
by = qy + (qh - 24) / 2
rrect(M + qw - bw - 18, by, bw, 24, 12, SAND)
ctext(M + qw - bw/2 - 18, by + 7.5, btn, 'Inter', 9, NAVY_D)
c.linkURL(CAL, (M + qw - bw - 18, by, M + qw - 18, by + 24), relative=0)

footer_band("Page 2 of 2  ·  sandhillhq.com")
c.showPage()
c.save()
print('PDF built: assets/sandhill-founders-finance-roadmap.pdf')
