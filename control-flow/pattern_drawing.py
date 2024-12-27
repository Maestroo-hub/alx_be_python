while True:
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a positive integer.")
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row += 1

