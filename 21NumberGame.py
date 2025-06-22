#Programme for the "21 number game"
import random
import time

def start():#To start the game
    print("Welcome to the 21 Number game\n")
    print('The rules are:\n')
    print('1.You can only enter upto 3 numbers and they have to be positive numbers\n2.The number has to start from 1\n3.You have to enter consecutive numbers\n4.if you get 21 in your turn you lose\n')

    while True:
        level = input("There are three levels\nPlease chose your level\n>>>").lower()
        if level == 'one' or level == '1':
            level1()
        elif level == 'two' or level == '2':
            level2()
        elif level == 'three' or level == '3':
            level3()
        else:
            print("Invalid Input.")

#Checks if it violates rule no.1
def rule1(n):
    if n<=0 and n>3:#checking if the number is between 0 to 3
        print("Wrong!!\nYou violated rule 1")
        lose()

#Checks if it violates rule no.2
def rule2(n_list):
    if n_list[0] != 1:
        print("Wrong!!\nYou violated rule 2")
        lose()

#Checks if it violates rule no.3
def rule3(n_list):
    for i in range(1,len(n_list)):
        if n_list[i]-n_list[i-1] != 1:
            print("\nWrong!!\nYou violated rule 3")
            lose()

#Player has won the game
def won():
    time.sleep(1)
    print("\n\nCONGRATULATIONS!!!")
    time.sleep(1)
    print("\nYOU WON\nTHANK YOU FOR PLAYING\n\nExiting....")
    exit(0)

#Player has lost the game
def lose():
    time.sleep(1)
    print('\n\nYOU LOSE!!\nBETTER LUCK NEXT TIME')
    exit(0)


'''
Gives the last number

The reason for this function is that 
if the user chooses to start second 
then the computer needs to start with 1
hence not violating rule 2

'''
def lastno(n_list):
    if n_list == []:
        last_number = 0
    else:
        last_number = n_list[-1]
    return last_number



'''
This is used to find
the closest number after the last number
which is a multiple of 4
but it does not include the last number

'''
def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near


'''
This is used to find how many numbers it must input
for it to maximize its probability to win the game
by finding the nearest multiple of 4 and subtracting it with the last number

This function is only used in level 3

'''
def computerNumber(n_list):
    if n_list == []:
        comp = 1
    else:
        last_number = n_list[-1]
        near = nearestMultiple(last_number)
        comp = near - last_number
        if comp == 4:
            comp = 3
    return comp

#Checks if the last number that the Player entered is greater than or equal to 21
def checkForPlayer(number):
    if number >= 21:
        lose()

#Checks if the last number that the Computer entered is greater than or equal to 21
def checkForComputer(number):
    if number >= 21:
        won()
        
########################################################################################################################

#LEVEL 1
def level1():
    print('Enter F to take first chance\nEnter S to take second chance')#asking user for first or second chance
    ch = input('>>> ').lower()
    n_list =[] #creating an empty list for storing the numbers

    #Player starting first
    if ch == 'f':
        while True:
            #Player's turn

            n = int(input("How many numbers do you want to enter?\n>>> "))
            rule1(n)
            
            print(f"Enter the {n} values")
            number = list(map(int,input().split()))
            for i in range(n):
                try:
                    n_list.append(number[i])#adding the numbers into the list
                except:
                    print("Oops! You violated rule 4")
                    lose()
            
            rule2(n_list)
            rule3(n_list)#To check if the numbers are consecutive
            last_number = n_list[-1]#last number added in the list
            checkForPlayer(last_number)


            #Now computer's turn

            comp = random.randint(1,3)
            for j in range(comp):
                n_list.append(last_number+j+1)
            last_number = n_list[-1]
            print("The input(s) computer gave are:",n_list[-comp::])
            checkForComputer(last_number)            

    #Computer starting first
    elif ch == 's':
        while True:
            #computer's turn

            comp = random.randint(1,3)
            last_number = lastno(n_list)
            
            for i in range(comp):
                n_list.append(last_number+i+1)
            
            print("The input(s) computer gave are:",n_list[-comp::])
            last_number = n_list[-1]
            checkForComputer(last_number)
          

            #Now Player's turn

            n = int(input("How many numbers do you want to enter?\n>>> "))     
            rule1(n)
            
            print(f"Enter the {n} values")
            number = list(map(int,input().split()))
            for i in range(n):
                try:
                    n_list.append(number[i])#adding the numbers into the list
                except:
                    print("Oops! You violated rule 4")
                    lose()

            rule3(n_list)#To check if the numbers are consecutive
            last_number = n_list[-1]#last number added in the list
            checkForPlayer(last_number)
    else:
        print("\nWrong Input!!\n")
        lose()


####################################################### Next Level ######################################################

