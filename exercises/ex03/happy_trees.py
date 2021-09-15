"""Drawing forests in a loop."""

__author__ = "730391039"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
i: int = 0
depth: int = int(input("Depth: "))
blank: str = ""

if depth > 0:
    while i < depth:
        blank = blank + TREE
        i = i + 1
        print(blank)