from data import data
import random

def formatPerson(account):
    """"fomating a person from Instagram and returning him in string"""
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name}, {description} which comes from {country}" 

def compare(accountA,accountB,choice):
    
    a=accountA["follower_count"]
    b=accountB["follower_count"]
    if choice=="yes":
        if a>b:
            return 0
        else:
            0
        
gameOver=False
score=0
accountA=random.choice(data)
accountB=random.choice(data)
if accountA==accountB:
    accountB=random.choice(data)



while not gameOver:
    
    print("Welcome in the game MORE LESS ")
    print("What u think a ",formatPerson(accountA)," is more popular than ", formatPerson(accountB),"?" )
    choice=input().lower()
    
    if compare(accountA,accountB,choice)==0:
        gameOver=True
    else:
        accountA=accountB
        accountB=random.choice(data)
        score+=1

print(f"Your score is: {score}")