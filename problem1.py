#!python3
"""
###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You will need 2 nested loops to draw the contents of
1 row and the number of rows.

inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****

"""
n = round(float(input("please enter a number less than 10.")), 0)
n = int(n)
if n < 10:
    for b in range(n):
        print("*" * n)
elif n >= 10:
    print("Error: your number is too large.(Must be less than 10)")
