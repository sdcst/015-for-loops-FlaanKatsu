#! python3
"""
###### Task 2
Ask the user to enter in the prices of 5 items in dollars.cents (eg 10.34).  Find the total value of all items and then calculate the total price including 5% GST and 7% PST

Sample:
Enter in price of item #1: 10.25
Enter in price of item #2: 11.45
Enter in price of item #3: 13.85
Enter in price of item #4: 9.25
Enter in price of item #5: 10.25
Your subtotal is 55.05
Your GST is 2.75
Your PST is 3.85
Your total is 61.65
"""
##define vars
subtotal = 0

print("Lord beelzebul will calculate the total price of of 5 items, and their taxes.")
for i in range(1, 6):
    n = round(float(input(f"please enter the price of item {i}: ")), 2)
    subtotal = subtotal + n
print(f"the subtotal is ${round(subtotal, 2)}.")
GST = round(subtotal * 0.05, 2)
PST = round(subtotal * 0.07, 2)
total = round(subtotal + PST + GST, 2)
print(f"the GST is ${GST}.")
print(f"the PST is ${PST}.")
print(f"the total is ${total}.")