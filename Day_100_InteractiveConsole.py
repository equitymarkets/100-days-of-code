#Day 100: Days 1-49 of the #100DaysofCode Challenge-console apps and data visualizations in Matplotlib, Numpy, Pandas, and Seaborn. 

import matplotlib.pyplot as plt											
import numpy as np														
import pandas as pd
import seaborn as sns
import math 
import scipy as sp
import cv2 as cv
from pandas import DataFrame
from pylab import *
from random import seed					
from random import randint 
import statistics
import os 

choice = True


def python_intro():                                 #Day 1: Introduction to Python
        first_name = input("Please enter your first name then press enter.")
    
        input("Hello {}, let's learn about Python!".format(first_name) + "\nPlease press enter.")
    
        message = input("Some important details to know about Python include: Data Types, Loops, Lists, Dictionaries, Functions, Objects, Classes, and Inheritance.\nPlease type the name of one detail (e.g. Data Types) to learn more about it.")
    
        data = "Basic data types in Python include integers, floating-point numbers, complex numbers, strings, booleans, and many built-in functions. (Courtesy https://realpython.com)"
        loop = "A loop is a process that runs repeatedly until the fullfillment of a certain condition. (Courtesy https://techtarget.com/definition/loop"
        lists = "In Python, a list refers to an array. A list, or array, is a 'sequence of several variables, grouped together under a single name.' (Courtesy https://cscircles.cemc.uwaterloo.ca/13-lists/)"
        diction = "A dictionary is a collection of elements which is 'unordered, changeable, and indexed.' (Courtesy https://www.w3schools.com/python/python_dictionaries.asp)"
        funct = "A function, also known as a method, is a block of reusable code used as a tool for a specific action. (Courtesy https://www.tutorialspoint.com/python/python_functions.htm)"
        obj = "An object is a 'variable, data structure, function, or a method. (Courtesy https://en.wikipedia.org/wiki/Object_(computer_science)) Just about everything in Python can be considered an object!"
        clas = "Classes simply provide a way to group data and functionality together (Courtesy https://docs.python.org/3/tutorial/classes.html)"
        inherit = "Inheritance, a property of Python, allows the programmer to define classes, then later define more specific sub-classes that 'inherit' all of the parent classes characteristics. (Courtesy http://www.math.uaa.alaska.edu/~afkjm/cs110/handouts/inheritance.pdf)" 
    
        while message != (""):
            if message == ("Data Types"):
                message = input(data + " If you would like to learn about another data type, please type it in.")
            elif message == ("Loops"):
                message = input(loop + " If you would like to learn about another data type, please type it in.")
            elif message == ("Lists"):
                message = input(lists + " If you would like to learn about another data type, please type it in.")
            elif message == ("Dictionaries"):
                message = input(diction + " If you would like to learn about another data type, please type it in.")
            elif message == ("Functions"):
                message = input(funct + " If you would like to learn about another data type, please type it in.")
            elif message == ("Objects"):
                message = input(obj + " If you would like to learn about another data type, please type it in.")
            elif message == ("Classes"):
                message = input(clas + " If you would like to learn about another data type, please type it in.")
            elif message == ("Inheritance"):
                message = input(inherit + " If you would like to learn about another data type, please type it in.")
            else:
                message = input("You have entered an invalid response. Please enter the name of one of the data types to continue.")
    
        input("Thank you.")

			
 
def python_cont():                                  #Day 2: Using Lists
    data = ['high-level','interpreted','1995','Guido van Rossum', 'Google','Youtube']							#some data about Python

    data.append('Spotify')																						#adds item to end of list					

    level = data[0]																								#list of elements defined as variables
    style = data[1]																										
    pyth = data[2]
    founder = data[3]
    website1 = data[-3]
    website2 = data[-2]
    website3 = data[-1]

    input("Python is a " + level + " programming language. It is " + style + 									#concatenates the data into a readable sentence
    ".\nIt first appeared in the year " + pyth + 
    " and was founded by " + founder + ".\nIt is used by many large projects, including " 
    + website1 + ", " + website2 + ", and " 
    + website3 + ".\nPress enter to continue.")																	#waits for user to press enter

    input("\nIn the piece 'The Zen of Python', Tim Peters oulines a general mindset for Python programmers.\n")	#introduces following piece

    import this 																								#Zen of Python

    input()																										#waits for user to press enter

    print("Bye-bye")																							#Bye-bye cmd

    import antigravity																							#website

    input()																										#waits for user to press enter
    


def Fibonacci():                            #Day 3 - Fibonacci in the while loop
    number = input("Please enter a number for which to stop counting Fibonacci numbers. ")	
                                                #enter any number	

    A = 0										#initializes Fib sequence
    B = 1
    C = 1
    D = B + C 

    print(B)									#1
    print(C)									#1
    print(D)									#2

    while D < int(number):						#Fibonacci sequence
        A = B
        B = C
        C = D 
        D = C + B
        print(D)
    
    input()										#waits for enter key

 

def statis():                               #Day 4: Statistics
    from random import seed					#random module
    from random import randint 
    import math
    import statistics 

    input("Press enter to calculate of list of 10 random numbers.")

    ran_set = []

    for i in range(1,11):					#random numbers
        val = randint(1, 1000)
        ran_set.append(val)

    
    print(ran_set)							#set of random numbers

    input("Now, let's see some statistics about this set.")
    
    raw_data = sorted(ran_set)				#sorted set least to greatest

    print(raw_data)

    maximum = max(raw_data)
    minimum = min(raw_data)
    rang = maximum - minimum				#range
    avg = statistics.mean(raw_data)
    med = statistics.median(raw_data)
    vari = statistics.variance(raw_data)
    std = statistics.stdev(raw_data)

    input("This set of random numbers has a range of " + str(rang) + ", a mean of " + str(avg) + ", a median of " + str(med) + 
    ", a variance of " + str(round(vari, 2)) + ", and a standard deviation of " + str(round(std, 2)) + ".")
    


