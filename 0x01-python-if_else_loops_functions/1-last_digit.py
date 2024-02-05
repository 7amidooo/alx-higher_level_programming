#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
    x = number % 10
    y = number
    y *= -1
    if number % 10 > 5:
        print(f"Last digit of -{number} is -{x} and is greater than 5")
    elif number % 10 == 0:
        print("Last digit of -", number, "is", number % 10, "and is 0")
    else:
        print(f"Last digit of number {y} is -{x} and is less than 6 and not 0")
else:
    x = number % 10
    if number % 10 > 5:
        print("Last digit of", number, "is", x, "and is greater than 5")
    elif number % 10 == 0:
        print("Last digit of", number, "is", number % 10, "and is 0")
    else:
        print("Last digit of", number, "is", x, "and is less than 6 and not 0")
