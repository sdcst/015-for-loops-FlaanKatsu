"""
Help Jenny keep track of her expenses!
Each month, she needs to keep track of:
1. The current balance on her credit card
2. The total amount of her purchases
3. The total amount that she pays off
4. If she has an unpaid balance, then 2% of the current balance is charged to her

Write a program that asks her to enter in her total purchases as
well as how much she pays off.  Calculate any interest that she must add to her
balance and display her total balance at the end of the month.

A sample for the first few months is shown below:

Enter total purchases for month(1) : 100
Enter total payments for month(1)  : 75
2% interest has been charged: 0.5
Your closing balance is $25.5

Enter total purchases for month(2) : 100
Enter total payments for month(2)  : 75
2% interest has been charged: 1.01
Your closing balance is $51.51

"""

##1st attempt:
"""
Aa = 0
AA = 0
fee = 0
n月 = round(float(input("please input the amount of months you want the calculator to calculate: ")), 0)
n月 = int(n月)
n月 + 1
for 今月 in range(1, n月):
    debt = round(float(input(f"please enter the amount of money used on your card for month {今月}: ")), 2)
    undebt = round(float(input(f"please enter the amount of money payed back for month {今月}: ")), 2)
    aa = debt - undebt
    Aa = aa
    AA = AA + Aa
    fee = AA * 0.02
    AA = AA + fee
    if debt > undebt:
        print(f"the amount of money you now owe is ${round(AA, 2)}", end="")
        if fee == 0:
            print(".")
        elif fee != 0:
            print(f", including 2% additional interest that has been charged: ${round(fee, 2)}.")
"""

##new attempt

n月 = round(float(input("please input the amount of months you want the calculator to calculate: ")), 0)
n月 = int(n月)
n月 + 1
currentOwe = 0
for 今月 in range(1, n月):
    debt = round(float(input(f"please enter the amount of money used on your card for month {今月}: ")), 2)
    undebt = round(float(input(f"please enter the amount of money payed back for month {今月}: ")), 2)
    deltaM = debt - undebt
    currentOwe = currentOwe + deltaM
    fee = currentOwe * 0.02
    if currentOwe > 0:
        currentOwe = currentOwe + fee
    if currentOwe > 0:
        print(f"the amount of money you now owe is ${round(currentOwe, 2)}", end="")
        if fee == 0:
            print(".")
        elif fee != 0:
            print(f", including 2% additional interest that has been charged: ${round(fee, 2)}.")
    elif currentOwe < 0:
        print(f"congradulations, you have payed off all debt! You have payed the bank an excess of ${round(currentOwe - (currentOwe* 2), 2)}")
    elif currentOwe == 0:
        print("You have payed off all debt properly.")
print("The current pay period has ended, program will now terminate.")
        