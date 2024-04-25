#! python3
"""
##### Task 3
Print all the numbers from 1 to 1000 that are divisible by 5.
"""
import math
for i in range(1001):
    ix = math.ceil(i / 5)
    iy = math.floor(i / 5)
    if iy == ix:
        print(i)
print("done")