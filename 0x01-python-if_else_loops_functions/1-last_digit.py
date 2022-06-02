#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digt = number % 10 if number >= 0 else ((-number % 10) * -1)
message = f"Last digit of {number} is {last_digt}"
if (last_digt > 5):
    print(f"{message} and is greater than 5")
elif (last_digt == 0):
    print(f"{message} and is zero")
elif (last_digt < 6) and (last_digt != 0):
    print(f"{message} and is less than 6 and not 0")
