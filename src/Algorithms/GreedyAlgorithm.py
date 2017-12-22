import sys
sys.path.append('..')
from imports import *

class GreedyAlgorithm(ConstructiveAlgorithm):

    def __init__(self):
        super().__init__()

    def run(self,myMap):
        self.startTimer()
        route=myMap.initRoute()
        while True:
            nextCity=self.getClosestCity(myMap,route)
            if nextCity<0: # if no more next cities stop
                break
            route.selectNextCity(myMap,nextCity) # select closest city
        self.stopTimer()
        return route
   
    def getClosestCity(self,myMap,route):
        minDistance=float("inf")
        minIndex=-1
        c=route.getCurrentCity()
        remainingCities=route.getRemainingCities()
        for i in remainingCities:
             distance=myMap.getDistance(c,i)
             if distance<minDistance:
                 minDistance=distance
                 minIndex=i
        return minIndex
    
    def unitTest(argv):
        Algorithm.testAlgorithm(GreedyAlgorithm())
    
if __name__ == "__main__":
    GreedyAlgorithm.unitTest(sys.argv)