#LEVEL 2
def level2():
    print('Enter F to take first chance\nEnter S to take second chance')#asking user for first or second chance
    ch = input('>>> ').lower()
    n_list = list()#creating an empty list for storing the numbers

    #Player starting first
    if ch == 'f':
        while True:
            #Player's turn

            n = int(input("How many numbers do you want to enter?\n>>> "))
            
            if n>0 and n<=3:#checking if the number is between 0 to 3
                comp = 4 - n #the number of values computer is going to give
            else:
                rule1(n)
            
            print(f"Enter the {n} values")
            number = list(map(int,input().split()))
            for i in range(n):
                try:
                    n_list.append(number[i])#adding the numbers into the list
                except:
                    print("Oops! You violated rule 4")
                    lose()
            
            rule2(n_list)
            rule3(n_list)#To check if the numbers are consecutive
            last_number = n_list[-1]#last number added in the list
            checkForPlayer(last_number)

            #Now computer's turn

            for j in range(comp):
                n_list.append(last_number+j+1)
            last_number = n_list[-1]
            print("The input(s) computer gave are:",n_list[-comp::])
            checkForComputer(last_number)
            
    #Computer starting first
    elif ch == 's':
        while True:
            #computer's turn

            comp = random.randint(1,3)
            last_number = lastno(n_list)
            
            for i in range(comp):
                n_list.append(last_number+i+1)
            
            print("The input(s) computer gave are:",n_list[-comp::])
            last_number = n_list[-1]
            checkForComputer(last_number)
          

            #Now Player's turn

            n = int(input("How many numbers do you want to enter?\n>>> "))
            
            rule1(n)
            
            print(f"Enter the {n} values")
            number = list(map(int,input().split()))
            for i in range(n):
                try:
                    n_list.append(number[i])#adding the numbers into the list
                except:
                    print("Oops! You violated rule 4")
                    lose()

            rule3(n_list)#To check if the numbers are consecutive
            last_number = n_list[-1]#last number added in the list
            checkForPlayer(last_number)
    else:
        print("\nWrong Input!!\n")
        lose()


####################################################### Next Level ######################################################

#LEVEL 3
def level3():
    print('Enter F to take first chance\nEnter S to take second chance')#asking user for first or second chance
    ch = input('>>> ').lower()
    n_list = list()#creating an empty list for storing the numbers

    #Player starting first
    if ch == 'f':
        while True:
            #Player's turn

            n = int(input("How many numbers do you want to enter?\n>>> "))
            
            if n>0 and n<=3:#checking if the number is between 0 to 3
                comp = 4 - n #the number of values computer is going to give
            else:
                rule1(n)
            
            print(f"Enter the {n} values")
            number = list(map(int,input().split()))
            for i in range(n):
                try:
                    n_list.append(number[i])#adding the numbers into the list
                except:
                    print("Oops! You violated rule 4")
                    lose()
            
            rule2(n_list)
            rule3(n_list)#To check if the numbers are consecutive
            last_number = n_list[-1]#last number added in the list
            checkForPlayer(last_number)

            #Now computer's turn

            for j in range(comp):
                n_list.append(last_number+j+1)
            last_number = n_list[-1]
            print("The input(s) computer gave are:",n_list[-comp::])
            checkForComputer(last_number)
            
    #Computer starting first
    elif ch == 's':
        while True:
            #computer's turn

            comp = computerNumber(n_list)
            last_number = lastno(n_list)
            
            for i in range(comp):
                n_list.append(last_number+i+1)
            
            print("The input(s) computer gave are:",n_list[-comp::])
            last_number = n_list[-1]
            checkForComputer(last_number)
          

            #Now Player's turn

            n = int(input("How many numbers do you want to enter?\n>>> "))  
            rule1(n)
            
            print(f"Enter the {n} values")
            number = list(map(int,input().split()))
            for i in range(n):
                try:
                    n_list.append(number[i])#adding the numbers into the list
                except:
                    print("Oops! You violated rule 4")
                    lose()

            rule3(n_list)#To check if the numbers are consecutive
            last_number = n_list[-1]#last number added in the list
            checkForPlayer(last_number)

    else:
        print("\nWrong Input!!\n")
        lose()


########################################################################################################################


#Main program
def main():
    while True:
        print ("Player 2 is a Computer.")
        print("Do you want to play the 21 number game? (yes / no)")
        inp1 = input('>>> ')
        if inp1 =='yes':
            start()
        else:
            print ("Do you want quit the game?(yes / no)")
            inp2 = input('>>> ')
            if inp2 == "yes":
                print ("You are quitting the game...")
                exit(0)
            elif inp2 == "no":
                print ("Continuing...")
            else:
                print ("Wrong choice")

if __name__ == "__main__":
    main()
