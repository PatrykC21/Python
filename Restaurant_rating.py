print(" Rate our restaurant 1-5\n 5 == Very Good\n 1 == Very Bad\n -1 == Quit the program")
rating_li = []

while True:
    try:
        rate = int(input("Rating:"))
        if rate in range(1, 6):
            rating_li.append(rate)
        elif rate == -1:
            title = "|    Customers    |    Rating    |"
            horizontal = "|" + "_" * 17 + "_" * 17 + "|"
            print(horizontal + "\n" + title, "\n", horizontal, "\n",
                  "|", rating_li.count(1), "Customers    |    1 star    |", "\n"
                                                                            "|", rating_li.count(2),
                  "Customers    |    2 stars    |", "\n"
                                                    "|", rating_li.count(3), "Customers    |    3 stars    |", "\n"
                                                                                                               "|",
                  rating_li.count(4), "Customers    |    4 stars    |", "\n"
                                                                        "|", rating_li.count(5),
                  "Customers    |    5 stars    |", "\n")
            count = len(rating_li)
            total = sum(rating_li)
            avr = total / count
            print("Total amount of ratings:", count)
            print("Average rating:", round(avr))
            break
        else:
            print("Please rate restaurant with a number between 1-5")
    except ValueError:
        print("Please enter a required number:")
        pass
    except ZeroDivisionError:
        print("No ratings inputted")
        pass
