"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730391039"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

print("Your fortune cookie says...")
random_number: int = randint(1, 3)
if random_number == 1:
    print("You will have a long and fruitful life.")
else:
    if random_number == 2:
        print("You will do well in your classes this semester.")
    else:
        print("A great change is coming.")
print("Now, go spread positive vibes!")