import random


def card_generator(card):
    if card == 14:
        card_value = "Ace"
    elif card == 11:
        card_value = "Jack"
    elif card == 12:
        card_value = "Queen"
    elif card == 13:
        card_value = "King"
    else:
        card_value = str(card)

    return card_value


choice = 0
correct = True
card1 = random.randint(2, 14)
card2 = card1
counter = 0

print("Current Card: {}".format(card1))

while choice != -1 and correct:
    player = int(input("Next card will be Higher or Lower? (-1 = stop | 1 = higher | 2 = lower"))
    if player == 1 or player == 2:
        card1 = random.randint(2, 14)
        if (card1 >= card2 and player == 1) or (card1 <= card2 and player == 2):
            counter += 1
            print("CORRECT!\nOld card was {} and new card is {}".format(card_generator(card2), card_generator(card1)))
        else:
            correct = False
            print("WRONG!\nThe old card was {} and new card is {}".format(card_generator(card2), card_generator(card1)))
        card2 = card1
    elif choice != -1:
        print("Invalid input, Try again!")
print("You got {} guesses right".format(counter))
