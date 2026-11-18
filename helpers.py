"""Shared formatting helpers (fractions, graphs, tables, page styles) for the Talking Turkey review."""
import random, math
random.seed(1126)

def F(a, b):
    return f'<span class="fr"><span>{a}</span><span>{b}</span></span>'

M = '−'  # unicode minus

# ---------------- SVG helpers ----------------
def plane(xmin, xmax, ymin, ymax, px=220, curves=(), pts=(), labels=True):
    nx, ny = xmax - xmin, ymax - ymin
    s = px / max(nx, ny)
    w, h = nx * s, ny * s
    X = lambda x: (x - xmin) * s
    Y = lambda y: (ymax - y) * s
    o = [f'<svg class="plane" width="{w+12:.0f}" height="{h+12:.0f}" viewBox="-6 -6 {w+12:.0f} {h+12:.0f}">']
    for i in range(nx + 1):
        o.append(f'<line x1="{X(xmin+i):.1f}" y1="0" x2="{X(xmin+i):.1f}" y2="{h:.1f}" stroke="#ccc" stroke-width="0.6"/>')
    for j in range(ny + 1):
        o.append(f'<line x1="0" y1="{Y(ymin+j):.1f}" x2="{w:.1f}" y2="{Y(ymin+j):.1f}" stroke="#ccc" stroke-width="0.6"/>')
    o.append(f'<line x1="{X(0)}" y1="0" x2="{X(0)}" y2="{h}" stroke="#000" stroke-width="1.2"/>')
    o.append(f'<line x1="0" y1="{Y(0)}" x2="{w}" y2="{Y(0)}" stroke="#000" stroke-width="1.2"/>')
    for c in curves:
        d = ' '.join(f'{X(x):.1f},{Y(y):.1f}' for x, y in c)
        o.append(f'<polyline points="{d}" fill="none" stroke="#1a5fb4" stroke-width="2.2" stroke-linejoin="round"/>')
    for x, y in pts:
        o.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="3" fill="#1a5fb4"/>')
    o.append('</svg>')
    return ''.join(o)

def numline(lo=-10, hi=10, mark=None, w=300, labeled=False):
    n = hi - lo; s = (w - 20) / n
    X = lambda v: 10 + (v - lo) * s
    o = [f'<svg class="nl" width="{w}" height="38" viewBox="0 0 {w} 38">',
         f'<line x1="2" y1="14" x2="{w-2}" y2="14" stroke="#000" stroke-width="1.2"/>',
         f'<path d="M2 14 l7 -4 v8z M{w-2} 14 l-7 -4 v8z" fill="#000"/>']
    for v in range(lo, hi + 1):
        o.append(f'<line x1="{X(v):.1f}" y1="9" x2="{X(v):.1f}" y2="19" stroke="#000" stroke-width="1"/>')
        if labeled:
            o.append(f'<text x="{X(v):.1f}" y="32" font-size="10" text-anchor="middle">{str(v).replace("-", M)}</text>')
    if mark:
        for kind, a, b in mark:  # ('ray', start, direction) or ('seg', a, b)
            pass
    o.append('</svg>')
    return ''.join(o)

def numline_graph(lo, hi, segs, circles, w=300):
    """segs: list of (a,b) values, use None for arrow to end. circles: list of (v, filled)"""
    n = hi - lo; s = (w - 20) / n
    X = lambda v: 10 + (v - lo) * s
    base = numline(lo, hi, w=w, labeled=True)[:-6]
    o = [base]
    for a, b in segs:
        xa = 2 if a is None else X(a)
        xb = w - 2 if b is None else X(b)
        o.append(f'<line x1="{xa:.1f}" y1="14" x2="{xb:.1f}" y2="14" stroke="#1a5fb4" stroke-width="4"/>')
        if a is None: o.append(f'<path d="M0 14 l9 -6 v12z" fill="#1a5fb4"/>')
        if b is None: o.append(f'<path d="M{w} 14 l-9 -6 v12z" fill="#1a5fb4"/>')
    for v, filled in circles:
        o.append(f'<circle cx="{X(v):.1f}" cy="14" r="5" fill="{"#1a5fb4" if filled else "#fff"}" stroke="#1a5fb4" stroke-width="2"/>')
    o.append('</svg>')
    return ''.join(o)

def table(xs, ys):
    tx = ''.join(f'<td>{str(v).replace("-", M)}</td>' for v in xs)
    ty = ''.join(f'<td>{str(v).replace("-", M)}</td>' for v in ys)
    return f'<table class="xy"><tr><th><i>x</i></th>{tx}</tr><tr><th><i>y</i></th>{ty}</tr></table>'

