# Summer Preparation Programme — Computer Science

A 6-week self-study programme built from CS50x, CS50 Python, and CS50 AI.
Each week lives on its own branch, with assignments and a written reflection.

## Progress

| Week | Topic | Status | Branch |
| ---- | ----- | ------ | ------ |
| 1 | Deep Dive into C | Complete | `week-1` |
| 2 | Python Essentials | Complete | `week-2` |
| 3 | OOP & Flask | In progress | `week-3` |
| 4 | AI: Search | Not started | — |
| 5 | AI: Knowledge | Not started | — |
| 6 | Final Project | Not started | — |

## Week 3 — Object-Oriented Programming and Flask

Lectures completed: CS50 Python Week 8 (OOP) and CS50x Week 9 (Flask).

### Assignments

| Assignment | File |
| ---------- | ---- |
| Jar | [`week3/jar/jar.py`](week3/jar/jar.py) (tests: [`test_jar.py`](week3/jar/test_jar.py)) |
| Seasons (optional) | [`week3/seasons/seasons.py`](week3/seasons/seasons.py) |
| Additional (Flask BMI app) | [`week3/flaskapp/app.py`](week3/flaskapp/app.py) |

### Running

**Jar** (plus its pytest tests):

```bash
python week3/jar/jar.py
cd week3/jar && python -m pytest
```

**Seasons** (needs the `inflect` package):

```bash
pip install inflect
python week3/seasons/seasons.py
```

**Flask BMI app** (the additional assignment):

```bash
cd week3/flaskapp
pip install -r requirements.txt
flask run
```

The Flask app has two routes: `/` serves an input form, and `/result` (POST)
validates the submitted weight/height, computes the BMI, and shows the category.

### Week 3 Reflection

This week tied two big ideas together: organising code with classes, and
putting Python behind a web page with Flask. The `Jar` problem was my
introduction to real object-oriented programming. At first I wasn't sure why I'd
bother wrapping a couple of numbers in a class, but implementing it made the
value obvious — the class *guarantees its own rules*. By putting the checks
inside `deposit` and `withdraw`, and exposing `capacity` and `size` as
read-only `@property` methods, it becomes impossible for outside code to put the
jar into an invalid state. Understanding the difference between the private
`_size` attribute and the public `size` property was the key insight.

Writing `test_jar.py` changed how I think about correctness. Instead of eyeing
the output once, I wrote tests for the normal cases *and* the error cases, using
`pytest.raises` to confirm the jar rejects a negative capacity, an over-deposit,
and an over-withdrawal. Seeing "4 passed" gave me real confidence, and it caught
a small mistake in my first version where I forgot the capacity check.

The optional `Seasons` problem pushed me into the `datetime` module. Working out
that I could subtract two `date` objects to get a `timedelta`, then read `.days`
off it, felt like discovering a superpower. I moved the calculation into its own
`minutes_since` function so the date maths is separated from the input/printing,
which also makes it testable.

Flask was the most exciting part. Building the BMI calculator, I finally saw how
a request turns into a response: the `/` route renders a form, the browser POSTs
the data to `/result`, and my function reads `request.form`, validates it, and
renders a result template. The part I had to think carefully about was
validation — what happens if someone types letters or a negative number? I
wrapped the conversion in a `try/except` and re-render the form with an error
message instead of crashing. Using Jinja template inheritance with a
`layout.html` also kept the HTML tidy. The hardest bit conceptually was
remembering that the server and browser are separate, but by the end I could
picture the whole round trip, and I'm keen to build something bigger with it.