def Hanoi_Towers():                         #Day 5 - Towers of Hanoi Problem - Binary Code and Efficiency
    #
    #Great explanation for this courtesy of Youtube user 3Blue1Brown:
    #[https://www.youtube.com/watch?v=2SUvWfNJSsM]
    #
    #In the Towers of Hanoi problem, the priests in the temple are given 64 golden
    #disks with holes in the middle of them and 3 towers (poles which the golden disks
    #slide onto. They must move all of the disks, in the most efficient way possible, to
    #another tower, but they must not put a larger disk on top of a smaller one. (The disks
    #are distributed, and must always stay, in descending order.) When they finish moving the
    #disks, as the story goes, the end of the world is upon us. When solved, the minimum
    #amount of moves will always be two to the power of the amount of disks, minus one. This
    #means that in binary, the most efficient amount of moves will always be represented 
    #with all ones, and the same amount of ones as disks that we start with. (See below.)
    #Of course, to move one disk we only need one move (1 or 1 in binary), to move two disks we
    #need three moves (3 or 11 in binary), and the numbers increase exponentially after that.
    #
    # 
    #    |Moves|                 |Binary|   |Disks to Move|
    #       1              =         1    <----1 disk
    #       2              =        10    
    #       3              =        11    <----2 disks
    #       4              =       100
    #       5              =       101
    #       6              =       110
    #       7              =       111    <----3 disks
    #       8              =      1000
    #       9              =      1001
    #      10              =      1010
    #      11              =      1011
    #      12              =      1100
    #      13              =      1101
    #      14              =      1110
    #      15              =      1111    <----4 disks
    #                              etc.
    
    loop = 1
    
    while loop == 1:
        disk_number = input("Please enter a number of disks, then press enter. ")
        moves_required = pow(2,(int(disk_number)))-1
        print("Moves required: " + str(moves_required))
        req_in_binary = bin(moves_required)
        print("In base 2: " + str(req_in_binary))
        query = input("Would you like to enter another number? Y/N ")
        if query == 'Y':
            loop = 1
        if query == 'N':
            loop = 0



def Monty_Hall():                           #Day 6: The Monty Hall Problem
    from random import seed												#imports random modules
    from random import randint
    print('\n')															#draws the three doors
    print('Please pick Door 1, 2, or 3 by typing the number below.')
    print('\n')
    print('\n')
    
    print('         ________         ________         ________')
    print('        |        |       |        |       |        |')
    print('        |        |       |        |       |        |')
    print('        |        |       |        |       |        |')
    print('        |   1    |       |   2    |       |    3   |')
    print('        |        |       |        |       |        |')
    print('        |        |       |        |       |        |')
    print('        |________|       |________|       |________|')
    print('\n')

                          
    first_choice = int(input())											#Choose one door: 1, 2, or 3
        
    if (first_choice==1) or (first_choice==2) or (first_choice==3):		#set flag for correct input
        flag=0
        answer = first_choice
    else:																#set flag for user error
         flag=1
    
    while flag==1:														#keeps asking until they get it right
        answer = int(input("You have entered an invalid response. Please enter a 1, 2, or 3. "))
        if (answer == 1) or (answer == 2) or (answer ==3):
            flag=0
        first_choice = answer			
    
    print("\nYou have picked Door number " + str(first_choice) + ".")	#Repeats door number
    
    input()
    
    actual = randint(1,3)												#Door the Porsche will be under
    
    MontyPick = randint(1,3)											#Game show host picks this number
    
    while (MontyPick == actual) or (MontyPick == first_choice):
        MontyPick = randint(1,3)
    
    input("\nYou may or may not have picked the right door. \n\nLet's see what is behind Door Number " + str(MontyPick) + ".")
    
    input("\nBehind Door Number " + str(MontyPick) + ", we have a goat.")
    
    new_answer = int(input("\nIf you would like to stay with the door you picked, type that number again.  If you would like to change doors, type that number. "))
        
    if new_answer == actual:											#Does the answer match the Porsche door?
        print("  ")
        print("Congratulations! You win a new Porsche 911!")
    else:
        print("  ")
        print("You lose!")												#Or do you get a slice of pepperoni pizza?
    
    input()																#User can press enter to exit



def SWOT():                                 #Day 7: Dictionaries and the SWOT Analysis
    print("The SWOT Analysis (acronym for Strengths, Weaknesses, Opportunities, and Threats) is a tool to evaluate what we are good at, bad at, can do well, and can do poorly. A common strategy for using the SWOT analysis is to design strategies to utilize our strengths and opportunities, while turning our weaknesses and threats into strengths and opportunities.")
    print('              __________              __________              __________              __________')
    print('             (          )            (          )            (          )            (          )')
    print('             (          )            (          )            (          )            (          )')
    print('             (    S     )            (    W     )            (     O    )            (     T    )')
    print('             (          )            (          )            (          )            (          )')
    print('             (__________)            (__________)            (__________)            (__________)')
    print('               +++   ^                    |                    +++   ^                     |')
    print('                     |____________________|                          |_____________________|')
    
    strengths = []
    strengths_open = 'O'
    weaknesses = []
    weaknesses_open = 'O'
    opportunities = []
    opportunities_open = 'O'
    threats = []
    threats_open = 'O'
    print(" ")
    print("Please think about some of your strengths. Enter them one by one.")                                  #enter your strengths
    while strengths_open == 'O':
        
        enter = input("Please tell me one your strengths or press 'C' to close the strengths module.")
        if enter == 'C':
            strengths_open = 'C'
        if enter != 'C':
            strengths.append(enter)
          
    while weaknesses_open == 'O':
        
        enter = input("Please tell me one your weaknesses or press 'C' to close the weaknesses module.")        #enter your weaknesses       
        if enter == 'C':
            weaknesses_open = 'C'
        if enter != 'C':
            weaknesses.append(enter)
    
    while opportunities_open == 'O':
        
        enter = input("Please tell me one your opportunities or press 'C' to close the opportunities module.")  #enter your opportunities
        if enter == 'C':
            opportunities_open = 'C'
        if enter != 'C':
            opportunities.append(enter)
    
    while threats_open == 'O':
        
        enter = input("Please tell me one your threats or press 'C' to close the threats module.")              #enter your threats
        if enter == 'C':
            threats_open = 'C'
        if enter != 'C':
            threats.append(enter)
            
    S = len(strengths)
    W = len(weaknesses)
    O = len(opportunities)
    T = len(threats)
    
    print('You have ' + str(S) + ' strengths. Here is the list: ' + ' ,'.join(strengths))                       #takes out quotes 
    print('You have ' + str(W) + ' weaknesses. Here is the list: ' + ' ,'.join(weaknesses))                     #in the string
    print('You have ' + str(O) + ' opportunities. Here is the list: ' + ' ,'.join(opportunities))
    print('You have ' + str(T) + ' threats. Here is the list: ' + ' ,'.join(threats))
          
    input()



def planets():                              #Day 8: Planets of the Solar System
    #Data from: https://theplanets.org/planets/
    
    print("Planets of the Solar System:")   #'key': 'value'
    print("     Mercury     Venus     Earth     Mars     Jupiter     Saturn       Uranus      Neptune")
    planets = {'Mercury': {'diameter': '4,879 km', 'distance from the sun': '57,910,000 km','year': '88 days', 'moons': '0',},
               'Venus': {'diameter': '12,104 km', 'distance from the sun': '108,200,000 km', 'year': '243 days', 'moons': '0',},
               'Earth': {'diameter': '12,756 km', 'distance from the sun': '149,600,000 km', 'year': '365 days', 'moons': '1'},
               'Mars': {'diameter': '6,805 km', 'distance from the sun': '227,940,000 km', 'year': '687 days', 'moons': '2'},
               'Jupiter': {'diameter': '142,984 km', 'distance from the sun': '778,330,000 km', 'year': '4,329 days', 'moons': '67'},
               'Saturn': {'diameter': '120,536 km', 'distance from the sun': '1,424,600,000 km', 'year': '10,731 days', 'moons': '150'},
               'Uranus': {'diameter': '51,118 km', 'distance from the sun': '2,873,550,000 km', 'year': '30,770 days', 'moons': '27'},
               'Neptune': {'diameter': '49,528 km', 'distance from the sun': '4,501,000,000 km', 'year': '60,152 days', 'moons': '14'}}
    
    query = input("\nTell me which planet you are interested in learning about. ")
    
    print(query)                            #name of planet   
    
    print('\n' + query + ' has a diameter of ' + str(planets[query]['diameter']) +
          '.'  + ' It is ' + str(planets[query]['distance from the sun']) + ' from the Sun. ' +
          'A year on ' + query + ' is ' + str(planets[query]['year']) + ' long. ' +
          query + ' has ' + str(planets[query]['moons']) + ' moons.')



