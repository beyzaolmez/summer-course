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
| 5 | AI: Knowledge | In progress | `week-5` |
| 6 | Final Project | Not started | — |

## Week 5 — Artificial Intelligence: Knowledge

Lecture completed: CS50 AI Lecture 1 (Knowledge).

### Assignments

| Assignment | File |
| ---------- | ---- |
| Knights | [`week5/knights/puzzle.py`](week5/knights/puzzle.py) |
| Additional (custom logic puzzle + write-up) | [`week5/knights/extra.py`](week5/knights/extra.py), [`explanation.md`](week5/knights/explanation.md) |

### Running

No external packages needed:

```bash
cd week5/knights
python puzzle.py   # solves the four required puzzles
python extra.py    # solves my custom puzzle
```

### Week 5 Reflection

Where Week 4 was about *searching* for a path, this week was about *reasoning*
from facts — representing knowledge as logic and letting the computer deduce
conclusions. The Knights puzzles were a brilliant way to practise this, because
the challenge is almost entirely about translation: turning a sentence like "A
says we are both knaves" into propositional logic without accidentally changing
its meaning.

The insight that made everything click was how to model a *statement*. A knight
tells the truth and a knave lies, so a character's claim is true exactly when
that character is a knight. That is a **biconditional**:
`Biconditional(AKnight, statement)`. This one idea handles both cases at once —
if A is a knave, the biconditional forces the statement to be false, which is
precisely what lying means. I liked it enough that I wrapped it in a small
`says()` helper, plus a `game_rules()` helper for the "everyone is exactly one
of knight or knave" constraints, so each puzzle reads almost like the English.

Puzzle 3 was the hardest to think about. A says one of two things but we don't
know which, and B *reports* what A said. At first I tried to encode "A said X"
directly and got stuck. The breakthrough was realising that B's own statement is
what carries the information: `says(BKnight, says(AKnight, AKnave))` means "B is
telling the truth exactly when A really is a knave-claimer." The `Or` covering
A's two possible statements turns out to add nothing on its own (one side is a
tautology), which confused me until I accepted that the constraints come from the
*other* characters' testimony.

For the additional assignment I invented my own three-person puzzle in
`extra.py` (A says "B is a knave", B says "A and C are the same kind", C says "A
is a knight") and solved it with the same `model_check` engine, then verified the
unique answer by hand in `explanation.md`. What I find powerful about this whole
approach is that I never search for the answer myself — I only describe the world
truthfully in logic, and the model checker exhaustively tests every assignment
to find the consistent one. It made abstract logic feel concrete and genuinely
useful.
