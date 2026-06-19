#  welcome to tic tac toe game

l1=['1','2','3','4','5','6','7','8','9']

print("Welcome to Tic-Tac-Toe game\n".center(100))
def table():
    print(f"{l1[0]} | {l1[1]} | {l1[2]} ".center(100))
    print("----------".center(100))
    print(f"{l1[3]} | {l1[4]} | {l1[5]} ".center(100))
    print("----------".center(100))
    print(f"{l1[6]} | {l1[7]} | {l1[8]} ".center(100))
table()

def table_change_for_X(x):
    match(x):
        case 1:
            l1[0]='X'
        case 2:
            l1[1]='X'
        case 3:
            l1[2]='X'
        case 4:
            l1[3]='X'
        case 5:
            l1[4]='X'
        case 6:
            l1[5]='X'
        case 7:
            l1[6]='X'
        case 8:
            l1[7]='X'
        case 9:
            l1[8]='X'
    table()

def table_change_for_O(y):
    match(y):
        case 1:
            l1[0]='O'
        case 2:
            l1[1]='O'
        case 3:
            l1[2]='O'
        case 4:
            l1[3]='O'
        case 5:
            l1[4]='O'
        case 6:
            l1[5]='O'
        case 7:
            l1[6]='O'
        case 8:
            l1[7]='O'
        case 9:
            l1[8]='O'
    table()

def valid_move(z):
    if l1[z-1] not in ['X','O']:
        return True
    else:
        return False

def table_full():
    l2 = [i for i in l1 if i in ['X', 'O']]
    if (len(l2)==len(l1)):
        return True
    else:
        return False

def condition_checker():
    if( (l1[0]==l1[1]==l1[2]) or (l1[3]==l1[4]==l1[5]) or (l1[6]==l1[7]==l1[8]) ):
        return 1
    elif( (l1[0]==l1[3]==l1[6]) or (l1[1]==l1[4]==l1[7]) or (l1[2]==l1[5]==l1[8]) ):
        return 1
    elif( (l1[0]==l1[4]==l1[8]) or (l1[2]==l1[4]==l1[6]) ):
        return 1
    elif table_full():
        print("Game over , it's a tie".center(100))
        return 1
    else:
        return 0
    
def winner_finder():
    win_condtion = [ (0,1,2) , (3,4,5) , (6,7,8) ,
                     (0,3,6) , (1,4,7) , (2,5,8) ,
                     (0,4,8) , (2,4,6) ]
    for a,b,c in win_condtion:
        if(l1[a]==l1[b]==l1[c]):
            print()
            print(f"Player with {l1[a]} wins!".center(100))

while True:
    num1=condition_checker()
    if (num1==0):
        while True:
            print("Enter number where u want to put X : ")
            a=int(input())
            if valid_move(a):
                table_change_for_X(a)
                break
            else:
                print("Enter a valid move  ")
    else:
        winner_finder()
        break

    num2=condition_checker()
    if (num2==0):
        while True:
            print("Enter number where u want to put O : ")
            b=int(input())
            if valid_move(b):
                table_change_for_O(b)
                break
            else:
                print("Enter a valid move")
    else:
        winner_finder()
        break