def bubble_sort():                          #Day 9: Sorting Algorithms-BubbleSort
    #Ideas from Coding Blocks Youtube Channel Episode 84: Algorithms You Should Know
    #https://www.youtube.com/watch?v=5R80MfMxtx4&list=PLWWyzc5ehM92EyZYAL5e5i2zfVqeXY0DA&index=13&t=0s
    
    #--------------------------------------------------------------------------------------------------------------------+
    #1 Bubble Sort: iterates through list, swapping each if in incorrect order
    #  easiest to implement and understand but very inefficient  
    #  time to code=fast; time to run=slow; memory required=average
    
    from time import sleep  
    
    sample = [9,7,11,5,20,7,14,19,12,10,4,7,19,9,17,20,10,4,6,10]					#this is a set a random numbers between 1-20
    n = len(sample)																	#number of elements in the sample, in this case 20
    
    print(sample)																	#beginning value
    
    def bubble(sample):																#defines bubble() method
        for x in range(n-1,0,-1):													#start with 19, end with 0, increment down by 1
            for i in range(x):														#i counts 
                if sample[i]>sample[i+1]:											#performing iterations
                    tempvalue=sample[i]
                    sample[i] = sample[i+1]
                    sample[i+1] = tempvalue 										#loop restarts until the value is met
                    print(sample)													#prints current list
                    #sleep(1)														#pauses for 1 second
    print(" ")
    print(" ")				
    print("BUBBLE SORT")
    print(" ")
                    
    bubble(sample)
                                                                                    #calls bubble() function
    print(sample)
                                                                                    #prints final sample
    input()
    
    


def merge_sort():                           #Day 10: Merge Sort
    #Ideas from Coding Blocks Youtube Channel Episode 84: Algorithms You Should Know
    #https://www.youtube.com/watch?v=5R80MfMxtx4&list=PLWWyzc5ehM92EyZYAL5e5i2zfVqeXY0DA&index=13&t=0s
    #Thank you also to Interactive Python website:
    #http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
    
    #--------------------------------------------------------------------------------------------------------------------+
    #2 Merge Sort: "Divide and Conquer"-this method splits the list in half, and continues to split each half until
    #  there consists all pairs. At that point, the pairs are resorted back up to form a sorted list. 
    #  very common algorithm  
    #  time to code=slow; time to run=fast; memory required=high
    
    
    from time import sleep
    
    list1 = [16,10,6,17,4,1,1,20,2,18]
    
    print("Your current list is " + str(list1))
    
    def merger(list1):                                              #defines method to perform Merge Sort
        if len(list1)>1:
            
            mid = len(list1)//2                                     #splits n in half to begin algorithm
            sideleft = list1[:mid]                                  #left side
            sideright = list1[mid:]                                 #in an odd sample, the right side will include one more than left
            merger(sideleft)                                        #runs the method on each side
            merger(sideright)
    
            a=0
            b=0
            c=0
            while a < len(sideleft) and b < len(sideright):         #iterating through the sides,
                if sideleft[a] < sideright[b]:                      #breaking them in half each time
                    list1[c]=sideleft[a]
                    a=a+1
                else:
                    list1[c]=sideright[b]
                    b=b+1
                c=c+1
    
            while a < len(sideleft):
                list1[c]=sideleft[a]
                a=a+1
                c=c+1
    
            while b < len(sideright):
                list1[c]=sideright[b]
                b=b+1
                c=c+1
    
    merger(list1)                                                   #calls our method
    print(" ")
    print("MERGE SORT")
    print("Your sorted list is "  + str(list1))                     #prints new list, sorted from least to greatest



def quick_sort():                           #Days 11, 12, and 13: Quick Sort Part 3
    #Some ideas and logic from Brian Faure's youtube video "Quicksort: Background and Python Code" [https://www.youtube.com/watch?v=RFyLsF9y83c]
    #Pivot can be chosen in different ways: first, last, median, random
    
    import random															#imports random module
    from time import sleep													#imports sleep module
                                                                            #random or predefined?
    response = input("Would you like a random sample of numbers, or would you like to use a predifined array?\nPress R for random or P for predefined.")
    
    flag = 0																#correct input = 0
    
    if response == ("R") or response == ('r'):								#R will give us a random list of 8 numbers
        arr = random.sample(range(0,100),8)
    
    elif response == ("P") or response == ('p'):							#P gives us these 8 numbers
        arr = [82, 80, 57, 26, 52, 59, 62, 21]
    
    else:
        flag = 1															#incorrect input = 1
    
    while flag == 1:                                                        #this will loop until we have a correct input
            response = input("You have entered an incorrect character. Please enter R for random or P for predefined.")	
            if response == ("R") or response == ('r'):
                arr = random.sample(range(0,100),8)
                flag = 0
            elif response == ("P") or response == ('p'):
                arr = [82, 80, 57, 26, 52, 59, 62, 21]
                flag = 0
    print(arr)																#the array
    
    def sort(arr):
        length = len(arr)													#length of the list
        index = length - 1													#index of the last number
        if length <= 1: 
            return arr														#this will eventually terminate the program
        left, pivots, right = [],[],[]
        p = arr[index]														#here's our pivot: last number in list
        
        for x in arr:														#for a number in the list...
            if x<p: 
                left.append(x)												#less than pivot, throw it in the left list
            elif x==p:
                pivots.append(x)											#equal to pivot(or a pivot), throw it in the middle
            else:
                right.append(x)												#more than pivot, throw it to the right
            print(" ")
            print(left)														#let's watch it in action...
            print(pivots)													#as the temp arrays change
            print(right)
            print(arr)
            sleep(1)														
        return sort(left) + pivots + sort(right)							#sort() concatenates and returns all three arrays
    outputarr = sort(arr)													#output array is the function return
    print(" ")
    print(outputarr)														#print it for the user
        


