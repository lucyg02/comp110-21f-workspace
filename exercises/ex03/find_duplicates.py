"""Finding duplicate letters in a word."""

__author__ = "730391039"

word: str = input("Enter a word: ")
i: int = 0
answer: str = ""

while i < len(word):
    j: int = i + 1
    result: bool = bool(word[j] == word[i])
    result_string: str = str(result)
    if result is True and not False:
        answer = result_string
        i = len(word)
    else:
        answer = result_string
    j += 1
    i += 1
print("Found duplicate: " + answer)