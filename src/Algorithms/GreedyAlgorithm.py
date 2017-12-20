import sys
sys.path.append('../')
from imports import *

class GreedyAlgorithm:
    
    def getClosestCity(self,c,remainingCities):
        minDistance=float("inf")
        minIndex=-1
        # for i in remainingCities:
        #     distance=self.getDistance(c,i)
        #     if distance<minDistance:
        #         minDistance=distance
        #         minIndex=i
        # return minIndex
