#On Day 70 I want to take a break from Django and learn a little bit about
#the Pygal Module, and in the future use this to  plot a Random Walk
import pygal
import pygal_maps_world
import pyquery
import matplotlib.pyplot as plt
from random import choice

world_chart = pygal.maps.world.World()
#world_chart = pygal.maps.world.SupranationalWorld()
world_chart.add('North america', [('north_america', 1)])
world_chart.add('South america', [('south_america', 1)])
world_chart.add('Europe', [('europe', 1)])
world_chart.add('Africa', [('africa', 1)])
world_chart.add('Asia', [('asia', 1)])
world_chart.add('Oceania', [('oceania', 1)])
world_chart.add('Antartica', [('antartica', 1)])

# ~ world_chart.render()


world_chart.render_in_browser()