def selection_sort():                       #Day 14: Selection Sort
    #Good information for the code logic found at interactivepython.org/lpomz "The Selection Sort"
    #Selection sort simply passes through the list looking for values in order to place aside, putting them in order as it does so.
    #The Selection Sort, as with the Bubble Sort, is light on memory. It is a bit faster to compute(but still considered slow), as it only has to go through less
    #iterations. It is quicker to code than almost any other sorting algorithm. 
    from time import sleep
    import math
    import copy 
    
    numlist = [1,2,75,2,91,3,70,22,38,48]								#previously psuedo-randomly generated numbers
    length = len(numlist)												#length of list
    lengthInd = length - 1
    print(numlist)
    print("  ")  														#some spacing                                                               
    print("  ")                                                                 
     
    for i in range(lengthInd, 0, -1):									#count down from length to 0 by 1
        maxvalue = 0
        maxend = i + 1
        for a in range(1,maxend):
            if numlist[a] > numlist[maxvalue]:
                maxvalue = a
        
        arrtem = numlist[i]
        numlist[i] = numlist[maxvalue]
        numlist[maxvalue] = arrtem
    
    print("  ")
    print("SELECTION SORT")
    print(numlist)



def heap_sort():                            #Days 15 and 16: Heap Sort
    #Heap Sort separates the array elements into nodes, with index 0 (for algorithm purposes, index + 1, or i = 1) representing the top node, or parent. The rest
    #of the nodes are represented as a binomial tree, with the variable i representing the root, or top parent, the expression i//2 representing each parent, the
    #expression 2i representing each left child, and the formula 2i + 1 representing the right child. A good youtube video on this is available in a lecture by
    #Srini Devadas of MIT available here: [https://www.youtube.com/watch?v=B7hVxCmfPtM]
    import math
    from time import sleep 
    input()
    def heapify(data_array, length, i):										#The famous "heapify" method
        
        largest = i															#Largest value should float to top then swap with lowest node, pop, and remove node
        
        left = 2 * i + 1													#left side child													
        
        right = 2 * i + 2													#right side child
        
        if left < length and data_array[i] < data_array[left]:				#|	left and right sides of the equation, accounting for index |#	
            largest = left													#|															   |#
                                                                            #|															   |#
        if right < length and data_array[largest] < data_array[right]:		#|															   |#
            largest = right													#|															   |#
                                                                            #|															   |#
        if largest != i:													#V															   V#
            data_array[i], data_array[largest] = data_array[largest], data_array[i]
            
            heapify(data_array, length, largest)
            
    def heapsort(data_array):												#Here's where we perform sort
        
        length = len(data_array)
        
        for i in range(length, -1, -1):
            heapify(data_array, length, i)
            print(data_array)
            sleep(2)
        for i in range(length-1, 0, -1):
            data_array[i], data_array[0] = data_array[0], data_array[i]
            heapify(data_array, i, 0)
            print(data_array)
            #sleep(2)                                                       #cut off or on at will
    data_array = [4, 89, 1, 34, 88, 12, 34]									#inputs
    
    print("Your original list is: \n\t" +str(data_array))
    
    print("   ")
    print("   ")
    print("   ")
    print("   ")
    heapsort(data_array)													#generates output
    print("Using Heap Sort, your number inputs have been converted to the following: \n\t" +str(data_array))



def binaryhex():                            #Day 17: Standard Numbers to Binary and Hex
    #Finding a base 2 (binary) number manually is simply a matter of repeatedly dividing the number by 2, saving each remainder, and reversing the order. 
    #Similarly, finding a base 16 (hexadecimal) number if found by repeatedly dividing the number by 16, and saving each remainder, making sure to assign values 
    #from 10-15 as 'a' to 'f', and reversing the order. 
    from time import sleep
    import math 
    
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    
    n = input("Please enter a standard integer: ")
    
    n = int(n)																#converts string input to int
    
    b = bin(n)																#standard python base 2 method
    
    h = hex(n)																#standard python base 16 method
    
    print(" ")
    print(b)
    print(" ")
    print(h)
    print(" ")
    
    
    class manual_calc:
        def slowbin(n):														#function to manually calculate Base 2 / Binary Code					
            while n > 0:
                m = n%2
                print(str(n) + "       " + str(m))
                n = n//2
                sleep(1)
    
        def slowhex(n):														#function to manually calculate Base 16 / Hexadecimal 
            while n > 0:
                m = n%16
                if m != 0:
                    if m == 10:
                        m = 'a'
                    if m == 11:
                        m = 'b'
                    if m == 12:
                        m = 'c'
                    if m == 13:
                        m = 'd'
                    if m == 14:
                        m = 'e'
                    if m == 15:
                        m = 'f'
            
                print(str(n) + "        " + str(m).format('>'))
                n = math.floor(n/16)
                sleep(1)
    manual_calc.slowbin(n)													#call slowbin()
    print("   ")
    manual_calc.slowhex(n)													#call slowhex()
    print("   ")
    print(n)



def bin_search():                           #Days 18 and 19: Binary Search
    import statistics
    from time import sleep
    
    arr = []
    
    for var in range(1,11):													#1-10, remember, last element will be one less
        
        arr.append(var)														#add each value to end of list in order
        
    
    print(arr)																#show user the list
    
    pick = input("Please enter a number between 1-100 and let the computer search for it.")
    pick = int(pick)														#pick a number
    
    
    
    
    def binary_search(pick, arr):											#function
        left, right = 0, len(arr)-1											#moves in on it starting at both sides, len(arr)-1 should be last value
        while left <= right:												#while we are iterating through the list...			
            middle = left + (right - left)//2
            middle_value = arr[middle]						
            if middle_value == pick:
                return arr[middle]											#if correct right return to main program the answer
            elif middle_value < pick:
                left = middle + 1											#if pick is on the right move the left over
            else:
                right = middle - 1											#if pick is on the left move the right over
        return -1															#out-of-range
    
    result = binary_search(pick, arr)
    
    input()
    if result >= 0:
        print("The number " + str(result) + " has been found in our list.")	#has been found
    else:																	#has not been found
        print("Your number, " + str(pick) + " has not been found on our list.")	



def closing_time():                         #Day 20: Iterative and Recursive Functions-Function to determine closing time based on average profit / hour of business in a coffee shop
    import math
     
    input()
    def avg_profit_mult(hour):
        total = sum(hour) * .6
        return total
        
    hour = [[6.99, 4.95, 8.55, 3.99, 4.95, 4,99, 7.50, 11.99, 5.50, 4.95, 4.95, 7.50, 6.99, 3.99], [5.99, 4.95, 3.99, 11.55, 7.50, 7.50, 7.50, 5.50, 4.95, 3.99, 3.99],
    [3.99, 4.95, 11.55, 5.50, 4.95, 5.99, 5.99], [4.95, 11.95, 3.99, 3.99], [3.99, 4.95, 4.95], [4.95, 7.50], [3.99]] 
    
    def printprof(hour):													#iterative
        for n in range(1,8):
            prof = round(avg_profit_mult(hour[n]),2)
            if prof <= 10.00:
                return n
                break
    
    close = printprof(hour)													#calls function
    
    for i in range(1,8):													
        if close == i:
            print("OPTIMAL CLOSING TIME:  " + str(i + 4) + " PM " )			#n index + 4 is our optimal closing time
    
    input()
    
    n = len(hour)-1
    
    def profit_recursion(n, hour):												#recursive												
        
        
                                                                    #calls one global variable
        if (sum(hour[n]) * .6) > 10:										#base case
            return n + 1
        else:																#recursive case
            n = n-1
            return profit_recursion(n, hour)
    
    close = profit_recursion(n, hour)											#calls function
    
    for i in range(1,8):
        if close == i:
            print("OPTIMAL CLOSING TIME:  " + str(i + 4) + " PM " )			#n index + 4 is our optimal closing time		
    
    input()																				



