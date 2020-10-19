first = int(input("Enter first number:"))


print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Reminder")

reason = int(input("Select function: "))
second = int(input("Enter second number:"))


def calc():
    if reason == 1:
        total = first + second
        print(first, "+", second, "=", total)
    elif reason == 2:
        total = first - second
        print(first, "-", second, "=", total)
    elif reason == 3:
        total = first * second
        print(first, "*", second, "=", total)
    elif reason == 4:
        total = first / second
        if second == 0:
            print("You can not divide by zero")
        else:
            print(first, "/", second, "=", total)
    elif reason == 5:
        total = first % second
        print(first, "%", second, "=", total)
    else:
        print("Wrong input")


calc()
