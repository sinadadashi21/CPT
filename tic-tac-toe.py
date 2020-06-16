
import sys
go = 0
game = 1
count = 0

row = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]

while game == 1:

    while go != 1:
        position = int(input("Which position do you want to put an x in? "))

        if row[position-1] == " ":
            row[position-1] = "x"
            go = 1
            count = count + 1

        else:
            print("That position has been taken")

    print(row[0:3])
    print(row[3:6])
    print(row[6:])

    go = 0

    if count == 9:
        print("Game over, it's a draw")
        sys.exit()

    while go != 1:
        position = int(input("Which position do you want to put an o in? "))

        if row[position-1] == " ":
            row[position-1] = "o"
            go = 1
            count = count + 1

        else:
            print("That position has been taken")

    print(row[0:3])
    print(row[3:6])
    print(row[6:])

    go = 0

    if count == 9:
        print("Game over, it's a draw")
        sys.exit()