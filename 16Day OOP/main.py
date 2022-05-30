from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_Mach= MoneyMachine()
coffee_Make=CoffeeMaker()
menu=Menu()
powerOn=True


while powerOn:
    objects=menu.get_items()
    choose=input(f"What is your choice ? {objects} ")
    if choose=="off":
        powerOn=False
    elif choose=="report":
        money_Mach.report()
        coffee_Make.report()
    else:
        drink=menu.find_drink(choose)
        if coffee_Make.is_resource_sufficient(drink)and money_Mach.make_payment(drink.cost):
            coffee_Make.make_coffee(drink)
    
    
