# Maze Solver — Final Project

A small Flask web application that finds the **shortest path** through a maze
using **breadth-first search (BFS)**. It ties together three ideas from the
programme: Python fundamentals, a Flask web interface (Week 3), and an AI search
algorithm (Week 4).

## What it does

You "draw" a maze in a text box using simple characters:

| Character | Meaning |
| --------- | ------- |
| `A` | start |
| `B` | goal |
| `#` | wall |
| space | open path |

When you submit it, the app searches for the shortest route from `A` to `B` and
draws the maze back to you with the solution path highlighted, along with the
number of steps and how many cells were explored. If no route exists, it says so.

## How it works

The project is split into two clear parts:

- **`maze.py`** — the logic, with no web code. A `Maze` class parses the text
  into a grid, and `solve()` runs BFS:
  - Each cell position `(row, col)` is a **state**.
  - A **queue frontier** (`QueueFrontier`) explores cells in the order they were
    discovered, so the first time it reaches `B` it has used the fewest steps —
    that is why BFS gives the *shortest* path.
  - Every `Node` remembers its parent, so once the goal is found the path is
    rebuilt by following parent links back to the start.
  - An `explored` set prevents revisiting cells and looping forever.
- **`app.py`** — the Flask layer with two routes:
  - `GET /` shows the input form (`index.html`) with an example maze.
  - `POST /solve` reads the submitted maze, validates it, solves it, and renders
    the result grid (`result.html`).

Keeping the logic (`maze.py`) separate from the web layer (`app.py`) means the
solver can be tested on its own from the command line:

```bash
python maze.py
```

## Running it

```bash
cd week6/maze-solver
pip install -r requirements.txt
flask run
```

Then open the printed URL (usually <http://127.0.0.1:5000>).

## What I learned

Building this pulled together the whole programme. The BFS came straight from
the Week 4 "Degrees" project, but applying it to a 2D grid made me really
understand that a "graph" is just states and the moves between them — here the
moves are up/down/left/right. Wrapping the maze in a class (Week 3 OOP) kept the
parsing, neighbour-finding, and solving neatly in one place. Flask (Week 3) then
turned it into something interactive. The trickiest parts were reconstructing
the path from parent pointers and validating messy user input (a maze with no
`A` or `B`), which I handle by raising a `ValueError` and showing a friendly
message instead of crashing.
