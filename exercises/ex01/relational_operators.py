"""Relational operator program for EX01 to pratice using relational operators."""

__author__: str = "730391039"

left_hand_number: str = input("Left-hand side: ")
right_hand_number: str = input("Right-hand side: ")

integer_left: int = int(left_hand_number, base=0)
integer_right: int = int(right_hand_number, base=0)

bool_less_than = integer_left < integer_right
less_than: str = str(bool_less_than)
print(left_hand_number + " < " + right_hand_number + " is " + less_than)

bool_greater_equal = integer_left >= integer_right
greater_equal: str = str(bool_greater_equal)
print(left_hand_number + " >= " + right_hand_number + " is " + greater_equal)

bool_equal = integer_left == integer_right
equal: str = str(bool_equal)
print(left_hand_number + " == " + right_hand_number + " is " + equal)

bool_not_equal = integer_left != integer_right
not_equal: str = str(bool_not_equal)
print(left_hand_number + " != " + right_hand_number + " is " + not_equal)