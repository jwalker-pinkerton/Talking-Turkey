# Talking Turkey

A Thanksgiving riddle-decoder review for Algebra 1B, Units 1–3. It's a shorter alternative
to a full-period activity: 18 problems, 6 per unit.

Students solve each problem, find their answer in the Answer Bank to get a letter, and write
each letter above its problem number to answer the riddle *"Why did the turkey join the band?"*
The problem numbers are scrambled along the blanks, so the punchline can't be guessed without
doing the work. Each correct answer is mixed in with 1–2 wrong answers based on common mistakes;
a wrong answer gives a wrong letter, so the riddle won't spell real words.

- **Unit 1:** simplifying, function composition, equations with variables on both sides,
  absolute value equations, a define-write-solve-interpret word problem
- **Unit 2:** writing inequalities from sentences and graphs, solving and graphing
  (including sign flips), compound inequalities, an "at most" word problem
- **Unit 3:** function or not from a table, slope, converting standard form, interpreting
  slope and y-intercept, the vertex of an absolute value graph

## Files

| File | What it is |
| --- | --- |
| `Talking_Turkey_Units1-3_Riddle_Review.pdf` | Printable activity (problems, answer bank and riddle, teacher key) |
| `riddle.html` | The same activity as HTML |
| `riddle.py` | Generates `riddle.html`: questions, answers, wrong-answer choices, letters |
| `helpers.py` | Shared formatting: fractions, number lines, graphs, tables, page styles |
| `render.js` | Converts `riddle.html` to PDF with Playwright |

## Rebuilding after edits

Edit the questions in `riddle.py`, then run:

```bash
python3 riddle.py
```

```bash
node render.js "$PWD/riddle.html" "$PWD/Talking_Turkey_Units1-3_Riddle_Review.pdf"
```

Requires Python 3 and Node.js with Playwright (Chromium). If you change the number of
questions, the riddle phrase in `riddle.py` must have the same number of letters.
