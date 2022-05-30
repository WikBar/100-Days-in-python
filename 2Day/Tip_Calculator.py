print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
people=int(input("How many people to split the bill? "))
tip=int(input("What percentage tip would you like to give? 10, 12 or 15. "))
result=(bill+float((tip/100)))/people
print("Each person should pay: ${:.2f}".format(result))