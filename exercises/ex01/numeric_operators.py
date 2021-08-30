"""Numeric operator program for EX01 to practice numeric operators, type conversions, and string concatenation."""

__author__: str = "730391039"

left_hand_number: str = input("Left-hand side: ")
right_hand_number: str = input("Right-hand side: ")

integer_left: int = int(left_hand_number, base=0)
integer_right: int = int(right_hand_number, base=0)

integer_exponent = integer_left ** integer_right 
exponent: str = str(integer_exponent)
print(left_hand_number + " ** " + right_hand_number + " is " + exponent)

float_division = integer_left / integer_right
division: str = str(float_division)
print(left_hand_number + " / " + right_hand_number + " is " + division)

integer_integer_division = integer_left // integer_right
integer_division: str = str(integer_integer_division)
print(left_hand_number + " // " + right_hand_number + " is " + integer_division)

integer_remainder = integer_left % integer_right
remainder: str = str(integer_remainder)
print(left_hand_number + " % " + right_hand_number + " is " + remainder)
