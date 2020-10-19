# Import random module
import random
# Import math module
import math


# Function that will calculate the grid
def calculate_grid(m, s, d, c):
    poss = True
    surp = 0
    for j in range(len(m)):
        diff = m[j] - c[j]
        s[j] = 0
        d[j] = 0
        if diff > 3:
            diff -= 3
            s[j] = diff
            surp += diff
        elif diff < 0:
            diff *= -1
            d[j] = diff
            surp -= 2 * diff
            poss = False
    if poss:
        return 100
    else:
        return surp


# Function to display the grid
def display_grid(m, s, d, c, name):
    col_width = 5
    print("{:<15}{:^{width}}{:^{width}}{:^{width}}{:^{width}}{:^{width}}".format("Class", "Str", "Int", "Wis", "Dex", "Con", width=col_width))

    print_str = "{:<15}".format("Base Score")
    for j in m:
        print_str += "{:^{width}}".format(j, width=col_width)
    print(print_str)

    print_str = "{:<15}".format(name)
    for j in c:
        print_str += "{:^{width}}".format(j, width=col_width)
    print(print_str)

    print_str = "{:<15}".format("Surplus")
    for j in s:
        print_str += "{:^{width}}".format(j, width=col_width)
    print(print_str)

    print_str = "{:<15}".format("Deficit")
    for j in d:
        print_str += "{:^{width}}".format(j, width=col_width)
    print(print_str)


# Stats goes str, int, wis, dex, con
stats = []
# Surplus stats initially = 0
s_stats = [0, 0, 0, 0, 0]
# Deficit stats initially = 0
d_stats = [0, 0, 0, 0, 0]
# Repeat 5 times
for i in range(5):
    # Add a random number between 3 and 18 to stats
    stats += [random.randint(3, 18)]
# Class stats initially = 0
c_stats = [0, 0, 0, 0, 0]
# Create a variable called class_choice and make it equal 0
class_choice = ""
# Create a variable called surplus and make it equal 0
surplus = 0
# Create a variable called chances and make it equal 5
chances = 5
# Create a boolean variable called possible and make it equal False
possible = False

# Prompt the user to input a choice between 1-4, call this choice
choice = int(input("Choose your class:\n 1.Warrior\n 2.Wizard\n 3.Thief\n 4.Necromancer\n"))
# If the user selects warrior
if choice == 1:
    # Min stats for warrior
    c_stats = [15, 0, 0, 12, 10]
    # Modify class_choice to equal Warrior
    class_choice = "Warrior"
# If the user selects wizard
elif choice == 2:
    # Min stats for wizard
    c_stats = [0, 15, 10, 10, 0]
    # Modify class_choice to equal Wizard
    class_choice = "Wizard"
# If the user selects Thief
elif choice == 3:
    # Min stats for thief
    c_stats = [10, 9, 0, 15, 0]
    # Modify class_choice to equal Thief
    class_choice = "Thief"
# If the user selects necromancer
elif choice == 4:
    # Min stats for necromancer
    c_stats = [10, 10, 15, 0, 0]
    # Modify class choice to equal Necromancer
    class_choice = "Necromancer"
# If the user inputs anything else other than a number between 1-4
else:
    # Print not a valid input
    print("{} is not a valid input".format(choice))
    # Modify possible to equal True
    possible = True

# While possible is equal to False and chances is greater than 0
while possible == False and chances > 0:
    # Calculate the surplus
    surplus = calculate_grid(stats, s_stats, d_stats, c_stats)
    # Display the grid
    display_grid(stats, s_stats, d_stats, c_stats, class_choice)
    # If the surplus variable is equal to 100
    if surplus == 100:
        # Modify the possible variable to equal True
        possible = True

    # If the possible variable is equal to True
    if possible:
        # Print you have created (selected) class
        print("You have created a {}!".format(class_choice))
    # If the possible variable is equal to False
    else:
        # If the surplus is less than 0
        if surplus < 0:
            # Print user does not have enough points to create (selected) class
            print("You do not have enough attribute points to create a {}".format(class_choice))
            # Modify chances to equal 0
            chances = 0
        # Else if surplus is greater than 0
        else:
            # Create a variable called take and make it equal 0
            take = 0
            # Create a variable called give and make it equal 0
            give = 0
            # Create a variable called amount and make it equal 0
            amount = 0
            # Print how many chances the user has remaining
            print("You have {} chances remaining to move attribute points (2 surplus points to make 1 deficit point)".format(chances))
            # Ask the user to enter the stats to take points from and modify the take variable
            take = int(input("Choose which stats to take points from (1=str|2=int|3=wis|4=dex|5=con): "))
            # Ask the user to enter the stats to give points to and modify the give variable
            give = int(input("Choose which stats to give points to (1=str|2=int|3=wis|4=dex|5=con): "))
            # Ask the how many points should be taken away
            amount = int(input("How many points should be moved across (2:1 move ratio (input will be rounded down to a multiple of 2)): "))

            # Create a variable called not_changed and make it equal True
            not_changed = True
            if 0 < take < 6:
                amount = min(amount, s_stats[take-1])
                amount = int(math.floor(amount / 2) * 2)
                if amount > 0:
                    stats[take-1] -= amount
                    not_changed = False

            # If the not_changed variable is equal to True
            if not_changed:
                # Print no changes made (because of invalid input)
                print("No changes made as {} is not a valid input to take from".format(take))
            # Else if not_changed is equal to False
            else:
                # Amount is equal to amount divided by 2 rounded down the the nearest integer
                amount = int(amount / 2)
                if 0 < give < 6:
                    stats[give - 1] += amount
                else:
                    print("{} is not a valid input to give to, so points have been added to constitution".format(give))
                    stats[4] += amount
                chances -= 1
if chances == 0 and possible == False:
    print("You have run out of chances to make a {} class. Restart to try again".format(class_choice))