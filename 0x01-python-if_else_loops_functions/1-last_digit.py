#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
jam = number % 10
if jam > 5:
    print(f"Last digit of {number:d} is {jam:d} and is greater than 5")
elif jam == 0:
    print(f"Last digit of {number:d} is {jam:d} and is 0")
elif jam < 6:
    print(f"Last digit of {number:d} is {jam:d} and is less than 6 and not 0")
