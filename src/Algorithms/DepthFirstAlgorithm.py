import sys
sys.path.append('..')
from imports import *

class DepthFirstAlgorithm(ConstructiveAlgorithm):

    def __init__(self,branchAndBound):
        super().__init__()
        self.branchAndBound=branchAndBound

    def run(self,myMap):
        self.startTimer()
        self.reset()
        route=myMap.initRoute()
        self.recursiveDepthFirst(myMap,route)
        self.stopTimer()
        return self.getBestRoute()
   
    def recursiveDepthFirst(self,myMap,route):
        if viz:
            vizRouteWait(myMap,route) # vizualize
        distance=route.getDistance()
        if route.isComplete(): # stop condition
            self.updateBestRoute(route)
        else:
            if distance<self.bestScore or not self.branchAndBound: # branch and bound
                for nextCity in route.getRemainingCities(): # try all options
                    route.selectNextCity(myMap,nextCity)
                    self.recursiveDepthFirst(myMap,route) # recursive call
                    route.unselectLastCity(myMap) # undo selectNextCity
    
    def unitTest(argv):
        Algorithm.testAlgorithm(DepthFirstAlgorithm(True))
    
if __name__ == "__main__":
    DepthFirstAlgorithm.unitTest(sys.argv)
