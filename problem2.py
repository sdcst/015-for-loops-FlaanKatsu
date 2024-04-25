#!python3

"""
##### Problem 2
Calculate the factorial of a number. 

 4! does not mean 4 is excited, it's the notation for a factorial.
A factorial is a special operation in math that is used in probability 
and combination problems.  For example, if you have 4 people, the number
of ways that they can be lined up against the wall is 4!

A factorial is defined as:
5! = 1 * 2 * 3 * 4 * 5
5! = 120

3! = 1 * 2 * 3
3! = 6

Note that a factorial can only accept an integer as an input number.  
Your program should also include some "input validation". This means that
the program will only determine the factorial IF the input is a positive
integer.  If the number is not a positive integer, it will display 
"Invalid input"

inputs:
int number

outputs:
"xx! is yy" where xx is the integer entered and yy is the calculated answer
Invalid input

example:
Enter a number: 4
4! is 24

example:
Enter a number: -4
Invalid input
"""
##import modules
import math

#Define vars
UE = 0
aa = 1
n = float(input("Please enter a number, must be a positive intager."))
if int(n) == n and n > 0:
    n = int(n)
    for i in range(1, n + 1):
        aa = aa * i
    print(f"{n}! is {aa}")
##test if user input is valid. else, set variable "user error" (UE) to true (1)
