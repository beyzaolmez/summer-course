"""
Additional assignment: a custom knights-and-knaves puzzle.

On the Island of Knights and Knaves, knights always tell the truth and knaves
always lie. Every inhabitant is exactly one of the two.

Three inhabitants, A, B, and C, make the following statements:
    A says: "B is a knave."
    B says: "A and C are the same kind."
    C says: "A is a knight."

The solver below uses the same model-checking approach as puzzle.py to find the
one assignment of knights/knaves that is logically consistent.
"""

from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


def game_rules(*characters):
    # Each character is exactly one of a knight or a knave
    rules = And()
    for knight, knave in characters:
        rules.add(Or(knight, knave))
        rules.add(Not(And(knight, knave)))
    return rules


def says(knight, statement):
    # A knight's statement is true iff they are a knight
    return Biconditional(knight, statement)


knowledge = And(
    game_rules((AKnight, AKnave), (BKnight, BKnave), (CKnight, CKnave)),

    # A says "B is a knave."
    says(AKnight, BKnave),

    # B says "A and C are the same kind."
    says(BKnight, Or(And(AKnight, CKnight), And(AKnave, CKnave))),

    # C says "A is a knight."
    says(CKnight, AKnight),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    print("Custom Puzzle")
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(f"    {symbol}")


if __name__ == "__main__":
    main()
