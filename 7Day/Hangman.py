import random
before=[]
fail=0
words=['mysz','lizak',"tragedia","zapierdol"]
wordIndex=random.randint(0,len(words))
word=words[wordIndex]
guess="_"*len(word)

while fail<8 or guess.isalpha():

    print("".join(guess))    
    letter=input("Wpisz literę aby uratować wisielca\n").lower()
    before.append(letter)
    
    for i in range(len(word)):
        
        if word[i].lower()==letter: 
            guess=guess[:i] +letter+guess[i+1:]
        elif word[i].lower!=letter:
            if not word[i].isalpha():
                guess=guess[:i] +"_"+guess[i+1:]
        
        if guess.isalpha():
            print("You won")
            break
        if fail>=7:
            print("You fail")
            break
    if letter not in guess:
        
        fail+=1
        print(f"Jest to {fail} próba")