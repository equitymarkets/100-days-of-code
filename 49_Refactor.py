#Day 49: Days 25-47 written in functions and refactored and/or improved in 
#most places

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


def statisexport():                         #Day 30 
				
    input("Press enter to calculate of list of 10 random numbers.")
	
    ran_set = []

    for i in range(1,11):					#random numbers
        val = randint(1, 1000)
        ran_set.append(val)

    
    print(ran_set)							#set of random numbers
    df = DataFrame(ran_set)
    Day_30 = df.to_csv(r'C:\Users\D\python_work\Day_30.csv')
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
    if inpt == "":
        outpt = ("Thanks for visiting.")
    else:
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


def ASEAN():                                #Days 34-35 
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
    #plt.adjust(hspace=.3)
    plt.show()


def doppler():                              #Days 36-37
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


def appliedfunctions():                     #Days 38, 39, and 40
    raw_data = pd.read_csv("country_population.csv")

    population1 = raw_data.sort_values('2016')
    sort_one = population1.to_csv(r'C:\Users\D\python_work\sort1.csv')
    
    population2 = raw_data.sort_values('2016', ascending=False)
    sort_two = population2.to_csv(r'C:\Users\D\python_work\sort2.csv')
    
    population3 = raw_data.sort_values('2016',na_position='first')
    sort_three = population3.to_csv(r'C:\Users\D\python_work\sort3.csv')
    
    population4 = raw_data.sort_values(['1960','2016'])
    sort_four = population4.to_csv(r'C:\Users\D\python_work\sort4.csv')


def seaborn():                              #Day 41
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


def heatmap():                              #Days 42 and 43
    
    ans = sns.load_dataset('anscombe')
    anspiv = ans.pivot('dataset', 'y', 'x')
    heat = sns.heatmap(anspiv)
    
    data = ans.pop('dataset')
    cluster = sns.clustermap(ans)
    plt.show()
    

def joint():                                #Day 44
    example_four = sns.load_dataset('flights')
    sns.set(style='darkgrid')
    im = sns.load_dataset('flights')
    sns.jointplot(x = 'year',y = 'passengers', data=im, kind="hex",color="lime")

    plt.show()    
 
 
def boxdist():                              #Day 45
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
    

def swarm():                                #Day 46
    df_import = pd.read_csv('planets.csv')                                                        
    plt.figure("Planets Spreadsheet")
    sns.swarmplot(x="year",y="distance", data=df_import)
    plt.xticks(rotation=75)
    plt.show()


def many():                                 #Day 47
    exercise_data = pd.read_csv("exercise.csv")         #exercise spreadsheet

    #LMPlot
    lmplot = sns.lmplot(x='id',y='pulse',data=exercise_data)
    
    #BarPlot
    plt.figure("Barplot")
    barplot = sns.barplot(x='id',y='pulse',data=exercise_data)
    plt.xticks(size=8)
    
    #KDEPlot
    plt.figure()
    x = exercise_data.pulse
    KDE = sns.kdeplot(x, shade=True, color='green')
    
    #ScatterPlot
    plt.figure()
    scatterplot=sns.scatterplot(x='pulse',y='time',data=exercise_data, 
    color='purple')
    
    #DistPlot
    plt.figure()
    a = exercise_data.pulse
    distplot = sns.distplot(a, color='limegreen')
    
    #LinePlot
    plt.figure()
    lineplot = sns.lineplot(x='pulse',y='id',data=exercise_data, color='red')
    
    #RelPlot
    relplot = sns.relplot(x='pulse',y='id',data=exercise_data)
    
    #CatPlot
    catplot = sns.catplot(x='diet',y='id',hue='pulse',data=exercise_data)
    
    #BoxPlot
    plt.figure()
    boxplot = sns.boxplot(x='diet',y='pulse',data=exercise_data)
    
    #ViolinPlot
    plt.figure()
    violin = sns.violinplot(x='diet',y='pulse',hue='id', inner='quart', 
    data=exercise_data)
    
    #HeatMap
    plt.figure()
    p_e_data = exercise_data.pivot('time','id','pulse')
    exercise_heatmap = sns.heatmap(p_e_data)
    
    #JointPlot
    sns.set(style='white')
    jointplot = sns.jointplot(x='pulse',y='id',data=exercise_data, 
    kind='hex', color='darkblue')
    
    #StripPlot
    plt.figure()
    stripplot = sns.stripplot(x='id',y='pulse',data=exercise_data)
    
    #BoxenPlot
    plt.figure()
    boxen = sns.boxenplot(x='id',y='time',data=exercise_data,scale='exponential')
    
    #ResidPlot
    plt.figure()
    residplot = sns.residplot(x='id',y='pulse',data=exercise_data)
    
    #SwarmPlot
    plt.figure("Swarm Plot")
    swarm = sns.swarmplot(x='pulse',y='time',data=exercise_data)
    
    #PairPlot
    inp = exercise_data
    pairplot = sns.pairplot(inp)
    
    plt.show()


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
