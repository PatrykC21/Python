import random

count = 0

while True:
    dice = random.randint(1, 6)
    count += 1
    print("Dice value:", dice)

    if dice == 6:
        break
    print("Number of throws:", count)
print("Total number of throws:", count)