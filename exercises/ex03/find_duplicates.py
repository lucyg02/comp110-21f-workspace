"""Finding duplicate letters in a word."""

__author__ = "730391039"

word: str = input("Enter a word: ")

i: int = 0
dup: bool = False

while i < len(word):
    char = word[i]
    j: int = i + 1
    while j < len(word):
        dup = bool(word[j] == char)
        j += 1
        if dup is True:
            j = len(word) + 1
            i = len(word) + 1
    i += 1

dup_string: str = str(dup)
print("Found duplicate: " + dup_string)