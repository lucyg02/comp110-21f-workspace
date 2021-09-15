"""An exercise in remainders and boolean logic."""

__author__ = "730391039"


number: int = int(input("Enter an int: "))
if ((number % 2) == 0) and ((number % 7) == 0):
    print("TAR HEELS")
if ((number % 2) == 0) and (not (number % 7) == 0):
    print("TAR")
if ((number % 7) == 0) and (not (number % 2) == 0):
    print("HEELS")
if (not (number % 2) == 0) and (not (number % 7) == 0):
    print("CAROLINA")