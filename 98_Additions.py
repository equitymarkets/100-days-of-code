#Day 98: Here is the while loop and some other data enabling multiple runs of my Day 24 and Day 49 refactored programs. 
#(Please indent even with if statement for each day's function.)

choice = True

while choice == True:
    day_number = input("Please enter a Day Number to view my work for that day.")
    
#Body

choose = input("Would you like to run the program again? Type Y/N.")

    if choose == 'Y':
        choice = True
    else:
        print("Goodbye!")
        quit()
