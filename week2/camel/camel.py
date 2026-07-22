def main():
    name = input("camelCase: ")
    print(f"snake_case: {convert(name)}")


def convert(name):
    # Walk through each character; an uppercase letter marks a new word
    result = ""
    for char in name:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result


if __name__ == "__main__":
    main()
