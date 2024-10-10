import random

MINIMUM = 1
MAXIMUM = 45
COLUMN_AMOUNT = 6
number_of_lines = int(input("How many quick picks? "))
for i in range(number_of_lines):
    numbers = []
    for j in range(COLUMN_AMOUNT):
        number = random.randint(MINIMUM, MAXIMUM)
        numbers.append(number)
    numbers.sort()
    print("  ".join(f"{number:2}" for number in numbers))
