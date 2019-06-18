#Day 61: It is important to demonstrate the different parts of the idea in 
#visual format. Today I want to show the polyhedron inside the circle.
#
#
#
#/|4567891123456789212345678931234567894123456789512345678961234567897123456789812345678991234567890123456789112345678921234567893123456789+
#/|      10        20        30        40        50        60        70        80        90        100       110       120       130 AI.mq4|
#/|                                                                                                                 Copyright 2018, Entropy|
#/|                                                                                                                    https://www.mql5.com|
#/| In many instances, the theoretical application of Artificial Intelligence (AI) is becoming more and more commmonplace. In this program |    
#/| I attempt to represent human or animal intelligence as a sphere, with AI represented as a polyhedron inscribed within the sphere. When |
#/| a decision event strikes the sphere, there is a 100% probability of the human or animal being able to process the event, and therefore |   
#/| make a rational decision based on some desired outcome, whereas there is a distinct probability of the AI being able to process the    |  
#/| event as well, which is the probability of the event striking the polyhedron at a vertex touching what would be the sphere of human or |
#/| animal intelligence. In this way we can visualize AI approaching the level of human or animal intelligence, as the polyhedron becomes  |
#/| more complex (increasing number of vertices due to technological advances, becoming more sphere-like), but never actually reaching it, |     
#/| due to the linear nature of the polyhedron.                                                                                            |
#/|                                                                                                                                        |
#/| Dilemna 1 -  If the vertices are assumed to be singularities, then the decision event would never make contact, and therefore never    |
#/|              be processed by the AI. Of course, this is not the case given the current state of decision-based AI computing.           |
#/|              Conversely, if the vertices are represented as small finite areas, circles for instance, then the vertices would indeed   |
#/|              fill the entire area of the sphere and AI would certainly be able to completely emulate human or animal intelligence in   |
#/|              some amount of time. To counter this paradox, I would consider representing them as small finite circles on the surface   |
#/|              of the sphere with a finite and fixed probability of generating a decision event at any given time.                       |                        
#/+----------------------------------------------------------------------------------------------------------------------------------------+
import math 
from time import sleep
from random import seed					
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.text import Annotation
from itertools import product, combinations

rad = input("Please enter a value for your radius.")
radi = float(rad)
dia = radi * 2

circle_a = (math.pi * math.pow(radi ,2))
circle_c = ((math.pi) * (2 * radi))
vol = ((4/3) * math.pi * math.pow(radi,3))
area = ((4 * math.pi) * math.pow(radi,2))
sumval = 0
print("The area of your circle is approximately " + str(circle_a) + ".")
print("The circumference of your circle is approximately " + str(circle_c) + ".")
print("The volume of your sphere is approximately " + str(vol) + ".")
print("The surface area of your sphere is approximately " + str(area) + ".")

print("Living intelligence is defined here as a circle, with lower intelligence life forms represented simply as smaller circles.")
print("Lower intelligence life forms would normally make less decisions, so would not collide with as many decision events.      ");
print("The decision event in this diagram is represented by the +. A collision is more likely given a larger circle, similar to the")
print("probability of a comet colliding with the Moon vs. the Earth vs. Jupiter vs. the Sun.")

#Cube___________________________________
ax = plt.figure("Higher Intelligence Sphere").gca(projection='3d')
plt.title("Higher Intelligence = Sphere / Artificial Intelligence = Polyhedron")
xs = 10
ys = 10
zs = 10
r = [-5, 5]
for s, e in combinations(np.array(list(product(r,r,r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        ax.plot3D(*zip(s, e), color="purple")

#Sphere__________________________________
    
a1 = np.linspace(0,2 * np.pi, 100)
b1 = np.linspace(0, np.pi, 100)

x1 = dia * np.outer(np.cos(a1), np.sin(b1))
y1 = dia * np.outer(np.sin(a1), np.sin(b1))
z1 = dia * np.outer(np.ones(np.size(a1)), np.cos(b1))
ax.plot_surface(x1,y1,z1, rstride=4, cstride=4, color='#31F8FD40')

#Arrows__________________________________

x = np.zeros(10)
y = np.zeros(10)
z = np.arange(10)
dx = np.zeros(10)
dy = np.arange(10)
dz = np.zeros(10)
#fig = plt.figure()
#ax = fig.gca(projection='3d')
ax.quiver(x, y, y, dx, dx, dz)
ax.set_ylim(0,10)

plt.show()

#_________________________________________



angle = input("Please enter an angle amount.")

angle_measure = ((float(angle) - 2) * 180)
print("The total angle measurement is " + str(angle_measure))

print("Now, lets examine some probabilities.");
sleep(1)


dec_event = int(input("Please define an integer percentage value of the decision event, based on your thoughts."))


for e in range(0,100):
    x = randint(0,100)
    if(x < dec_event):
        print(x)
        print("Strike: Rational decision made!")
        
    else:
        print(str(x) + " - No decision possible.")
        
        
impact_calc = ((float(angle) * .25)/circle_c) * 100
print("\nIn reality, based on your angle input, assuming a .25 unit zone around each angle, a particle travelling towards your circle stands a "+ str(impact_calc) + 
"% chance of facing an intelligent response by AI. ")
