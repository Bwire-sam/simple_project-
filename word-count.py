def main():
    word = input("Write a sentence: ")
    print(word)
    print(new_word(word))

def new_word(word):
    new = word.split()
    return f"Your sentence has {len(new)} words"

if __name__ == "__main__":
    main()
