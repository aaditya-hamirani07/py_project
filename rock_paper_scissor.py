import random
l1=["rock","paper","scissor"]
d1={
    "rock,paper":"paper",
    "paper,scissor":"scissor",
    "rock,scissor":"rock",
    "paper,rock":"paper",
    "scissor,paper":"scissor",
    "scissor,rock":"rock"
}
def game(x):
    count = 0
    p1_win = 0
    p2_win = 0

    while(count!=x):
        print()
        count += 1
        p1 = input("Enter you choice: ").lower()
        p2 = random.choice(l1)
        print("Bot's choice:",p2)
        key = f"{p1},{p2}"
        winner_round = d1.get(key)
        if (winner_round==p1):
            print(f"Player won round {count}")
            p1_win += 1
        elif(winner_round==p2):
            print(f"Bot won round {count}")
            p2_win += 1
        else:
            print(f"Round {count} is a tie.")

    if(p1_win>p2_win):
        print("Player won the tournament!!!".center(150))
    elif(p2_win>p1_win):
        print("Bot won the tournament!!!".center(150))
    else:
        print("Tournament ended in tie!!!".center(150))


print("Welcome to game of Rock-Paper-Scissor!!".center(150))
while True:
    a = int(input("\n\nEnter the number of rounds for the Rock-Paper-Scissor tournament: "))
    game(a)
    b=int(input("Enter 1 for playing again , 0 for exit: "))
    if(b!=1):
        break


