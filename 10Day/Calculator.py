def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

def counting():
    should_continue=True
    print("What is your first number?")
    a=float(input())
    while should_continue:
        print("Select operation\n")
        for key in operations:
            print(key)
        select=input()
        selected=operations[select]
        print("What is your next number")
        b=float(input())
        result=selected(a,b)
        print(f"{a} {select} {b} = {result}")
        print("You want to continue? y or n")
        choose=input()
        
        if choose=="y":
            a=result
        else:
            should_continue=False
            counting()


operations={
    "+":add,
    "-":minus,
    "*":multiply,
    "/":division
}




counting()