def tap_codes():                            #Day 21: Tap Code
    #During the U.S./Vietnam War, US POWs used a system of tap codes to communicate with one another. Important messages between troops in different cells could
    #be communicated quietly using this system. 
    
    
    import winsound																					#imports sound in same folder as application
    from time import sleep																			#sleep timer is used for spacing between taps
    
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                                 _______________________________________________")
    print("                                | TAP   |       |       |       |       |       |")                                                 
    print("                                | CODE  |   1   |   2   |   3   |   4   |   5   |")
    print("                                |       |       |       |       |       |       |")
    print("                                |_______|_______|_______|_______|_______|_______|")
    print("                                |       |       |       |       |       |       |")
    print("                                |   1   |   A   |   B   |  C/K  |   D   |   E   |")
    print("                                |       |       |       |       |       |       |")
    print("                                |_______|_______|_______|_______|_______|_______|")
    print("                                |       |       |       |       |       |       |")
    print("                                |   2   |   F   |   G   |   H   |   I   |   J   |")
    print("                                |       |       |       |       |       |       |")
    print("                                |_______|_______|_______|_______|_______|_______|")
    print("                                |       |       |       |       |       |       |")
    print("                                |   3   |   L   |   M   |   N   |   O   |   P   |")
    print("                                |       |       |       |       |       |       |")
    print("                                |_______|_______|_______|_______|_______|_______|")
    print("                                |       |       |       |       |       |       |")
    print("                                |   4   |   Q   |   R   |   S   |   T   |   U   |")
    print("                                |       |       |       |       |       |       |")
    print("                                |_______|_______|_______|_______|_______|_______|")
    print("                                |       |       |       |       |       |       |")
    print("                                |   5   |   V   |   W   |   X   |   Y   |   Z   |")
    print("                                |       |       |       |       |       |       |")
    print("                                |_______|_______|_______|_______|_______|_______|")
    print("")
    print("")
    print("")
    print("")
    input()																							#press enter
    
    def tapper():																					#pulls tap sound from folder and plays it (.wav)
        winsound.PlaySound("tap", winsound.SND_ASYNC)
    
    def tap_code(array):																			#main function assigns a tap combo to each letter
        for i in array:
            if i == 'A' or i == 'a':
                for i in range(1,2):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,2):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'B' or i == 'b':
                for i in range(1,3):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,2):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'C' or i == 'K' or i == 'c' or i == 'k':
                for i in range(1,4):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,2):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'D' or i == 'd':
                for i in range(1,5):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,2):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'E' or i == 'e':
                for i in range(1,6):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,2):
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'F' or i == 'f':
                for i in range(1,2):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,3):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'G' or i == 'g':
                for i in range(1,3):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,3):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'H' or i == 'h':
                for i in range(1,4):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,3):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'I' or i == 'i':
                for i in range(1,5):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,3):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'J' or i == 'j':
                for i in range(1,6):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,3):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'L' or i == 'l':
                for i in range(1,2):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,4):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'M' or i == 'm':
                for i in range(1,3):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,4):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'N' or i == 'n':
                for i in range(1,4):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,4):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'O' or i == 'o':
                for i in range(1,5):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,4):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'P' or i == 'p':
                for i in range(1,6):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,4):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'Q' or i == 'q':
                for i in range(1,2):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,5):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'R' or i == 'r':
                for i in range(1,3):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,5):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'S' or i == 's':
                for i in range(1,4):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,5):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'T' or i == 't':
                for i in range(1,5):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,5):
                    sleep(.30)
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'U' or i == 'u':
                for i in range(1,6):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,5):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'V' or i == 'v':
                for i in range(1,2):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,6):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'W' or i == 'w':
                for i in range(1,3):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,6):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'X' or i == 'x' or i == '.':
                for i in range(1,4):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,6):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'Y' or i == 'y':
                for i in range(1,5):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,6):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            if i == 'Z' or 'z':
                for i in range(1,6):
                    tapper()
                    sleep(.20)
                sleep(.30)
                for i in range(1,6):
                    
                    tapper()
                    sleep(.20)
                sleep(1)
            
                    
    word = input("Type a message and press enter.")												#asks for user input
    
    
    
    array1 = list(word)
    
    
    length_index = len(array1)-1
    
    
    tap_code(array1)
    
    
    
    input()



def runtime_info():                         #Day 22: Measuring execution time, code complexity, and memory usage for a given script
    import time
    from time import sleep
    import math
    import psutil 
    import os
            
    n = int(input("Enter a number: "))
    forloop_array = []
    listcomp_array = []
    
    
    
    
    begin = time.time()
    for num in range(1,n+1):
        x = num**4
        forloop_array.append(x)
        #sleep(1)
    finish = time.time()
    timed = finish - begin
    print(forloop_array) 
    print("Time to execute: " + str(timed))
    
    
    
    begin = time.time()
    listcomp_array = [num**4 for num in range(1,n+1)]
    finish = time.time()
    timed = finish - begin	
    print(listcomp_array)	
    print("Time to execute: " + str(timed))
    
    mem = os.getpid()
    print(mem)
    print(psutil.cpu_times)
    proc = psutil.Process().memory_full_info()
    print(proc)
    
    
    
    input() 



def tupler():                               #Day 23: Using the Tuple
    #The following illustrates speeds on a highway during a random one-minute sample. First, the samples will be converted to kmph, then the resulting list will
    #be turned into a tuple. Tuples are light on memory, giving them an advantage over lists. However, tuples are immutable, whereas lists are not. The immutable
    #quality can be an advantage or disadvantage, so the use of a tuple must be carefully considered. 
       
    def cmp(x, y):															#deprecated Python 2 standard library method
        return (x > y) - (x < y)
    
    def mph_kmph_converter(speed_mph):										#mph to kmph is * 1.609 , interesting
        speed_kmph = speed_mph * 1.609
        return speed_kmph
        
    
                                                                            #let's calculate kmph
    highway_speeds_mph = [65, 71, 69, 49, 72, 69, 64, 74, 75, 68, 64, 64, 55, 73, 59, 72, 71, 73, 59, 51, 65, 69, 70, 79, 72, 71]
    highway_speeds_kmph = []
    
    for num in highway_speeds_mph:											#for loop calculates each value
        highway_speeds_kmph.append(mph_kmph_converter(num))
        
    mph_tuple = tuple(highway_speeds_mph)									#this makes the lists immutable - tuples!
    kmph_tuple = tuple(highway_speeds_kmph)
    print("  ")																#wrap function in str() for output
    print("When comparing the two tuples, we get " + str(cmp(mph_tuple, kmph_tuple)))
    print("  ")
    print("Miles per hour readings, one minute: " + str(mph_tuple))
    print("  ")
    print("Kilometers per hour readings, one minute: " + str(kmph_tuple))
    
    lengthmph = len(mph_tuple)												#these variables split the both the tuples in half
    lengthkmph = len(kmph_tuple)
    mphhalf = lengthmph//2 
    kmphhalf = lengthkmph//2
    mph_tuple_a = (mph_tuple[:mphhalf])
    mph_tuple_b = (mph_tuple[mphhalf:])
    print(mph_tuple_a)
    print(mph_tuple_b)
    kmph_tuple_a = (kmph_tuple[:kmphhalf])
    kmph_tuple_b = (kmph_tuple[kmphhalf:])
    print(kmph_tuple_a)
    print(kmph_tuple_b)
            


