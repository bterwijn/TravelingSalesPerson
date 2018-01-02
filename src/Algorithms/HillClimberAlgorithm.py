import sys
sys.path.append('..')
from imports import *

class HillClimberAlgorithm(IterativeAlgorithm):
    
    def __init__(self,nrIterations,restartCounter):
        super().__init__(nrIterations)
        self.restartCounter=restartCounter
        
    def run(self,myMap):
        self.startTimer()
        self.reset()
        self.iteration=0
        route=myMap.initRoute()
        while self.iteration<self.nrIterations:
            self.hillClimberRun(myMap,route)
        self.stopTimer()
        return self.getBestRoute()

    def acceptNewRoute(self,oldRoute,newRoute):
        return newRoute.getDistance()<oldRoute.getDistance()
    
    def hillClimberRun(self,myMap,route):
        route.randomize(myMap) # restart hill climber with random route
        notImproved=0
        while self.iteration<self.nrIterations:
            self.iteration+=1
            oldRoute=copy.deepcopy(route)  # remember old route before change
            route.randomSwap2Cities(myMap) # do hill climber step (change route)
            if self.acceptNewRoute(oldRoute,route): # check if route is accepted
                notImproved=0
                if viz:
                    vizRouteWait(myMap,route) # vizualize
            else:
                notImproved+=1
                route=oldRoute # revert back to oldRoute when score is not better
            self.updateBestRoute(route)
            if self.restartCounter>0 and notImproved>=self.restartCounter: # restart after not improving for restartCounter steps
                break
    
    def unitTest(argv):
        Algorithm.testAlgorithm(HillClimberAlgorithm(30000,300))
        
if __name__ == "__main__":
    HillClimberAlgorithm.unitTest(sys.argv)
