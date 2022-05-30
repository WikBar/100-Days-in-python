import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pull=[letters,numbers,symbols]


lenght=nr_numbers+nr_symbols+nr_letters
password=[]

while lenght!=0:
    
    letter=random.randint(0,len(pull[0])-1)
    number=random.randint(0,len(pull[1])-1)
    symbol=random.randint(0,len(pull[2])-1)
    pullrand=random.randint(0,len(pull))
    
    if pullrand==0 and nr_letters!=0:
        password.append(pull[0][letter])
        nr_letters-=1
    if pullrand==1 and nr_numbers!=0:
        password.append(pull[1][number])
        nr_numbers-=1
    if pullrand==2 and nr_symbols!=0:
        password.append(pull[2][symbol])
        nr_symbols-=1
    lenght=nr_numbers+nr_symbols+nr_letters
print(password)