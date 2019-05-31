#Day 39: Continuing with the project to import, process, and export data
#World Population from www.kaggle.com

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

from pandas import DataFrame
import os
x = os.getcwd()
y = os.listdir()


print(x)
print(y)
input()

raw_data = pd.read_csv("country_population.csv")
# ~ listdata = raw_data.to_dict('series')
# ~ print(listdata)

# ~ with open("country_population.csv", "r") as data:
    # ~ reader = csv.reader(data)
    # ~ raw_data = list(reader)
# ~ print(raw_data)
    
populations = raw_data.iloc[:, 14]

# ~ world = int(populations.to_dict('list'))

print(world)
input()

stats = populations.describe()

print(stats)







sample = populations

n = len(sample)                                                                 #number of elements in the sample, in this case 20
input(n)
print(sample)                                                                   #beginning value

def bubble(sample):                                                             #defines bubble() method
    for x in range(n-1,0,-1):                                                   #start with 19, end with 0, increment down by 1
        for i in range(x):                                                      #i counts 
            if sample[i]>sample[i+1]:                                           #performing iterations
                tempvalue=sample[i]
                sample[i] = sample[i+1]
                sample[i+1] = tempvalue                                         #loop restarts until the value is met
print(" ")
print(" ")              
print("BUBBLE SORT")
print(" ")
                
bubble(sample)
                                                                                #calls bubble() function
print(sample)
                                                                                #prints final sample
input()

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
#sample = [9,7,11,5,20,7,14,19,12,10,4,7,19,9,17,20,10,4,6,10]
    


n = len(sample)                                                                 #number of elements in the sample, in this case 20

print(sample)                                                                   #beginning value

def bubble(sample):                                                             #defines bubble() method
    for x in range(n-1,0,-1):                                                   #start with 19, end with 0, increment down by 1
        for i in range(x):                                                      #i counts 
            if sample[i]>sample[i+1]:                                           #performing iterations
                tempvalue=sample[i]                                             
                sample[i] = sample[i+1]
                sample[i+1] = tempvalue                                         #loop restarts until the value is met 
                
    
print(" ")
print(" ")              
print("BUBBLE SORT")
print(" ")              
bubble(sample)                                                                  #calls bubble() function
print(sample)	 
    
#bubble_sort()
		
def merge_sort():
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
	
	#list1 = [16,10,6,17,4,1,1,20,2,18]
	list1 = populations
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
    
    
#merge_sort()

def quick_sort():
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
			response = input("You have entered an incorrect number. Please enter R for random or P for predefined.")	
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
		
def selection_sort():                                                                                                                                                                               
    
	#Good information for the code logic found at interactivepython.org/lpomz "The Selection Sort"
	#Selection sort simply passes through the list looking for values in order to place aside, putting them in order as it does so.
	#The Selection Sort, as with the Bubble Sort, is light on memory. It is a bit faster to compute(but still considered slow), as it only has to go through less
	#iterations. It is quicker to code than almost any other sorting algorithm. 
	from time import sleep
	import math
	import copy 
	numlist = populations
	#numlist = [1,2,75,2,91,3,70,22,38,48]								#previously psuedo-randomly generated numbers
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
#selection_sort()

  
def heap_sort():
	#Heap Sort separates the array elements into nodes, with index 0 (for algorithm purposes, index + 1, or i = 1) representing the top node, or parent. The rest
	#of the nodes are represented as a binomial tree, with the variable i representing the root, or top parent, the expression i//2 representing each parent, the
	#expression 2i representing each left child, and the formula 2i + 1 representing the right child. A good youtube video on this is available in a lecture by
	#Srini Devadas of MIT available here: [https://www.youtube.com/watch?v=B7hVxCmfPtM]
	import math
	from time import sleep 
	#input()
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
			sleep(2)
	#data_array = [4, 89, 1, 34, 88, 12, 34]									#inputs
	data_array = populations
	print("Your original list is: \n\t" +str(data_array))
	
	print("   ")
	print("   ")
	print("   ")
	print("   ")
	heapsort(data_array)													#generates output
	print("Using Heap Sort, your number inputs have been converted to the following: \n\t" +str(data_array))







#heap_sort()