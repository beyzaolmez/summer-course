# Summer Preparation Programme — Computer Science

A 6-week self-study programme built from CS50x, CS50's Introduction to
Programming with Python, and CS50's Introduction to Artificial Intelligence with
Python. It covers programming fundamentals in C and Python, object-oriented
programming, web development with Flask, and core AI concepts (search and
logical reasoning).

Each week was originally developed on its own branch (`week-1` … `week-6`) with
clear commit messages. This `main` branch **merges all six weeks together** so
the whole programme can be viewed in one place.

## Progress

| Week | Topic | Status |
| ---- | ----- | ------ |
| 1 | Deep Dive into C | Complete |
| 2 | Python Essentials | Complete |
| 3 | OOP & Flask | Complete |
| 4 | AI: Search | Complete |
| 5 | AI: Knowledge | Complete |
| 6 | Final Project — Maze Solver | Complete |

## Repository layout

```
week1/   C problem sets (hello, mario, cash, credit, readability) + write-up
week2/   Python problem sets + command-line quiz app
week3/   OOP (Jar + tests), Seasons, and a Flask BMI calculator
week4/   AI search: Degrees (BFS) + BFS/DFS write-up
week5/   AI knowledge: Knights logic puzzles + a custom puzzle
week6/   Final project: Maze Solver (Flask + BFS)
```

## Running things

- **C (Week 1):** compile in the CS50 environment (`make <name>` then `./<name>`).
- **Python (Weeks 2–6):** run with `python <file>.py`. Some parts need extra
  packages: `pip install inflect` (Seasons) and
  `pip install -r requirements.txt` inside the Flask apps.
- **Flask apps (Weeks 3 & 6):** `cd` into the app folder and run `flask run`.

---

## Week 1 — Deep Dive into C

CS50x lectures: Week 0 (Scratch), Week 1 (C), Week 2 (Arrays). Assignments:
Scratch project, Hello, Mario, Cash, Credit, Readability, plus a write-up of the
Credit algorithm (`week1/explanation.md`).

### Week 1 Reflection

This week was my first real experience with C. Scratch made programming easy to understand because I could drag and drop blocks and instantly see what happened. With C, I had to pay much more attention to the details. Even a missing semicolon or brace could stop the whole program from compiling, which I find very annoying. :)

The first assignments, `hello` and `mario`, helped me get used to using `printf`, `get_string`, `get_int`, and writing loops. The `mario` problem especially helped me understand how nested loops work. At first it was confusing, but once I figured out how the rows and columns related to each other, it started to make sense. `cash` introduced me to the greedy algorithm, and I learned why it's better to convert dollars into cents using `round()` instead of working with floating-point numbers, which can cause unexpected errors.

The most challenging assignment was `credit`. Implementing Luhn's algorithm took some time because I had to work with each digit individually, double every second digit, and handle numbers larger than 9 correctly. My first solution became more complicated than it needed to be, so I started over and split the problem into smaller parts. First, I checked whether the card number was valid, and then I determined the card issuer. That approach made the code much easier to understand, and I also explained my solution in `explanation.md`. The `readability` assignment was interesting because it showed how counting letters, words, and sentences can be used to calculate a reading grade level.

The biggest thing I learned this week was the importance of debugging step by step. Instead of trying to fix everything at once, I compiled my code often, tested different inputs, and used small `printf` statements to check whether my variables contained the values I expected. I also realized that reading the assignment instructions carefully saves a lot of time because many of my mistakes came from missing small details.

---

## Week 2 — Python Essentials

CS50P lectures: Week 0, Week 1, and the loops portion of Week 2. Assignments:
Indoor Voice, Playback Speed, Deep Thought, Home Federal Savings Bank, Camel
Case, plus a command-line quiz app (`week2/quiz/quiz.py`).

### Week 2 Reflection

After a few weeks in C, moving to Python this week felt like taking off a heavy backpack. Ideas that took several careful lines in C — reading a string, looping over its characters, printing formatted output — became short and readable. The biggest early adjustment was trusting indentation instead of curly braces to define blocks, and getting used to not declaring types. It felt strange at first that a variable could just be a string without me saying so, but it made experimenting much faster.

The problem sets each reinforced one idea. `indoor` and `playback` were about string methods like `.lower()` and `.replace()`, which do in one call what would be a manual loop in C. `deep` was my first real use of Python conditionals and the handy `in` operator to check several accepted answers at once. `bank` taught me `.strip()` and `.startswith()`, and I liked splitting the logic into a separate `value()` function so `main()` stayed clean. `camel` was the one that made loops click: I walked through each character, and whenever I hit an uppercase letter I inserted an underscore and lowercased it — a small, satisfying algorithm.

