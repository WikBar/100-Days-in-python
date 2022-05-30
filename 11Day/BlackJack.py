import random

def giveCard(Cards):
    pool=[2,3,4,5,6,7,8,9,10,10,10,10,11]
    card=random.randint(0,12)
    Cards.append(pool[card])
    return Cards

def sumOfCards(Cards):
    
    if 11 in Cards and 10 in Cards and len(Cards)==2:
        return 0
    if 11 in Cards and sum(Cards)>21:
        Cards.remove(11)
        Cards.append(1)
        return sum(Cards)
    return sum(Cards)


    
def compare(yourCards,computerCards):
    if sumOfCards(yourCards)==0 :
        print("Black Jack. You win !!!")
    elif sumOfCards(computerCards)>21:
        print("Opponent has Lost. You Win!!!")
    elif sumOfCards(yourCards)==sumOfCards(computerCards):
        print("Draw")
    elif sumOfCards(yourCards)>21:
        print("Bust! ! !")
    elif sumOfCards(computerCards)==0:
        print("Oponnent has a Black Jack")
    
    while sum(computerCards)<17:
        giveCard(computerCards)
    return computerCards


start=input("Welcome in Black Jack game lets play a game.\nSay 'y' to start")

yourCards=[]
computerCards=[]
gameOver=False

for _ in range(2):
    giveCard(yourCards)
    giveCard(computerCards)
    
print(yourCards)
print(sumOfCards(yourCards))
print(computerCards[0])
if sumOfCards(yourCards)==0:
    print("Black Jack. You win !!!")
    gameOver=True
    
while not gameOver:

    print(yourCards)
    print(sumOfCards(yourCards))
    print("You want another card?\nSay 'hit' to take another card\nSay 'Stand' to end your turn")
    answer=input("Say: ").lower()
    if answer=="hit":
        yourCards=giveCard(yourCards)
    elif answer=="stand":
        while sum(computerCards)<17 or sum(computerCards)==0:
            giveCard(computerCards)
        print(computerCards)
    compare(yourCards,computerCards)
    if input("You want to play again?").lower()=="no":
        gameOver=True






