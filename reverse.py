def main():
    word=input("Enter the word: ")
    print(reversed_word(word))

def reversed_word(word):
    reverse=word[::-1]
    return f"You wrote {word} when reversed it would give you {reverse}"


if __name__ == "__main__":
    main()