The additional assignment was the most fun. I built a command-line quiz in `quiz.py`. I wanted it to feel solid, so I stored the questions as a list of dictionaries, looped over them with `enumerate` to number them, and wrote a `get_choice()` function that keeps asking until the user types a valid option. That input-validation loop was the part I had to think hardest about — my first version accepted anything, so I added a `while True` loop that only returns once the input is one of a, b, c, or d.

What I found difficult was resisting the urge to write everything inside one big function. Breaking the quiz into `ask`, `get_choice`, and `report` took a bit of planning, but it made testing each piece much easier. I improved mainly by running my code constantly with different inputs — empty strings, weird capitalisation, invalid answers — instead of assuming it worked. By the end of the week I feel comfortable with Python's core building blocks and genuinely enjoy how quickly I can turn an idea into a working program.

---

## Week 3 — Object-Oriented Programming and Flask

CS50P Week 8 (OOP) and CS50x Week 9 (Flask). Assignments: Jar (with pytest
tests), optional Seasons, and a Flask BMI calculator (`week3/flaskapp/`) with two
routes.

### Week 3 Reflection

This week tied two big ideas together: organising code with classes, and putting Python behind a web page with Flask. The `Jar` problem was my introduction to real object-oriented programming. At first I wasn't sure why I'd bother wrapping a couple of numbers in a class, but implementing it made the value obvious — the class guarantees its own rules. By putting the checks inside `deposit` and `withdraw`, and exposing `capacity` and `size` as read-only `@property` methods, it becomes impossible for outside code to put the jar into an invalid state. Understanding the difference between the private `_size` attribute and the public `size` property was the key insight.

Writing `test_jar.py` changed how I think about correctness. Instead of eyeing the output once, I wrote tests for the normal cases and the error cases, using `pytest.raises` to confirm the jar rejects a negative capacity, an over-deposit, and an over-withdrawal. Seeing "4 passed" gave me real confidence, and it caught a small mistake in my first version where I forgot the capacity check.

The optional `Seasons` problem pushed me into the `datetime` module. Working out that I could subtract two `date` objects to get a `timedelta`, then read `.days` off it, felt like discovering a superpower. I moved the calculation into its own `minutes_since` function so the date maths is separated from the input/printing, which also makes it testable.

Flask was the most exciting part. Building the BMI calculator, I finally saw how a request turns into a response: the `/` route renders a form, the browser POSTs the data to `/result`, and my function reads `request.form`, validates it, and renders a result template. The part I had to think carefully about was validation — what happens if someone types letters or a negative number? I wrapped the conversion in a `try/except` and re-render the form with an error message instead of crashing. Using Jinja template inheritance with a `layout.html` also kept the HTML tidy. The hardest bit conceptually was remembering that the server and browser are separate, but by the end I could picture the whole round trip.

---

## Week 4 — Artificial Intelligence: Search

CS50 AI Lecture 0 (Search). Assignment: Degrees (`week4/degrees/degrees.py`),
plus a write-up comparing BFS and DFS (`week4/degrees/explanation.md`). A small
`sample/` dataset is included for testing without the large official data.

### Week 4 Reflection

This week was my first taste of artificial intelligence, and the "degrees of separation" problem turned out to be a really intuitive way in. The big conceptual shift was learning to see a messy real-world question — how are two actors connected through films? — as an abstract graph search. Once I framed each actor as a state and "starred in the same movie" as an action between states, the AI lecture's vocabulary of nodes, frontiers, and explored sets suddenly mapped directly onto the code.

The core of the assignment was implementing `shortest_path`. The distribution code gave me `Node`, `StackFrontier`, and `QueueFrontier`, so my job was to wire them into a search loop. I chose a queue (breadth-first search) because the problem asks for the shortest chain, and BFS explores the graph ring by ring, guaranteeing the first path it finds to the target is a minimum-length one. The detail I found hardest was reconstructing the answer: the search only tells you that you reached the target, so I had to give every node a reference to its parent and the movie used to get there, then walk those parent links backwards and reverse the list.

A subtle point I initially got wrong was when to check for the goal. My first version tested the node when I removed it from the frontier, which works but does extra work. Moving the goal test to the moment a neighbour is generated made it stop as early as possible. I also had to remember to track both the `explored` set and what's already in the frontier, otherwise the search can loop forever on cycles in the graph.

