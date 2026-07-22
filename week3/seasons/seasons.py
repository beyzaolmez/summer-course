import sys
from datetime import date

import inflect


def main():
    birth = input("Date of Birth: ")
    minutes = minutes_since(birth)

    # Convert the number to words, without an "and" (e.g. "five hundred")
    engine = inflect.engine()
    words = engine.number_to_words(minutes, andword="")
    print(f"{words.capitalize()} minutes")


def minutes_since(birth, today=None):
    # Parse an ISO date (YYYY-MM-DD); anything else is an error
    try:
        year, month, day = birth.split("-")
        born = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")

    if today is None:
        today = date.today()

    days = (today - born).days
    return days * 24 * 60


if __name__ == "__main__":
    main()
