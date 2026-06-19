import random

dice = {
    1:["-------","|     |","|  *  |","|     |","-------"],
    2:["-------","| *   |","|     |","|   * |","-------"],
    3:["-------","| *   |","|  *  |","|   * |","-------"],
    4:["-------","| * * |","|     |","| * * |","-------"],
    5:["-------","|*   *|","|  *  |","|*   *|","-------"],
    6:["-------","| * * |","| * * |","| * * |","-------"],
}

snake = {
    30:7,47:13,56:19,73:51,98:2,92:75,82:42
}

ladder = {
    4:25,26:67,43:76,59:80,71:93,29:69
}

board = []
p1_location=0
p2_location=0

def print_board():
    num = 100
    for row in range(10):
        current_row = []
        for col in range(10):
            current_row.append(num)
            num -= 1
        if row % 2 == 1:
            current_row.reverse()
        board.append(current_row)
    for row in board:
        print(" | ".join(f"{cell:3}" for cell in row).center(100))
        print(("-" * 58).center(100))

def board_updation():
    for r in board:
        row_str = []
        for cell in r:
            if cell == p1_location and cell == p2_location:
                row_str.append(f"{'P1/P2':5}")
            elif cell == p1_location:
                row_str.append(f"{'P1':3}")
            elif cell == p2_location:
                row_str.append(f"{'P2':3}")
            else:
                row_str.append(f"{cell:3}")
        print(" | ".join(row_str).center(100))
        print(("-" * 58).center(100))

def condition_checker():
    global flag , p1_location , p2_location , p1_dice , p2_dice
    if(p1_location==100):
            board_updation()
            print("congratulations player 1 win !!!".center(100))
            exit()
    elif(p2_location==100):
            board_updation()
            print("congratulations player 2 win !!!".center(100))
            exit()
    elif (p1_location>100):
        p1_location -= p1_dice
        print("Number should be less than ",(101-p1_location))
    elif (p2_location>100):
        p2_location -= p2_dice
        print("Number should be less than ",(101-p2_location))
    elif (p1_location in snake):
        print(f"Player 1 got bitten by a snake at {p1_location} and slid down to {snake[p1_location]}!")
        p1_location = snake.get(p1_location)
    elif (p2_location in snake):
        print(f"Player 2 got bitten by a snake at {p2_location} and slid down to {snake[p2_location]}!")
        p2_location = snake.get(p2_location)
    elif (p1_location in ladder):
        print(f"Player 1 climbed a ladder from {p1_location} up to {ladder[p1_location]}!")
        p1_location = ladder.get(p1_location)
    elif (p2_location in ladder):
        print(f"Player 2 climbed a ladder from {p2_location} up to {ladder[p2_location]}!")
        p2_location = ladder.get(p2_location)
    
def coordinates_P1():
    global row_player1 , column_player1
    row_player1 = (100-p1_location)//10
    column_player1 = (p1_location-1)%10

def coordinates_P2():
    global row_player2 , column_player2
    row_player2 = (100-p2_location)//10
    column_player2 = (p2_location-1)%10


def dice_printing(x):
    for line in dice[x]:
        print(line.center(25))

print("Welcome to game of snake and ladder".center(100))
print()
print_board()
while True:
    flag = 0
    a=input("P1 Enter Y for rolling die: ")
    p1_dice=random.randint(1,6)
    print(f"You got {p1_dice}")
    p1_location += p1_dice
    dice_printing(p1_dice)
    condition_checker()
    coordinates_P1()
    board_updation()

    flag = 0
    b=input("P2 Enter Y for rolling die: ")
    p2_dice=random.randint(1,6)
    print(f"You got {p2_dice}")
    p2_location += p2_dice
    dice_printing(p2_dice)
    condition_checker()
    coordinates_P2()
    board_updation()