def cornclose():                            #Day 25: Corn prices
    
    x = [0,1,2,3,4,5,6,7,8,9,10,11]											
    y = [3.94,3.50,3.72,3.51,3.56,3.63,3.67,3.75,3.77,3.62,3.57,3.53]
    bins = [3.50,3.55,3.60,3.65,3.70,3.75,3.80,3.85,3.90,3.95]
    
    line = plt.figure("Monthly Closing Price of Corn")
    
    sub1 = plt.subplot(2,2,1)
    plt.plot(x,y,label='Corn',color='firebrick')							
    plt.xlabel("Months")													
    plt.ylabel("Corn Price/Bushel")											
        
    sub2 = plt.subplot(2,2,2)														
    plt.bar(x,y,label='Corn', color='limegreen')							
    plt.xlabel("Months")													
    plt.ylabel("Corn Price/Bushel")	
    
    sub3 = plt.subplot(2,2,3)												
    plt.hist(y,bins,histtype='bar',rwidth=.8,color='darkslateblue')		
    plt.xlabel("Corn Price/Bushel")											
    plt.ylabel("Frequency")	
    
    sub4 = plt.subplot(2,2,4)
    plt.scatter(x,y,color='darkorchid', marker='+')								
    plt.xlabel("Months")													
    plt.ylabel("Corn Price/Bushel")	
    
    plt.subplots_adjust(hspace=.3, wspace=.4)
    plt.suptitle("Monthly Closing Corn Prices")
                                            
    plt.show()
                                                                                                    
                                                                                                    

def bigO():                                 #Day 26: Big O Notation
    x = [0,1,2,3,4,5,6,7,8,9,10,11]
    yexp = []
    yqud = []
    ylin = []
    ylog = []
    ycst = []
    for num in range(0,len(x)):
        num = math.pow(2,num)
        yexp.append(num)
    for num in range(0,len(x)):
        num = num**2
        yqud.append(num)
    for num in range(0,len(x)):
        ylin.append(num)
    for num in range(0,len(x)):
        if num == 0:
            ylog.append(num)
        else:
            num = math.log(x[num],2)
            ylog.append(num)
    for num in range(0,len(x)):
        num = 1
        ycst.append(num)
    
    plt.figure('Big O Notation')
    plt.plot(x,yexp, label='Exponential  O(2^n)', linewidth='3', color='red')
    plt.plot(x,yqud, label='Quadratic  O(n^2)', linewidth='3', color='orange')
    plt.plot(x,ylin, label='Linear  O(n)', linewidth='3', color='blue')
    plt.plot(x,ylog, label="Logarithmic  (log n)", linewidth='3',color='purple')
    plt.plot(x,ycst, label='Constant  O(1)', linewidth='3', color='green')
    plt.xlabel('Elements in Search')
    plt.ylabel('Time')
    plt.title('Time Increase as Sample Size Increases', color='teal')
    plt.legend()
    plt.show() 


    
def supplydemand():                         #Days 27-28: Economics
    Q = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170]
    PS = []
    PD = []
    for num in Q:
        pslist = num
        PS.append(pslist)
    for numb in Q:
        pdlist = max(Q)-numb
        PD.append(pdlist)
            
    
    img =  cv.imread("world_map.jpg")
    img = cv.resize(img, (175,175))

    plt.figure('Supply and Demand',figsize=(10.36,8))
    
    plt.imshow(img)
    plt.title('World Supply and Demand for Our Widget \n2018')
    plt.plot(Q,PS,label='Supply',linewidth='3',color='maroon')
    plt.plot(Q,PD,label='Demand',linewidth='3', color='forestgreen')
    plt.hlines(85, 0, 85, colors='blue', linestyles='--')
    plt.vlines(85, 0, 85, colors='blue', linestyles='--')
    plt.xlabel('Quantity')
    plt.ylabel('Price')
    plt.legend()
    plt.gca().invert_yaxis()
    plt.annotate('equilibrium', xy=(80,80), arrowprops=dict(arrowstyle='->'))
    plt.show()


    
def variousmatplot():                       #Day 29: Operating Systems by Market Share
    mobile = 39.89 + 13.28
    desktop = 35.41 + 7.35 + 3.23 + .84
    market_share=[39.89,35.41,13.28,7.35,3.23,.84]
    OSlabels='Android','Windows','iOS','OSX','Unknown','Linux'              
                                             
    colors=['blue','limegreen','khaki','mediumorchid','bisque','pink']              
    TYPElabels ='Mobile','Desktop'
    market_shareType = [mobile, desktop]
    colorsType = ['lightblue','lightgreen']

    wedgeoutline ={"edgecolor": "black","linewidth": 1,"linestyle": "solid", 
    "antialiased": True}

    plots = arange(0.0,17.0,1)                                              

    plt.figure("OS Use by %, 2019")                                         

    histogram = subplot(2,2,1)                                              
    bins = [10,20,30,40,50]
    plt.hist(market_share,bins,edgecolor='black',
    histtype='bar',rwidth=1,color='limegreen')
    plt.xlabel("Market Share")
    plt.ylabel("Frequency")
    plt.title('Histogram')
    
    pie = subplot(2,2,2)                                                    
    plt.pie(market_share,wedgeprops=wedgeoutline,labels=OSlabels,
    colors=colors,autopct='%1.1f',startangle=135)
    plt.axis('equal')
    plt.title('Market Share by OS and Type')

    subplot(2,2,3)                                                          
    plt.figure("OS Use by %, 2019")
    bins = [10,20,30,40,50]
    plt.hist(market_share,bins,edgecolor='black',histtype='bar',
    rwidth=1,color='limegreen',orientation='horizontal')
    plt.xlabel("Market Share")
    plt.ylabel("Frequency")

    subplot(2,2,4)                                                          
    plt.pie(market_shareType,wedgeprops=wedgeoutline,labels=TYPElabels,
    colors=colorsType,autopct='%1.1f',startangle=135)
    plt.axis('equal')
    plt.tight_layout()
    plt.axis('equal')
    plt.show()



