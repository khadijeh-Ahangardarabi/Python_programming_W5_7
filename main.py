
DELIMITER = ","


def collectWords() -> str:
    words = ""

    while True:
        word = input("Insert word(empty stops): ")

        if word == "":
            break

        if words == "":
            words = word
        else:
            words += DELIMITER + word

    return words


def analyseWords(words: str) -> None:
    wordList = words.split(DELIMITER) if words else []

    wordCount = len(wordList)
    characterCount = sum(len(word) for word in wordList)

    if wordCount > 0:
        averageLength = characterCount / wordCount
    else:
        averageLength = 0.0

    print(f"- {wordCount} Words")
    print(f"- {characterCount} Characters")
    print(f"- {averageLength:.2f} Average word length")


def main() -> None:
    words = collectWords()
    analyseWords(words)


print("Program starting.")
main()
print("Program ending.")

