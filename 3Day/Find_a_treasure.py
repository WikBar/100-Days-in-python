def main():
    print("Welcome to Treasue Island.\nYour mission is to find the treasuere.")
    beach=input("You are on the beach you are going to the left or right?\n")
    if beach.lower()=="right":
        return 0
    if beach.lower()=="left":
        see=input("You are going to the see u swim or wait for the boat\n")
        if see.lower()=="swim":
            return 0
        if see.lower()=="wait":
            door=input("You see 3 doors yellow, red and Blue? Which u will open?\n")
            if door.lower()=="red" or door.lower=="blue":
                return 0
            if door.lower()=="yellow":
                print("You win a treasure!!!")
                return 0    

main()