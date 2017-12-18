import sys
sys.path.append('..')
from imports import *

class City:
    """represents a city with name and position"""

    def __init__(self,name,position):
        """initialize with name and position"""
        self.name=name
        self.position=position

    def __repr__(self):
        """defines what is printed by print() function"""
        return str(self.name+" "+str(self.position))
    def __str__(self):
        return repr(self)
        
    def getName(self):
        return self.name

    def getPosition(self):
        return self.position
