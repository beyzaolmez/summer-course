# Additional assignment: a small command-line multiple-choice quiz.
# It accepts user input, validates it, keeps score, and reports a result.

QUESTIONS = [
    {
        "prompt": "Which keyword defines a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "b",
    },
    {
        "prompt": "What does the len() function return for the string 'CS50'?",
        "options": ["3", "4", "5", "It raises an error"],
        "answer": "b",
    },
    {
        "prompt": "Which of these is used to repeat code a fixed number of times?",
        "options": ["if statement", "for loop", "function", "variable"],
        "answer": "b",
    },
    {
        "prompt": "What symbol starts a comment in Python?",
        "options": ["//", "<!--", "#", "/*"],
        "answer": "c",
    },
    {
        "prompt": "What is the result of 7 % 3?",
        "options": ["1", "2", "2.33", "0"],
        "answer": "b",
    },
]

LETTERS = ["a", "b", "c", "d"]


def main():
    print("Welcome to the Python Quiz! Answer with a, b, c, or d.\n")

    score = 0
    for number, question in enumerate(QUESTIONS, start=1):
        if ask(number, question):
            score += 1

    report(score, len(QUESTIONS))


def ask(number, question):
    # Show one question and its options, then grade the (validated) answer
    print(f"Question {number}: {question['prompt']}")
    for letter, option in zip(LETTERS, question["options"]):
        print(f"  {letter}) {option}")

    choice = get_choice()

    if choice == question["answer"]:
        print("Correct!\n")
        return True
    else:
        correct_letter = question["answer"]
        print(f"Wrong. The correct answer was {correct_letter}.\n")
        return False


def get_choice():
    # Keep prompting until the user gives a valid option
    while True:
        choice = input("Your answer: ").strip().lower()
        if choice in LETTERS:
            return choice
        print("Please enter a, b, c, or d.")


def report(score, total):
    percent = round(score / total * 100)
    print(f"You scored {score} out of {total} ({percent}%).")

    if percent == 100:
        print("Perfect score! Great job.")
    elif percent >= 60:
        print("Nicely done.")
    else:
        print("Keep practising - you'll get there.")


if __name__ == "__main__":
    main()
