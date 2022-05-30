
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clearConsole()

def addNewPlayer():
    clearConsole()
    name=input("What is your name??: ")
    bid=int(input("What's your bid?: $"))

    players[name]=bid
    return players

players={}
AnyOthers="yes"
print("Welcome to the secret auction program.")

while AnyOthers.lower()=="yes":
    
        addNewPlayer()
        AnyOthers=input("Are there any other bidders? Type 'yes' or 'no'")
    
max=0
for i in players:
    if max<players[i]:
        max=players[i]
        winner=i
print("Winner is %s and she/he bid %d" % (winner,max) )

        