def statisexport():                         #Day 30: Statistics: Pandas Export
                
    input("Press enter to calculate of list of 10 random numbers.")
    
    ran_set = []

    for i in range(1,11):					#random numbers
        val = randint(1, 1000)
        ran_set.append(val)

    
    print(ran_set)							#set of random numbers
    df = DataFrame(ran_set)
    directory = os.path.dirname(os.path.abspath(__file__))
    
    file_path = os.path.join(directory, 'Day_30.csv')   
    df.to_csv(file_path, header=False, index=False)
    
    input("Now, let's see some statistics about this set.")
    
    raw_data = sorted(ran_set)				#sorted set least to greatest
    x = [1,2,3,4,5,6,7,8,9,10]
    print(raw_data)
    
    maximum = max(raw_data)
    minimum = min(raw_data)
    rang = maximum - minimum				#range
    avg = statistics.mean(raw_data)
    med = statistics.median(raw_data)
    vari = statistics.variance(raw_data)
    std = statistics.stdev(raw_data)

    input("This set of random numbers has a range of " + str(rang) + ", a mean of " + str(avg) + ", a median of " + str(med) + 
    ", a variance of " + str(round(vari, 2)) + ", and a standard deviation of " + str(round(std, 2)) + ".")
    plt.figure('Some Random Numbers from 1-1000')
    plt.plot(x, ran_set,label='Numbers from 1-1000',linewidth='4',color='indigo')
    plt.show() 


    
def pandaimport():                          #Day 31: Pokemon: Pandas Import
    input("Welcome. Please press enter.")

    df = pd.read_csv('pokemon_data.csv', index_col=1)

    print(df)

    input()

    print(df.head(10))
    input()

    print(df.tail(10))
    input()
    inpt = input("Now, who would you like to get information for?")
    if inpt == "":
        outpt = ("Thanks for visiting.")
    else:
        outpt = df.loc[inpt]
        query = DataFrame(outpt)
        query.to_csv('Pokemon_Query.csv')   #A little simpler
    print(outpt)


    
def coffeeshop():                           #Days 32-33: The Coffeeshop
    coffee_shop = pd.read_csv('coffeeshop_totalsales.csv')                
    print(coffee_shop)                                                    
    
    plt.figure("Optimal Closing Time")                                    
    plt.plot(coffee_shop.Hour, coffee_shop.Sales, label='Sales/hour', 
    color='green')
    plt.hlines(10/.6, 0, 6, colors='red')                                 
    plt.xlabel("Hour")                                                    
    plt.ylabel("Sales in $")                                              
    plt.legend()                                                          
    plt.show()                                                            


    
def ASEAN():                                #Days 34-35: AEC Cooperation by Imports and Exports
    raw_data = pd.read_csv('ASEAN.csv')

    countries = raw_data.iloc[:, 0]
    imports = raw_data.iloc[:, 1]
    exports = raw_data.iloc[:, 2]


    n = np.arange(len(raw_data))

    plt.figure("Domestic Import/Export ASEAN 2017")
    plt.title("ASEAN Domestic Import/Export 2017")
    import_export = plt.bar(x = n, height = imports, color = 'fuchsia', 
    width = .40)
    export_import = plt.bar(x = n, height = exports, 
    color = 'mediumspringgreen', width = .40, bottom = imports)
    plt.ylabel("Billions of USD")
    plt.xticks(n, countries, rotation = 45)
    plt.legend([import_export, export_import], ('Imports', 'Exports'))
    plt.tight_layout()
    plt.show()



def doppler():                              #Days 36-37: Red Shift/Blue Shift
    print("Light waves tending towards the red end of the visible spectrum ") 
    print("have lower frequency than those near the blue end of the spectrum.") 
    print("This, considering cosmic proportions of scale, results in the fact")
    print("that galaxies moving away from us (most) will appear red to the ")
    print("human eye, whereas galaxies moving towards us (Andomeda for ")
    print("instance) will appear blue. The same effect occurs when measuring")
    print("sound.")
    
    input("Press enter to see why.")

    plt.figure('Doppler Effect')                            
    
    red = np.arange(0, 10, .1)
    blue = np.arange(0, 20, .1)
    ramp = np.sin(red)
    bamp = np.sin(blue)

    red_shift = plt.subplot(2,1,1)                  
    plt.title('Red Shift / Blue Shift')
    plt.ylabel('Amplitude')
    plt.annotate('', xy=(6,.5), xytext = (4,.5), 
    arrowprops=dict(arrowstyle="->")) 
    plt.plot(red, ramp, color='crimson')
    plt.axis('off')
    plt.axhline(y=0, color='black')

    blue_shift = plt.subplot(2,1,2)                 
    plt.xlabel('Wavelength')
    plt.ylabel('Amplitude')
    plt.annotate('', xy=(8,.5), xytext = (12,.5), 
    arrowprops=dict(arrowstyle="->"))
    plt.plot(blue, bamp, color='dodgerblue')
    plt.axis('off')
    plt.axhline(y=0, color='black')
    plt.show()                                      



def appliedfunctions():                     #Days 38, 39, and 40: Pokemon Dataset
    raw_data = pd.read_csv("country_population.csv")

    population1 = raw_data.sort_values('2016')
    sort_one = population1.to_csv('sort1.csv')
    
    population2 = raw_data.sort_values('2016', ascending=False)
    sort_two = population2.to_csv('sort2.csv')
    
    population3 = raw_data.sort_values('2016',na_position='first')
    sort_three = population3.to_csv('sort3.csv')
    
    population4 = raw_data.sort_values(['1960','2016'])
    sort_four = population4.to_csv('sort4.csv')


    
def seaborn():                              #Day 41: Seaborn Intro
    df = pd.read_csv("country_population.csv")
    plt.figure("Country Population")
    plt.subplot(2,2,1)
    sns.set_style('darkgrid')
    one = sns.scatterplot(x='2016',y='1960',data=df, color='mediumvioletred')
    
    
    plt.subplot(2,2,2)
    sns.set_style('whitegrid')
    two = sns.barplot(x='2016',y='1960',data=df, color='darkorchid')
    
    
    plt.subplot(2,2,3)
    sns.set_style('dark')
    three = sns.lineplot(x='2016',y='1960', data=df, color='dodgerblue')
    
    plt.subplot(2,2,4)
    sns.set_style('white')
    four = sns.boxplot(x='2016',y='1960', data=df, color='chartreuse')
    
    plt.show()



def heatmap():                              #Days 42 and 43: Heatmap
    
    ans = sns.load_dataset('anscombe')
    anspiv = ans.pivot('dataset', 'y', 'x')
    plt.figure('Heatmap')
    heat = sns.heatmap(anspiv)
    
    data = ans.pop('dataset')
    
    cluster = sns.clustermap(ans)
    
    plt.show()
    

    
