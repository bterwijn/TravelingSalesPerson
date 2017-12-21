import sys
sys.path.append('..')
from imports import *

class DepthFirstAlgorithm(ConstructiveAlgorithm):

    def __init__(self):
        super().__init__()

    def run(self,myMap):
        self.startTimer()
        self.bestScore=float('inf')
        self.bestRoute=None
        route=myMap.initRoute()
        self.recursiveDepthFirst(myMap,route)
        self.stopTimer()
        return self.bestRoute
   
    def recursiveDepthFirst(self,myMap,route):
        distance=route.getDistance()
        if route.isComplete(): # stop condition
            if distance<self.bestScore:
                self.bestScore=distance
                self.bestRoute=copy.deepcopy(route)
                print(distance)
        else:
            if distance<self.bestScore: # branch and bound
                for nextCity in route.getRemainingCities(): # try all options
                    route.selectNextCity(myMap,nextCity)
                    self.recursiveDepthFirst(myMap,route) # recursive call
                    route.unselectLastCity(myMap) # undo selectNextCity
    
    def unitTest(argv):
        myMap=Map()
        myMap.randomizeMap(10,Position([10,10]))
        algo=DepthFirstAlgorithm()
        route=algo.run(myMap)
        #print(algo.getScores())
        print(route)
        print("time:",algo.getTime())
    
if __name__ == "__main__":
    DepthFirstAlgorithm.unitTest(sys.argv)
