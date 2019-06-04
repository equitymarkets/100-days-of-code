#Day 48: Days 25-48 Refactored Part 1 (will continue tomorrow)
#For Days 25-47, I have coded data visualizations in Matplotlib, Numpy, Pandas,  
#and Seaborn. Today I will clean them up.



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
input()
x = [0,1,2,3,4,5,6,7,8,9,10,11]											
y = [3.94,3.50,3.72,3.51,3.56,3.63,3.67,3.75,3.77,3.62,3.57,3.53]
bins = [3.50,3.55,3.60,3.65,3.70,3.75,3.80,3.85,3.90,3.95]
Q = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170]
mobile = 39.89 + 13.28
desktop = 35.41 + 7.35 + 3.23 + .84
market_share=[39.89,35.41,13.28,7.35,3.23,.84]

def cornclose():                            #Day 25
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
																										
    															
def bigO():                                 #Day 26
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


def supplydemand():                         #Days 27-28
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


def variousmatplot():                       #Day 29
    OSlabels='Android','Windows','iOS','OSX','Unknown','Linux'              
                                             
    colors=['blue','limegreen','khaki','mediumorchid','bisque','pink']              
    TYPElabels ='Mobile','Desktop'
    market_shareType = [mobile, desktop]
    colorsType = ['lightblue','lightgreen']

    wedgeoutline ={"edgecolor": "black","linewidth": 1,"linestyle": "solid", "antialiased": True}

    plots = arange(0.0,17.0,1)                                              

    plt.figure("OS Use by %, 2019")                                         

    histogram = subplot(2,2,1)                                              
    bins = [10,20,30,40,50]
    plt.hist(market_share,bins,edgecolor='black',histtype='bar',rwidth=1,color='limegreen')
    plt.xlabel("Market Share")
    plt.ylabel("Frequency")
    plt.title('Histogram')
    
    pie = subplot(2,2,2)                                                    
    plt.pie(market_share,wedgeprops=wedgeoutline,labels=OSlabels,colors=colors,autopct='%1.1f',startangle=135)
    plt.axis('equal')
    plt.title('Market Share by OS and Type')

    subplot(2,2,3)                                                          
    plt.figure("OS Use by %, 2019")
    bins = [10,20,30,40,50]
    plt.hist(market_share,bins,edgecolor='black',histtype='bar',rwidth=1,color='limegreen',orientation='horizontal')
    plt.xlabel("Market Share")
    plt.ylabel("Frequency")

    subplot(2,2,4)                                                          
    plt.pie(market_shareType,wedgeprops=wedgeoutline,labels=TYPElabels,colors=colorsType,autopct='%1.1f',startangle=135)
    plt.axis('equal')
    plt.tight_layout()
    plt.axis('equal')
    plt.show()


def statisexport():                         #Day 30 *reading index values
				
    input("Press enter to calculate of list of 10 random numbers.")
	
    ran_set = {}
    keys = range(1,11)
    x = []
    for i in keys:					
        x.append(i)
        ran_set[i] = randint(1,1000)
		
    print(ran_set)							
		
    df = DataFrame(ran_set, index=[2])
    Day_30 = df.to_csv(r'C:\Users\D\python_work\Day_30.csv')
    input("Now, let's see some statistics about this set.")
		
    raw_data = sorted(ran_set)				
    print(x)
    print(ran_set)
    print(df)
				
    maximum = max(raw_data)
    minimum = min(raw_data)
    rang = maximum - minimum				
    avg = statistics.mean(raw_data)
    med = statistics.median(raw_data)
    vari = statistics.variance(raw_data)
    std = statistics.stdev(raw_data)
	
    input("This set of random numbers has a range of " + str(rang) + ", a mean of " + str(avg) + ", a median of " + str(med) + 
    ", a variance of " + str(round(vari, 2)) + ", and a standard deviation of " + str(round(std, 2)) + ".") 


def pandaimport():                          #Day 31
    input("Welcome. Please press enter.")

    df = pd.read_csv('pokemon_data.csv', index_col=1)

    print(df)

    input()

    print(df.head(10))
    input()

    print(df.tail(10))
    input()
    inpt = input("Now, who would you like to get information for?")
    outpt = df.loc[inpt]
    query = DataFrame(outpt)
    query.to_csv('Pokemon_Query.csv')
    print(outpt)


def coffeeshop():                           #Days 32-33
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


def ASEAN():                                #Days 34-35 *unicode bytes error
    raw_data = pd.read_csv('ASEAN.csv')

    countries = raw_data.iloc[:, 0]
    imports = raw_data.iloc[:, 1]
    exports = raw_data.iloc[:, 2]


    n = np.arange(len(raw_data))

    plt.figure("Domestic Import/Export ASEAN 2017")
    plt.title("ASEAN Domestic Import/Export 2017")
    import_export = plt.bar(x = n, height = imports, color = 'fuchsia', width = .40)
    export_import = plt.bar(x = n, height = exports, color = 'mediumspringgreen', width = .40, bottom = imports)
    plt.ylabel("Billions of USD")
    plt.xticks(n, countries, rotation = 45)
    plt.legend([import_export, export_import], ('Imports', 'Exports'))
    plt.show()


cornclose()

bigO()

supplydemand()

variousmatplot()

#statisexport()

pandaimport()

coffeeshop()

#ASEAN()



