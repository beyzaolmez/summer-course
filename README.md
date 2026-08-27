# Summer Preparation Programme — Computer Science

A 6-week self-study programme built from CS50x, CS50 Python, and CS50 AI.
Each week lives on its own branch, with assignments and a written reflection.

## Progress

| Week | Topic | Status | Branch |
| ---- | ----- | ------ | ------ |
| 1 | Deep Dive into C | Complete | `week-1` |
| 2 | Python Essentials | Complete | `week-2` |
| 3 | OOP & Flask | Complete | `week-3` |
| 4 | AI: Search | Complete | `week-4` |
| 5 | AI: Knowledge | Complete | `week-5` |
| 6 | Final Project | Complete | `week-6` |

## Week 6 — Final Project: Maze Solver (Flask + BFS)

A Flask web app that finds the shortest path through a user-drawn maze using
breadth-first search. Full project documentation is in
[`week6/maze-solver/README.md`](week6/maze-solver/README.md).

### Files

| Part | File |
| ---- | ---- |
| Search logic (Maze class + BFS) | [`week6/maze-solver/maze.py`](week6/maze-solver/maze.py) |
| Flask app (two routes) | [`week6/maze-solver/app.py`](week6/maze-solver/app.py) |
| Project README | [`week6/maze-solver/README.md`](week6/maze-solver/README.md) |

### Running

```bash
cd week6/maze-solver
pip install -r requirements.txt
flask run
```

The app meets the final-project brief: it is written in Python, demonstrates
structured problem solving, and includes both a Flask component and an
AI-related (search) component.

### Week 6 Reflection

For my final project I made a Maze Solver. You basically draw a maze in a text
box using a few characters, hit solve, and it shows you the shortest way from the
start to the goal. I went with this idea on purpose because it let me reuse stuff
I'd already built instead of starting something brand new. Honestly, after five
weeks I wanted a project I could actually explain end to end, not one where I'd
be guessing at my own code in the in-class session.

The part I'm most happy with is how it's organised. I kept all the actual logic
in `maze.py` and none of the web stuff touches it — there's a `Maze` class that
reads the text into a grid, figures out which neighbouring cells you're allowed to
move into, and then runs BFS to find the path. Then `app.py` is just a small Flask
file with two routes, one for the form and one that does the solving. Splitting it
like that turned out to be a really good call, because I could run `maze.py` on its
own in the terminal and check it worked before worrying about the browser at all.

The AI side is the search, which I lifted from the Week 4 Degrees project. Seeing
BFS work in a totally different setting was the bit that made everything click for
me. A maze is honestly just a graph in disguise — the cells are the states and the
moves are up, down, left and right. And because BFS spreads out evenly instead of
running down one path, the first time it hits the goal it's taken the fewest steps,
so you know the answer is the shortest one. The two things that gave me trouble
were the usual suspects: getting the path back out by walking the parent pointers,
and dealing with someone typing a broken maze (no A or B) without the whole thing
crashing.

Looking back at the whole six weeks, this project kind of sums up the journey. In
Week 1 I was losing fights with semicolons in C, and now I can take an algorithm,
put it in a class, stick it behind a web page, and actually say why it works. The
biggest thing I picked up wasn't really a specific topic — it was the habit of
building in small pieces, testing constantly, and writing these reflections, which
forced me to slow down and understand what I'd done instead of just moving on. I
feel ready to keep going with this.
