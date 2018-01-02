
# globals
viz=False    # makes Algorithms vizualize the routes

# system imports
import math
import random
import time
import copy
import os
import glob

# TravelingSalesPerson classes
from TravelingSalesPerson.Position import *
from TravelingSalesPerson.City import *
from TravelingSalesPerson.Route import *
from TravelingSalesPerson.Map import *

# Algorithm classes
from Algorithms.Algorithm import *
from Algorithms.IterativeAlgorithm import * # iterative
from Algorithms.RandomAlgorithm import *
from Algorithms.HillClimberAlgorithm import *
from Algorithms.SimulatedAnnealingAlgorithm import *
from Algorithms.ConstructiveAlgorithm import * # constructive
from Algorithms.GreedyAlgorithm import *
from Algorithms.BreadthFirstAlgorithm import *
from Algorithms.DepthFirstAlgorithm import *

# tools
from Tools.MapGenerator import *
from Tools.RunAlgorithm import *

# visualize
if viz:
    from Visualize.VizTSP import *
