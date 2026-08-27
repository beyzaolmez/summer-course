# Additional Assignment: A Custom Logic Puzzle

For the Week 5 additional assignment I created my own knights-and-knaves puzzle
and solved it with the same model-checking engine used in `puzzle.py`. The code
is in [`extra.py`](extra.py).

## The puzzle

On the Island of Knights and Knaves, **knights always tell the truth** and
**knaves always lie**, and every inhabitant is exactly one of the two.

Three inhabitants make these statements:

- **A says:** "B is a knave."
- **B says:** "A and C are the same kind."
- **C says:** "A is a knight."

**Question:** what is each inhabitant?

## How I encoded it

Each person gets two symbols, e.g. `AKnight` and `AKnave`. Two ideas turn the
English into logic:

1. **Game rules.** For every character I add `Or(knight, knave)` (they are one
   of the two) and `Not(And(knight, knave))` (not both).
2. **Statements.** A sentence is true exactly when its speaker is a knight. I
   model this with a biconditional: `Biconditional(speaker_is_knight, statement)`.
   If the speaker is a knight the statement must be true; if a knave, the
   biconditional forces the statement to be false — which is exactly what lying
   means.

So the three statements become:

- `Biconditional(AKnight, BKnave)`
- `Biconditional(BKnight, Or(And(AKnight, CKnight), And(AKnave, CKnave)))`
- `Biconditional(CKnight, AKnight)`

`model_check` then tries every possible True/False assignment of the six symbols
and keeps only the ones where the whole knowledge base is true.

## The solution

Running `python extra.py` gives:

```
A is a Knave
B is a Knight
C is a Knave
```

## Why that is the only consistent answer

I can verify it by hand:

- **A is a knave**, so A's statement "B is a knave" is a **lie** → B is **not**
  a knave → **B is a knight**.
- **B is a knight**, so B's statement is **true** → A and C are the same kind.
  Since A is a knave, **C is also a knave**.
- **C is a knave**, so C's statement "A is a knight" is a **lie** → A is **not**
  a knight → **A is a knave**, which matches where we started.

Every statement is consistent with the assignment, and `model_check` confirms no
other assignment satisfies all the constraints — so the answer is unique. The
nice thing about this approach is that I never had to reason through the cases
myself to *find* the answer; I only had to translate the English faithfully into
logic, and the model checker did the search.
