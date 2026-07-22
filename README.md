# Summer Preparation Programme — Computer Science

A 6-week self-study programme built from CS50x, CS50 Python, and CS50 AI.
Each week lives on its own branch, with assignments and a written reflection.

## Progress

| Week | Topic | Status | Branch |
| ---- | ----- | ------ | ------ |
| 1 | Deep Dive into C | Complete | `week-1` |
| 2 | Python Essentials | In progress | `week-2` |
| 3 | OOP & Flask | Not started | — |
| 4 | AI: Search | Not started | — |
| 5 | AI: Knowledge | Not started | — |
| 6 | Final Project | Not started | — |

## Week 2 — Python Essentials

CS50P lectures completed: Week 0, Week 1, and the loops portion of Week 2.

### Assignments

| Assignment | File |
| ---------- | ---- |
| Indoor Voice | [`week2/indoor/indoor.py`](week2/indoor/indoor.py) |
| Playback Speed | [`week2/playback/playback.py`](week2/playback/playback.py) |
| Deep Thought | [`week2/deep/deep.py`](week2/deep/deep.py) |
| Home Federal Savings Bank | [`week2/bank/bank.py`](week2/bank/bank.py) |
| Camel Case | [`week2/camel/camel.py`](week2/camel/camel.py) |
| Additional (CLI quiz app) | [`week2/quiz/quiz.py`](week2/quiz/quiz.py) |

### Running

Python 3 only — no external libraries needed:

```bash
python week2/indoor/indoor.py
python week2/quiz/quiz.py
```

The quiz app (`quiz.py`) is the additional assignment: a command-line
multiple-choice quiz that takes input, validates it, keeps score, and prints a
final result.

### Week 2 Reflection

After a few weeks in C, moving to Python this week felt like taking off a heavy
backpack. Ideas that took several careful lines in C — reading a string,
looping over its characters, printing formatted output — became short and
readable. The biggest early adjustment was trusting **indentation** instead of
curly braces to define blocks, and getting used to not declaring types. It felt
strange at first that a variable could just *be* a string without me saying so,
but it made experimenting much faster.

The problem sets each reinforced one idea. `indoor` and `playback` were about
string methods like `.lower()` and `.replace()`, which do in one call what would
be a manual loop in C. `deep` was my first real use of Python conditionals and
the handy `in` operator to check several accepted answers at once. `bank` taught
me `.strip()` and `.startswith()`, and I liked splitting the logic into a
separate `value()` function so `main()` stayed clean. `camel` was the one that
made loops click: I walked through each character, and whenever I hit an
uppercase letter I inserted an underscore and lowercased it — a small, satisfying
algorithm.

The additional assignment was the most fun. I built a command-line quiz in
`quiz.py`. I wanted it to feel solid, so I stored the questions as a list of
dictionaries, looped over them with `enumerate` to number them, and wrote a
`get_choice()` function that keeps asking until the user types a valid option.
That input-validation loop was the part I had to think hardest about — my first
version accepted anything, so I added a `while True` loop that only returns once
the input is one of a, b, c, or d.

What I found difficult was resisting the urge to write everything inside one
big function. Breaking the quiz into `ask`, `get_choice`, and `report` took a
bit of planning, but it made testing each piece much easier. I improved mainly
by running my code constantly with different inputs — empty strings, weird
capitalisation, invalid answers — instead of assuming it worked. By the end of
the week I feel comfortable with Python's core building blocks and genuinely
enjoy how quickly I can turn an idea into a working program.
