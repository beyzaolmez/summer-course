def main():
    # Accept the user's answer, ignoring case and surrounding spaces
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    if answer.strip().lower() in ["42", "forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
