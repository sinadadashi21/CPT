import sys

row = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]
print("This is a two player game.")
print (row[0:3])
print (row[3:6])
print (row[6:])

def board():
    print (row[0:3])
    print (row[3:6])
    print (row[6:])
    sys.exit()

def tictactoe():
    go = 0
    game = 1
    count = 0

    while game == 1:

        while go != 1:
            print("Positions: 1 is top left, middle left position is 4, bottom left position is 7. Count from left to right starting from the top left.")
            position = int(input("Which position do you want to put an x in? "))

            if row[position-1] == " ":
                row[position-1] = "x"
                go = 1
                count = count + 1

            else:
                print("That position has been taken")

            if row[0] == "x" and row[1] == "x" and row [2] == "x":
                print("X wins!")
                board()

            elif row[3] == "x" and row[4] == "x" and row [5] == "x":
                print("X wins!")
                board()

            elif row[6] == "x" and row[7] == "x" and row [8] == "x":
                print("X wins!")
                board()

            elif row[0] == "x" and row[3] == "x" and row [6] == "x":
                print("X wins!")
                board()

            elif row[1] == "x" and row[4] == "x" and row [7] == "x":
                print("X wins!")
                board()

            elif row[2] == "x" and row[5] == "x" and row [8] == "x":
                print("X wins!")
                board()

            elif row[0] == "x" and row[4] == "x" and row [8] == "x":
                print("X wins!")
                board()

        print(row[0:3])
        print(row[3:6])
        print(row[6:])

        go = 0

        if count == 9:
            print("Game over, it's a draw")
            sys.exit()

        while go != 1:
            print("Positions: 1 is top left, middle left position is 4, bottom left position is 7")
            position = int(input("Which position do you want to put an o in? "))

            if row[position-1] == " ":
                row[position-1] = "o"
                go = 1
                count = count + 1

            else:
                print("That position has been taken")

            if row[0] == "o" and row[1] == "o" and row [2] == "o":
                print("O wins!")
                board()

            elif row[3] == "o" and row[4] == "o" and row [5] == "o":
                print("O wins!")
                board()

            elif row[6] == "o" and row[7] == "o" and row [8] == "o":
                print("O wins!")
                board()

            elif row[0] == "o" and row[3] == "o" and row [6] == "o":
                print("O wins!")
                board()

            elif row[1] == "o" and row[4] == "o" and row [7] == "o":
                print("O wins!")
                board()

            elif row[2] == "o" and row[5] == "o" and row [8] == "o":
                print("O wins!")
                board()

            elif row[0] == "o" and row[4] == "o" and row [8] == "o":
                print("O wins!")
                board()
            

        print(row[0:3])
        print(row[3:6])
        print(row[6:])

        go = 0

        if count == 9:
            print("Game over, it's a draw")
            sys.exit()

tictactoe()