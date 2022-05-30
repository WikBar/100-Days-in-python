import random

scissors="scissors"
paper="paper"
rock="rock"

game=[scissors,paper,rock]

throw=random.randint(0,2)

player=int(input("choose one: 0.paper, 1.rock, 2.scissors\n"))
if player<3 and player>-1:

    print(f"Computer choose {game[throw]}, Player choose {game[player]}")
    if throw==player:
        print("Draw")
    if throw+1==player:
        print("Lose")
    if throw-1==player:
        print("Win")
else:
    print("Wrong, you lose")