To test without downloading the large dataset, I built a small `sample/` of six actors and three movies, which let me confirm both a connected case (Alice to Dave in 3 degrees) and a disconnected one. For the additional assignment I wrote up how the algorithm works and compared BFS and DFS: they share identical machinery and differ only in queue-vs-stack, but that single choice is what makes BFS optimal for shortest paths while DFS is not. This week made search feel much less mysterious and more like careful bookkeeping.

---

## Week 5 — Artificial Intelligence: Knowledge

CS50 AI Lecture 1 (Knowledge). Assignment: Knights (`week5/knights/puzzle.py`),
plus a custom logic puzzle (`week5/knights/extra.py`) with a write-up.

### Week 5 Reflection

Where Week 4 was about searching for a path, this week was about reasoning from facts — representing knowledge as logic and letting the computer deduce conclusions. The Knights puzzles were a brilliant way to practise this, because the challenge is almost entirely about translation: turning a sentence like "A says we are both knaves" into propositional logic without accidentally changing its meaning.

The insight that made everything click was how to model a statement. A knight tells the truth and a knave lies, so a character's claim is true exactly when that character is a knight. That is a biconditional: `Biconditional(AKnight, statement)`. This one idea handles both cases at once — if A is a knave, the biconditional forces the statement to be false, which is precisely what lying means. I liked it enough that I wrapped it in a small `says()` helper, plus a `game_rules()` helper for the "everyone is exactly one of knight or knave" constraints, so each puzzle reads almost like the English.

Puzzle 3 was the hardest to think about. A says one of two things but we don't know which, and B reports what A said. At first I tried to encode "A said X" directly and got stuck. The breakthrough was realising that B's own statement is what carries the information: `says(BKnight, says(AKnight, AKnave))` means "B is telling the truth exactly when A really is a knave-claimer." The `Or` covering A's two possible statements turns out to add nothing on its own (one side is a tautology), which confused me until I accepted that the constraints come from the other characters' testimony.

For the additional assignment I invented my own three-person puzzle in `extra.py` (A says "B is a knave", B says "A and C are the same kind", C says "A is a knight") and solved it with the same `model_check` engine, then verified the unique answer by hand. What I find powerful about this whole approach is that I never search for the answer myself — I only describe the world truthfully in logic, and the model checker exhaustively tests every assignment to find the consistent one. It made abstract logic feel concrete and genuinely useful.

---

## Week 6 — Final Project: Maze Solver (Flask + BFS)

A Flask web app that finds the shortest path through a user-drawn maze using
breadth-first search. It combines Python fundamentals, OOP, a Flask interface
(Week 3), and an AI search algorithm (Week 4). Full documentation is in
[`week6/maze-solver/README.md`](week6/maze-solver/README.md).

```bash
cd week6/maze-solver
pip install -r requirements.txt
flask run
```

### Week 6 Reflection

For my final project I made a Maze Solver. You basically draw a maze in a text box using a few characters, hit solve, and it shows you the shortest way from the start to the goal. I went with this idea on purpose because it let me reuse stuff I'd already built instead of starting something brand new. Honestly, after five weeks I wanted a project I could actually explain end to end, not one where I'd be guessing at my own code in the in-class session.

The part I'm most happy with is how it's organised. I kept all the actual logic in `maze.py` and none of the web stuff touches it — there's a `Maze` class that reads the text into a grid, figures out which neighbouring cells you're allowed to move into, and then runs BFS to find the path. Then `app.py` is just a small Flask file with two routes, one for the form and one that does the solving. Splitting it like that turned out to be a really good call, because I could run `maze.py` on its own in the terminal and check it worked before worrying about the browser at all.

The AI side is the search, which I lifted from the Week 4 Degrees project. Seeing BFS work in a totally different setting was the bit that made everything click for me. A maze is honestly just a graph in disguise — the cells are the states and the moves are up, down, left and right. And because BFS spreads out evenly instead of running down one path, the first time it hits the goal it's taken the fewest steps, so you know the answer is the shortest one. The two things that gave me trouble were the usual suspects: getting the path back out by walking the parent pointers, and dealing with someone typing a broken maze (no A or B) without the whole thing crashing.

Looking back at the whole six weeks, this project kind of sums up the journey. In Week 1 I was losing fights with semicolons in C, and now I can take an algorithm, put it in a class, stick it behind a web page, and actually say why it works. The biggest thing I picked up wasn't really a specific topic — it was the habit of building in small pieces, testing constantly, and writing these reflections, which forced me to slow down and understand what I'd done instead of just moving on. I feel ready to keep going with this.
