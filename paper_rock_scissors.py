import random
player_score = 0
pc_score = 0
win_score = 3
e_types = ["Rock", "Paper", "Scissors"]


def find_input_index(s):
    for i in range(len(e_types)):
        if e_types[i].lower() == s.lower():
            return i
    return -1


while player_score < win_score and pc_score < win_score:
    pc_index = random.randint(0, 2)
    player_type = input("Enter your selection (Rock|Paper|Scissors): ")
    player_index = find_input_index(player_type)
    if player_index == -1:
        print("Invalid input, try again")
    else:
        print("You chose: {}".format(e_types[player_index]))
        print("The computer chose: {}".format(e_types[pc_index]))
        if pc_index == player_index:
            # Draw
            print("It was a draw!")
        elif player_index - pc_index == -1:
            # PC Win
            print("The computer won")
            pc_score += 1
        elif player_index - pc_index == 2:
            # PC Win
            print("The computer won")
            pc_score += 1
        else:
            # Player Win
            print("Congratulations, you win!")
            player_score += 1
        print("You need: {} to win\nThe computer needs: {} to win".format(win_score - player_score, win_score - pc_score))
        print("****************************")
if player_score == win_score:
    print("Congratulations, you won! :)")
else:
    print("Commiserations, the computer won :(")