def joint():                                #Day 44: Flights
    example_four = sns.load_dataset('flights')
    sns.set(style='darkgrid')
    im = sns.load_dataset('flights')
    
    sns.jointplot(x = 'year',y = 'passengers', data=im, kind="hex",color="lime")

    plt.show()    
 

    
def boxdist():                              #Day 45: Boxplots
    dot = sns.load_dataset('dots')
    plt.figure('Some Data From Dots.csv')
    plt.subplot(2,2,1)                                              
    sns.boxplot(x=dot['choice'],y=dot['coherence'],color='mediumorchid')

    plt.subplot(2,2,2)                                              
    sns.boxplot(x=dot['align'],y=dot['firing_rate'],color='lightgreen')

    plt.subplot(2,2,3)                                              
    sns.distplot(dot['coherence'],color='deeppink')

    plt.subplot(2,2,4)                                               
    sns.distplot(dot['firing_rate'],color='greenyellow')
    plt.show()   
    


def swarm():                                #Day 46: Swarm Plots
    df_import = pd.read_csv('planets.csv')                                                        
    plt.figure("Planets Spreadsheet")
    sns.swarmplot(x="year",y="distance", data=df_import)
    plt.xticks(rotation=75)
    plt.show()


    
def many():                                 #Day 47: Physical Activity Spreadsheet Analysis
    exercise_data = pd.read_csv("exercise.csv")         #exercise spreadsheet

    #LMPlot
    lmplot = sns.lmplot(x='id',y='pulse',data=exercise_data)
    
    #BarPlot
    plt.figure("Barplot")
    barplot = sns.barplot(x='id',y='pulse',data=exercise_data)
    plt.xticks(size=8)
    
    #KDEPlot
    plt.figure("KDEPlot")
    x = exercise_data.pulse
    KDE = sns.kdeplot(x, shade=True, color='green')
    
    #ScatterPlot
    plt.figure("ScatterPlot")
    scatterplot=sns.scatterplot(x='pulse',y='time',data=exercise_data, 
    color='purple')
    
    #DistPlot
    plt.figure('DistPlot')
    a = exercise_data.pulse
    distplot = sns.distplot(a, color='limegreen')
    
    #LinePlot
    plt.figure('LinePlot')
    lineplot = sns.lineplot(x='pulse',y='id',data=exercise_data, color='red')
    
    #RelPlot
    relplot = sns.relplot(x='pulse',y='id',data=exercise_data)
    
    #CatPlot
    catplot = sns.catplot(x='diet',y='id',hue='pulse',data=exercise_data)
    
    #BoxPlot
    plt.figure('BoxPlot')
    boxplot = sns.boxplot(x='diet',y='pulse',data=exercise_data)
    
    #ViolinPlot
    plt.figure('ViolinPlot')
    violin = sns.violinplot(x='diet',y='pulse',hue='id', inner='quart', 
    data=exercise_data)
    
    #HeatMap
    plt.figure('HeatMap')
    p_e_data = exercise_data.pivot('time','id','pulse')
    exercise_heatmap = sns.heatmap(p_e_data)
    
    #JointPlot
    sns.set(style='white')
    jointplot = sns.jointplot(x='pulse',y='id',data=exercise_data, 
    kind='hex', color='darkblue')
    
    #StripPlot
    plt.figure('StripPlot')
    stripplot = sns.stripplot(x='id',y='pulse',data=exercise_data)
    
    #BoxenPlot
    plt.figure("BoxenPlot")
    boxen = sns.boxenplot(x='id',y='time',data=exercise_data,scale='exponential')
    
    #ResidPlot
    plt.figure("ResidPlot")
    residplot = sns.residplot(x='id',y='pulse',data=exercise_data)
    
    #SwarmPlot
    plt.figure("Swarm Plot")
    swarm = sns.swarmplot(x='pulse',y='time',data=exercise_data)
    
    #PairPlot
    inp = exercise_data
    pairplot = sns.pairplot(inp)
    
    plt.show()

    
        
    choose = input("Would you like to run the program again? Type Y/N.")

    if choose == 'Y':
        choice = True
    else:
        print("Goodbye!")
        quit()


while choice == True:
    day_number = input("Please enter a Day Number to view my work for that day.")

    
    
    
    
    if day_number == '1':
        python_intro()

    if day_number == '2':
            python_cont()
    
    if day_number == '3':
            Fibonacci()
    
    if day_number == '4':
            statis()
    
    if day_number == '5':
            Hanoi_Towers()
    
    if day_number == '6':
            Monty_Hall()
    
    if day_number == '7':
            SWOT()
    
    if day_number == '8':
            planets()
    
    if day_number == '9':
            bubble_sort()
    
    if day_number == '9':
            bubble_sort()
    
    if day_number == '10':
            merge_sort()
    
    if day_number == '11' or day_number == '12' or day_number == '13':
            quick_sort()
    
    if day_number == '14':
            selection_sort()
    
    if day_number == '15' or day_number == '16':
            heap_sort()
    
    if day_number == '17':
            binaryhex()
    
    if day_number == '18' or day_number == '19':
            bin_search()
    
    if day_number == '20':
            closing_time()
    
    if day_number == '21':
            tap_codes()
    
    if day_number == '22':
            runtime_info()
    
    if day_number == '23' or day_number == '24':
            tupler()
    
    if day_number == '25':
            cornclose()
    
    if day_number == '26':
            bigO()
    
    if day_number == '27' or day_number == '28':
            supplydemand()
    
    if day_number == '29':
            variousmatplot()
    
    if day_number == '30':
            statisexport()
    
    if day_number == '31':
            pandaimport()
    
    if day_number == '32' or day_number == '33':
            coffeeshop()
    
    if day_number == '34' or day_number == '35':
            ASEAN()
    
    if day_number == '36' or day_number == '37':
            doppler()
    
    if day_number == '38' or day_number =='39' or day_number =='40':
            appliedfunctions()
    
    if day_number == '41':
            seaborn()
    
    if day_number == '42' or day_number == '43':
            heatmap()
    
    if day_number == '44':
            joint()
    
    if day_number == '45':
            boxdist()
    
    if day_number == '46':
            seaborn()
    
    if day_number == '47' or day_number == '48' or day_number == '49':
            many()
    
    choose = input("Would you like to run the program again? Type Y/N.")

    if choose == 'Y':
        choice = True
    else:
        print("Goodbye!")
        quit()
        
python_intro()

python_cont()

Fibonacci()

statis()

Hanoi_Towers()

Monty_Hall()

SWOT()

planets()

bubble_sort()

merge_sort()

quick_sort()

selection_sort()

heap_sort()

binaryhex()

bin_search()

closing_time()

tap_codes()

runtime_info()

tupler()

cornclose()

bigO()

supplydemand()

variousmatplot()

statisexport()

pandaimport()

coffeeshop()

ASEAN()

doppler()

appliedfunctions()

seaborn()

heatmap()

joint()

boxdist()

swarm()

many()
