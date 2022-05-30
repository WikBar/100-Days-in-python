MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0
}

def insertCoins():
    quarters=int(input("How many quarters?"))
    dimes=int(input("How many dimes?"))
    nickles=int(input("How many nickles?"))
    pennies=int(input("How many pennies?"))
    return quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01  

def report():
    for x in resources:
            print(x, ':', resources[x])


powerOn=True
while powerOn:
    choose=input("What would you like to drink? cappucino/latte/espresso")
    if choose.lower() == "report":
        report()
    if choose.lower() in MENU:
        pay=insertCoins()
        if pay>=MENU[choose]["cost"]:
            resources["money"]=resources["money"]+MENU[choose]["cost"]
            for x in resources:
                if x in MENU[choose]["ingredients"]:
                    resources[x]=resources[x]-MENU[choose]["ingredients"][x]
            change=pay-MENU[choose]["cost"]
            report()
        else:
            print("Not enought resorces")
            continue
        print("You paid : %.2f" % pay)
        print("Your change : %.2f" % change)
    
    