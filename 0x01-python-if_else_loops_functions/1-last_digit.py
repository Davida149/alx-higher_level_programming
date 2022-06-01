#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digt = number % 10
last_digt = int(last_digt)
if (last_digit > 5):
    print(f"Last digit of {number} is {last_digt} and is greater than 5")
elif (last_digit == 0):
    print(f"Last digit of {number} is {last_digt} and is zero")
elif (last_digit < 6) and (last_digit != 0):
    print(f"Last digit of {number} is {last_digt} and is less than 6 and not 0)
