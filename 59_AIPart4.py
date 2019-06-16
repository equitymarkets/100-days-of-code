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

rad = input("Please enter a value for your radius.")
radi = float(rad)
dia = radi * 2

circle_a = (math.pi * math.pow(radi ,2))
circle_c = ((math.pi) * (2 * radi))
vol = ((4/3) * math.pi * math.pow(radi,3))
area = ((4 * math.pi) * math.pow(radi,2))
sumval = 0
print("The area of your 2-dimensional circle is approximately " + str(circle_a) + ".")
print("The circumference of your 2-dimensional circle is approximately " + str(circle_c) + ".")
print("The volume of your sphere is approximately " + str(vol) + ".")
print("The surface area of your sphere is approximately " + str(area) + ".")

print("Living intelligence is defined here as a circle, with lower intelligence life forms represented simply as smaller circles.")
print("Lower intelligence life forms would normally make less decisions, so would not collide with as many decision events.      ");
print("The decision event in this diagram is represented by the +. A collision is more likely given a larger circle, similar to the")
print("probability of a comet colliding with the Moon vs. the Earth vs. Jupiter vs. the Sun.")

#The original program just used ASCII which gets the point across, but let's make a seaborn plot today.

circle_plot = plt.figure("Higher Intelligence Sphere", figsize = (20, 20))
ax = circle_plot.add_subplot(111, projection='3d')
 
# ~ x = 2
# ~ y = 2
# ~ z = 6
# ~ ax.scatter(x,y,z)
# ~ ax.plot3D(x,y,z)

# ~ class Annotation3D(Annotation):
    # ~ '''Annotate the point xyz with text s'''

    # ~ def __init__(self, s, xyz, *args, **kwargs):
        # ~ Annotation.__init__(self,s, xy=(0,0), *args, **kwargs)
        # ~ self._verts3d = xyz        

    # ~ def draw(self, renderer):
        # ~ xs3d, ys3d, zs3d = self._verts3d
        # ~ xs, ys, zs = proj_transform(xs3d, ys3d, zs3d, renderer.M)
        # ~ self.xy=(xs,ys)
        # ~ Annotation.draw(self, renderer)

    
a1 = np.linspace(0,2 * np.pi, 100)
b1 = np.linspace(0, np.pi, 100)
plt.annotate('', xy=(6,.5), xytext = (4,.5))
x1 = dia * np.outer(np.cos(a1), np.sin(b1))
y1 = dia * np.outer(np.sin(a1), np.sin(b1))
z1 = dia * np.outer(np.ones(np.size(a1)), np.cos(b1))
ax.plot_surface(x1,y1,z1, rstride=4, cstride=4, color='palevioletred')
plt.show()

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
