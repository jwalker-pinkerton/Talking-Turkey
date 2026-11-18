import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import helpers as B
F, M, plane, table, numline, numline_graph = B.F, B.M, B.plane, B.table, B.numline, B.numline_graph

random.seed(2026)
Q = []
def q(unit, prompt, answer, distract, extra='', space=80, group=None):
    Q.append(dict(unit=unit, prompt=prompt, extra=extra, answer=answer, distract=distract, space=space, group=group))

NL = numline()
FG = f'Use <i>f</i>(<i>x</i>) = 3<i>x</i> {M} 1 and <i>g</i>(<i>x</i>) = {F(1,2)}<i>x</i> + 6.'
# Unit 1
q(1, f'Simplify the expression: 4(<i>x</i> {M} 3) {M} 6<i>x</i> + 5', f'{M}2<i>x</i> {M} 7', [f'{M}2<i>x</i> + 2', f'10<i>x</i> {M} 7'])
q(1, f'{FG} Evaluate <i>g</i>(<i>f</i>(3)).', '<i>g</i>(<i>f</i>(3)) = 10', ['<i>g</i>(<i>f</i>(3)) = 8', '<i>g</i>(<i>f</i>(3)) = 21.5'])
q(1, f'Solve: 2(3<i>k</i> {M} 5) = 4(<i>k</i> + 2)', '<i>k</i> = 9', [f'<i>k</i> = {M}9', '<i>k</i> = 6.5'])
q(1, f'Solve: |<i>x</i> {M} 2| = 9', f'<i>x</i> = 11 and <i>x</i> = {M}7', [f'<i>x</i> = 11 and <i>x</i> = {M}11', f'<i>x</i> = 7 and <i>x</i> = {M}11'])
q(1, f'Solve: {M}3|2<i>x</i> + 4| + 5 = {M}13', f'<i>x</i> = 1 and <i>x</i> = {M}5', ['No solution', f'<i>x</i> = 1 and <i>x</i> = {M}1'])
q(1, 'Define the variable, write an equation, solve, and interpret your solution.<br>A caterer charges a $40 delivery fee plus $12 per guest for Thanksgiving dinner. The total bill was $256. How many guests were there?',
  'There were 18 guests', ['There were 24.67 guests', 'There were 21.3 guests'], space=95)
# Unit 2
q(2, 'Write the sentence as an inequality: The sum of a number and 9 is no more than 25.', '<i>x</i> + 9 ≤ 25', ['<i>x</i> + 9 &lt; 25', '<i>x</i> + 9 ≥ 25'], space=40)
q(2, f'Solve and graph: {M}4 {M} 3<i>x</i> &gt; 17', f'<i>x</i> &lt; {M}7', [f'<i>x</i> &gt; {M}7', f'<i>x</i> &lt; {M}4.3'], extra=NL, space=55)
q(2, f'Solve and graph: 4(<i>x</i> {M} 2) ≥ 6<i>x</i> + 4', f'<i>x</i> ≤ {M}6', [f'<i>x</i> ≥ {M}6', f'<i>x</i> ≤ {M}3'], extra=NL, space=55)
q(2, 'Write an inequality for the graph:', '<i>x</i> ≤ 1', ['<i>x</i> &lt; 1', '<i>x</i> ≥ 1'], extra=numline_graph(-6, 6, [(None, 1)], [(1, True)]), space=15)
q(2, f'Solve and graph: {M}5 ≤ 2<i>n</i> + 3 &lt; 9', f'{M}4 ≤ <i>n</i> &lt; 3', [f'{M}1 ≤ <i>n</i> &lt; 6', f'{M}8 ≤ <i>n</i> &lt; 6'], extra=NL, space=55)
q(2, 'Define the variable, write the inequality, solve, and interpret the solution.<br>Cranberry sauce costs $2.75 per can. What is the maximum number of cans you can buy with $15?',
  'You can buy at most 5 cans', ['You can buy at most 6 cans', 'You can buy at least 5 cans'], space=95)
# Unit 3
q(3, 'Is the table a function or not a function? Explain how you know.', 'Not a function; the input 1 has two outputs', ['Function; each output is different'],
  extra=table([1, 2, 3, 1], [4, 5, 6, 7]), space=35)
q(3, f'Calculate the slope: ({M}1, 4) and (3, {M}8)', f'<i>m</i> = {M}3', ['<i>m</i> = 3', f'<i>m</i> = {M}{F(1,3)}'], space=55)
q(3, 'Convert to slope-intercept form: 2<i>x</i> + 5<i>y</i> = 20', f'<i>y</i> = {M}{F(2,5)}<i>x</i> + 4', [f'<i>y</i> = {F(2,5)}<i>x</i> + 4', f'<i>y</i> = {M}{F(2,5)}<i>x</i> + 20'], space=55)
RO = 'The total cost of renting a turkey roaster is modeled by <i>y</i> = 15<i>x</i> + 20, where <i>x</i> is the number of days and <i>y</i> is the total cost in dollars.'
q(3, 'Identify <u>and</u> interpret the slope.', '<i>m</i> = 15; it costs $15 per day', ['<i>m</i> = 20; it costs $20 per day', '<i>m</i> = 15; there is a $15 one-time fee'], group=RO, space=45)
q(3, 'Identify <u>and</u> interpret the <i>y</i>-intercept.', '(0, 20); there is a $20 one-time fee', ['(0, 15); there is a $15 one-time fee', '(0, 20); it costs $20 per day'], group=RO, space=45)
q(3, 'Find the vertex of the absolute value graph. Is it a maximum or minimum?', f'({M}2, {M}3); minimum', [f'(2, {M}3); minimum', f'({M}2, {M}3); maximum'],
  extra=plane(-6, 6, -6, 6, px=140, curves=[[(-6, 1), (-2, -3), (2, 1)]] , pts=[(-2, -3)]), space=10)
