from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


# The rules of the game, reused for every puzzle:
# each character is exactly one of a knight or a knave.
def game_rules(*characters):
    rules = And()
    for knight, knave in characters:
        rules.add(Or(knight, knave))          # is a knight or a knave
        rules.add(Not(And(knight, knave)))    # but not both
    return rules


# A knight's statement is true; a knave's statement is false. This is captured
# by a biconditional: (character is a knight) <=> (their statement is true).
def says(knight, statement):
    return Biconditional(knight, statement)


# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    game_rules((AKnight, AKnave)),
    says(AKnight, And(AKnight, AKnave)),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    game_rules((AKnight, AKnave), (BKnight, BKnave)),
    says(AKnight, And(AKnave, BKnave)),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    game_rules((AKnight, AKnave), (BKnight, BKnave)),
    says(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    says(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    game_rules((AKnight, AKnave), (BKnight, BKnave), (CKnight, CKnave)),

    # A made one of these two statements (we don't know which)
    Or(says(AKnight, AKnight), says(AKnight, AKnave)),

    # B claims that A said "I am a knave"
    says(BKnight, says(AKnight, AKnave)),

    # B claims that C is a knave
    says(BKnight, CKnave),

    # C claims that A is a knight
    says(CKnight, AKnight),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.symbols()) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
