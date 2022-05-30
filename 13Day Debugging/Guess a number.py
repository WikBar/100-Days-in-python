import random
LOW_LEVEL=10
HIGH_LEVEL=5
chance=0
print("Welcome in a game 'Guess a number'")
level=input("Choose a difficulty level easy or hard\n").lower()
if level=="easy":
    chance=LOW_LEVEL
elif level=="hard":
    chance=HIGH_LEVEL
    
number=random.randint(0,100)

guess=int(input(f"Try to guessa number You have a {chance} chances\n"))

while number!=guess or chance!=0:
    chance-=1
    if chance==0:
        print("You lose")
        break
    elif number==guess:
        print("You Win!!")
        break
    
    if number>guess:
        print("It's to low")
    elif number<guess:
        print("It's to high")
    guess=int(input(f"Try Again! You have a {chance} chances\n"))
    
