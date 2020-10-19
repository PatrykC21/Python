print("Main dishes are:")
print("1. Lasagne")
print("2. Stir Fry")
main_dish = int(input("Please select dish: "))

if main_dish == 1:
    print("Side dishes are:")
    print("1. Garlic bread")
    print("2. Fries")
    side_dish = int(input("Please select side dish: "))
    if side_dish == 1:
        print("You have selected Lasagne with garlic bread")
    elif side_dish == 2:
        print("You have selected Lasagne with fries")
    else:
        print("Invalid item selected")
elif main_dish == 2:
    print("Side dishes are:")
    print("1. Crispy Seaweed")
    print("2. Noodles")
    side_dish = int(input("Please select side dish: "))
    if side_dish == 1:
        print("You have selected Stir Fry with  Crispy Seaweed")
    elif side_dish == 2:
        print("You have selected Stir Fry with Noodles")
    else:
        print("Invalid item selected")
else:
    print("Invalid item selected")