"""Counting letters in a string."""

__author__ = "730391039"


letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
i: int = 0
frequency: str = ""

while i < len(word):
    if word[i] == letter:
        frequency = frequency + letter
    else:
        frequency == 0
    i = i + 1
count: int = len(frequency)
count_string: str = str(count)
print("Count: " + count_string)