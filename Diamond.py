width = int(input("Enter size of the diamond: "))
if width < 2:
    width = 2
elif width > 40:
    width = 40

d_width = width * 2
for i in range(width):
    display = "*"
    for j in range(i):
        display += " *"
    print("{:^{width}}".format(display, width=d_width))
for i in range(width - 1):
    display = "*"
    for j in range(width - i - 2):
        display += " *"
    print("{:^{width}}".format(display, width=d_width))

