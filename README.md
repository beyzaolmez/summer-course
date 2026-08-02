# Summer Preparation Programme — Computer Science

A 6-week self-study programme built from CS50x, CS50 Python, and CS50 AI.
Each week lives on its own branch, with assignments and a written reflection.

## Progress

| Week | Topic | Status | Branch |
| ---- | ----- | ------ | ------ |
| 1 | Deep Dive into C | Complete | `week-1` |
| 2 | Python Essentials | Complete | `week-2` |
| 3 | OOP & Flask | Complete | `week-3` |
| 4 | AI: Search | In progress | `week-4` |
| 5 | AI: Knowledge | Not started | — |
| 6 | Final Project | Not started | — |

## Week 4 — Artificial Intelligence: Search

Lecture completed: CS50 AI Lecture 0 (Search).

### Assignments

| Assignment | File |
| ---------- | ---- |
| Degrees | [`week4/degrees/degrees.py`](week4/degrees/degrees.py) |
| Additional (search write-up, BFS vs DFS) | [`week4/degrees/explanation.md`](week4/degrees/explanation.md) |

### Running

The official CS50 datasets are **not** committed here (the `large` set is big).
Download `degrees.zip` from the CS50 AI project page and copy its `small/` and
`large/` folders into `week4/degrees/`. Then:

```bash
cd week4/degrees
python degrees.py small
```

A tiny self-made `sample/` dataset is included so the program can be run and
tested without the download:

```bash
python degrees.py sample   # try "Alice" then "Dave" -> 3 degrees
```

### Week 4 Reflection

This week was my first taste of artificial intelligence, and the "degrees of
separation" problem turned out to be a really intuitive way in. The big
conceptual shift was learning to see a messy real-world question — how are two
actors connected through films? — as an abstract **graph search**. Once I
framed each actor as a *state* and "starred in the same movie" as an *action*
between states, the AI lecture's vocabulary of nodes, frontiers, and explored
sets suddenly mapped directly onto the code.

The core of the assignment was implementing `shortest_path`. The distribution
code gave me `Node`, `StackFrontier`, and `QueueFrontier`, so my job was to wire
them into a search loop. I chose a queue (breadth-first search) because the
problem asks for the *shortest* chain, and BFS explores the graph ring by ring,
guaranteeing the first path it finds to the target is a minimum-length one. The
detail I found hardest was reconstructing the answer: the search only tells you
*that* you reached the target, so I had to give every node a reference to its
parent and the movie used to get there, then walk those parent links backwards
and reverse the list.

A subtle point I initially got wrong was *when* to check for the goal. My first
version tested the node when I removed it from the frontier, which works but
does extra work. Moving the goal test to the moment a neighbour is generated
made it stop as early as possible. I also had to remember to track both the
`explored` set and what's already in the frontier, otherwise the search can loop
forever on cycles in the graph.

To test without downloading the large dataset, I built a small `sample/` of six
actors and three movies, which let me confirm both a connected case (Alice to
Dave in 3 degrees) and a disconnected one. For the additional assignment I wrote
up how the algorithm works and compared BFS and DFS in `explanation.md`: they
share identical machinery and differ only in queue-vs-stack, but that single
choice is what makes BFS optimal for shortest paths while DFS is not. This week
made search feel much less mysterious and more like careful bookkeeping.