assert len(Q) == 18

PHRASE = ['IT', 'HAD', 'THE', 'DRUMSTICKS']
letters = [ch for w in PHRASE for ch in w]
order = list(range(18)); random.shuffle(order)   # position p is answered by question order[p]
for p, qi in enumerate(order):
    Q[qi]['letter'] = letters[p]
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for qq in Q:
    qq['dletters'] = [random.choice([c for c in alpha if c != qq['letter']]) for _ in qq['distract']]

UNITS = B.UNITS
CSS = B.CSS + '''
.riddle { border: 2.5px solid #b5541c; border-radius: 10px; padding: 10px 14px; margin-top: 12px; background: #fdf2e4; }
.riddle .rq { font-family: "DejaVu Serif", serif; font-size: 15pt; color: #7a2e0e; font-weight: bold; text-align: center; margin-bottom: 10px; }
.words { display: flex; flex-wrap: wrap; justify-content: center; gap: 6px 22px; }
.word { display: flex; gap: 5px; }
.bl { width: 27px; text-align: center; }
.bl .ln { height: 30px; border-bottom: 2px solid #333; font-size: 17pt; font-weight: bold; }
.bl .n { font-size: 8.5pt; color: #555; margin-top: 2px; }
.bi b { width: 18px; }
'''

def qbox(n, qq, wide=False):
    extra = f'<div class="extra">{qq["extra"]}</div>' if qq['extra'] else ''
    return (f'<div class="qbox{" wide" if wide else ""}"><div class="qhead"><span class="qnum">{n}</span></div>'
            f'<div>{qq["prompt"]}</div>{extra}<div style="height:{int(qq["space"]*(1.0 if qq["unit"]==1 else 1.5))+(5 if qq["unit"]==1 else 15)}px"></div>'
            f'<div class="ans">Answer:<span class="blank"></span>Letter: <span class="codeblank" style="width:26px"></span></div></div>')

def header(t, s): return B.header(t, s)

DIR = ('<div class="dir"><b>🦃 Directions — Turkey Riddle Review</b><ol>'
       '<li>Solve each problem. <b>Show all required work</b> in the box.</li>'
       '<li>Find your answer in the <b>Answer Bank</b> and write its <b>letter</b> in the box.</li>'
       '<li>Write each letter above its problem number in the riddle to reveal the punchline.</li>'
       '<li>Can\'t find your answer, or the riddle doesn\'t spell real words? Check your work!</li></ol></div>')

layout = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17]]
wide = {5, 11}
pages = []
for pi, idxs in enumerate(layout):
    body = []
    if pi == 0:
        body += [header('Talking Turkey', 'Algebra 1B · Units 1–3 Thanksgiving Review · Riddle Decoder'), DIR]
    body.append(f'<h2 class="unit">{UNITS[pi+1]}</h2>')
    cur, last = [], None
    for i in idxs:
        qq = Q[i]
        if qq['group'] and qq['group'] != last:
            body.append('<div class="qs">' + ''.join(cur) + '</div>'); cur = []
            body.append(f'<div class="grp">{qq["group"]}</div>')
        last = qq['group']
        cur.append(qbox(i + 1, qq, i in wide))
    body.append('<div class="qs">' + ''.join(cur) + '</div>')
    pages.append('<div class="page">' + ''.join(body) + '</div>')

def riddle_html(key=False):
    out, p = [], 0
    for w in PHRASE:
        bls = []
        for ch in w:
            qi = order[p]; p += 1
            bls.append(f'<div class="bl"><div class="ln">{ch if key else ""}</div><div class="n">{qi+1}</div></div>')
        out.append('<div class="word">' + ''.join(bls) + '</div>')
    return ('<div class="riddle"><div class="rq">Why did the turkey join the band?</div>'
            '<div style="text-align:center;margin-bottom:6px">Because …</div><div class="words">' + ''.join(out) + '</div></div>')

bank = [header('Answer Bank &amp; Riddle', 'Not every answer here is correct!')]
for u in (1, 2, 3):
    items = []
    for qq in Q:
        if qq['unit'] != u: continue
        items.append((qq['answer'], qq['letter']))
        items += list(zip(qq['distract'], qq['dletters']))
    random.shuffle(items)
    bank.append(f'<div class="bank"><h3>{UNITS[u]}</h3><div class="bankgrid">' +
                ''.join(f'<div class="bi"><b>{l}</b><span>{a}</span></div>' for a, l in items) + '</div></div>')
bank.append(riddle_html())
pages.append('<div class="page">' + ''.join(bank) + '</div>')

key = ['<header class="top"><div><h1>Teacher Answer Key</h1><div class="sub">Talking Turkey · Units 1–3 Riddle Review</div></div></header>',
       '<div class="key"><table><tr><th>#</th><th>Unit</th><th>Correct answer</th><th>Letter</th><th>Distractors (likely error)</th></tr>']
for i, qq in enumerate(Q):
    ds = '; '.join(f'<b>{l}</b>: {a}' for a, l in zip(qq['distract'], qq['dletters']))
    key.append(f'<tr><td>{i+1}</td><td>{qq["unit"]}</td><td>{qq["answer"]}</td><td><b>{qq["letter"]}</b></td><td class="small">{ds}</td></tr>')
key.append('</table></div>')
key.append(riddle_html(True))
pages.append('<div class="page">' + ''.join(key) + '</div>')

out = f'<!doctype html><html><head><meta charset="utf-8"><title>Talking Turkey</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'riddle.html'), 'w').write(out)
print('ok')
