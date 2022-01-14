
name=input("What is your name?")#Checks whether the name is AURTHER 
if name.upper()=="AURTHUR":#If the name is aurther it show the oupt below
    print("My liege! You may pass!")
else:
    seek=input("What do you seek?")#Asks for another input 
    if "GRAIL" in seek.upper(): #checks whether the input contains grail or not
        #if yes it ask for another input
        colour=input("What is your favourite colour?")
        #checks whether the first letter of the name matches the name of the color
        if name[0].upper() == colour[0].upper():
            print("You may pass!!")
        else:
        #if the first letter doesn't match it gives this output
            print("You may not pass!!")
    else:
        #if there is no "grail" in the statement it gives this output
        print("You may not pass!!")