def bakery_graph():
    W_, H_ = 260, 200; L, B = 40, 30
    gw, gh = W_ - L - 10, H_ - B - 10
    X = lambda x: L + x / 8 * gw
    Y = lambda y: 10 + (64 - y) / 64 * gh
    o = [f'<svg width="{W_}" height="{H_+14}" viewBox="0 0 {W_} {H_+14}" font-size="10">']
    for i in range(9):
        o.append(f'<line x1="{X(i):.1f}" y1="10" x2="{X(i):.1f}" y2="{Y(0):.1f}" stroke="#ccc"/>')
        o.append(f'<text x="{X(i):.1f}" y="{Y(0)+13:.1f}" text-anchor="middle">{i}</text>')
    for j in range(0, 65, 8):
        o.append(f'<line x1="{L}" y1="{Y(j):.1f}" x2="{X(8):.1f}" y2="{Y(j):.1f}" stroke="#ccc"/>')
        o.append(f'<text x="{L-5}" y="{Y(j)+3.5:.1f}" text-anchor="end">{j}</text>')
    o.append(f'<line x1="{L}" y1="10" x2="{L}" y2="{Y(0)}" stroke="#000" stroke-width="1.3"/>')
    o.append(f'<line x1="{L}" y1="{Y(0)}" x2="{X(8)}" y2="{Y(0)}" stroke="#000" stroke-width="1.3"/>')
    o.append(f'<line x1="{X(0)}" y1="{Y(64)}" x2="{X(8)}" y2="{Y(0)}" stroke="#1a5fb4" stroke-width="2.4"/>')
    o.append(f'<circle cx="{X(3)}" cy="{Y(40)}" r="3.5" fill="#1a5fb4"/>')
    o.append(f'<text x="{X(3)+6}" y="{Y(40)-5}" font-size="10" font-weight="bold">(3, 40)</text>')
    o.append(f'<text x="{L+gw/2}" y="{H_+12}" text-anchor="middle" font-size="11">Hours since opening</text>')
    o.append(f'<text x="11" y="{10+gh/2}" text-anchor="middle" font-size="11" transform="rotate(-90 11 {10+gh/2})">Pies left</text>')
    o.append('</svg>')
    return ''.join(o)

# ---------------- HTML ----------------
CSS = '''
@page { size: letter; margin: 0.45in 0.5in; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", "Liberation Sans", sans-serif; font-size: 10.5pt; color: #222; margin: 0; }
i { font-family: "DejaVu Serif", serif; }
.fr { display: inline-flex; flex-direction: column; vertical-align: middle; text-align: center; font-size: 0.85em; margin: 0 1px; line-height: 1.05; }
.fr > span:first-child { border-bottom: 1px solid currentColor; padding: 0 2px; }
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }
header.top { display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 3px solid #b5541c; padding-bottom: 4px; margin-bottom: 8px; }
header.top h1 { font-size: 19pt; margin: 0; color: #7a2e0e; font-family: "DejaVu Serif", serif; }
header.top .sub { font-size: 9.5pt; color: #555; }
.name { font-size: 10pt; }
.dir { background: #fdf2e4; border: 1.5px solid #e0a35c; border-radius: 8px; padding: 8px 12px; margin-bottom: 10px; font-size: 10pt; }
.dir ol { margin: 4px 0 0 0; padding-left: 20px; }
h2.unit { font-size: 12.5pt; margin: 6px 0 6px; color: #fff; background: #b5541c; padding: 3px 10px; border-radius: 5px; }
.grp { font-weight: bold; margin: 4px 0 4px; font-size: 10pt; }
.qs { display: grid; grid-template-columns: 1fr 1fr; gap: 8px 14px; }
.qbox { border: 1px solid #bbb; border-radius: 6px; padding: 6px 8px 4px; break-inside: avoid; display: flex; flex-direction: column; }
.qbox.wide { grid-column: span 2; }
.qhead { display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px; }
.qnum { font-weight: bold; background: #7a2e0e; color: #fff; border-radius: 4px; padding: 0 6px; font-size: 10pt; }
.color { font-size: 8.5pt; font-weight: bold; display: flex; align-items: center; gap: 4px; }
.sw { display: inline-block; width: 13px; height: 13px; border: 1px solid #333; border-radius: 2px; }
.extra { margin: 4px 0; }
.ans { margin-top: auto; font-size: 8.5pt; display: flex; gap: 10px; padding-top: 4px; }
.ans span.blank { border-bottom: 1px solid #333; flex: 1; }
.ans span.codeblank { border: 1px solid #333; width: 38px; height: 16px; display: inline-block; }
table.xy { border-collapse: collapse; font-size: 10pt; }
table.xy td, table.xy th { border: 1px solid #555; padding: 2px 9px; text-align: center; }
table.xy th { background: #f3e3cf; }
.bank h3 { margin: 3px 0 1px; font-size: 11pt; color: #7a2e0e; }
.bankgrid { display: grid; grid-template-columns: 1fr 1fr; gap: 0 14px; }
.bi { display: flex; gap: 8px; border-bottom: 1px dotted #bbb; padding: 0.8px 0; font-size: 8.4pt; break-inside: avoid; align-items: center; }
.bi b { font-family: "DejaVu Sans Mono", monospace; width: 26px; flex: none; color: #7a2e0e; }
table.grid { border-collapse: collapse; margin: 0 auto; }
table.grid td { border: 0.8px solid #888; width: 0.3in; height: 0.3in; text-align: center; font-size: 7.5pt; font-family: "DejaVu Sans Mono", monospace; padding: 0; }
.key table { border-collapse: collapse; width: 100%; font-size: 8pt; }
.key td, .key th { border: 1px solid #aaa; padding: 1px 4px; }
.key th { background: #f3e3cf; text-align: left; }
.small { font-size: 8.5pt; color: #555; }
'''

UNITS = {1: 'Unit 1 · Equations, Functions & Absolute Value Equations',
         2: 'Unit 2 · Inequalities',
         3: 'Unit 3 · Functions, Slope & Graphing'}

def header(title, sub):
    return (f'<header class="top"><div><h1>{title}</h1><div class="sub">{sub}</div></div>'
            f'<div class="name">Name: ______________________ &nbsp;Block: ____</div></header>')

