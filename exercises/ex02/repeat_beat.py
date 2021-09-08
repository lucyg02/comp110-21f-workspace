"""Repeating a beat in a loop."""

__author__ = "730391039"


i: int = 0
beat: str = input("What beat do you want to repeat? ")
repeats: int = int(input("How many times do you want to repeat it? "))
blank: str = ""

if repeats <= 0:
    print("No beat...")
else:
    while i < repeats:
        if i == 0:
            blank = blank + beat
        else:
            blank = blank + " " + beat
        i = i + 1
    print(blank)