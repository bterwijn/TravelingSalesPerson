import sys
sys.path.append('..')
from imports import *

class HillClimberAlgorithm(IterativeAlgorithm):
    
    def __init__(self,nrIterations,restartCounter):
        super().__init__(nrIterations)
        self.restartCounter=restartCounter
 
    def run(self,myMap):
        self.startTimer()
        self.bestScore=float('inf')
        self.bestRoute=None
        self.iteration=0
        route=myMap.initRoute()
        while self.iteration<self.nrIterations:
            self.hillClimberRun(myMap,route)
        self.stopTimer()
        return self.bestRoute

    def hillClimberRun(self,myMap,route):
        localBestScore=float('inf')
        localBestRoute=None
        route.randomize(myMap) # restart hill climber with random route
        notImproved=0
        while self.iteration<self.nrIterations:
            self.iteration+=1
            oldRoute=copy.deepcopy(route)  # remember old route before change
            route.randomSwap2Cities(myMap) # do single hill climber step (change route)
            distance=route.getDistance()
            if distance<localBestScore: # if better update local best
                localBestScore=distance
                localBestRoute=copy.deepcopy(route)
                #print("localBestScore:",localBestScore)
                #print("notImproved:",notImproved)
                notImproved=0
                if distance<self.bestScore: # if better update best
                    self.bestScore=distance
                    self.bestRoute=copy.deepcopy(route)
                    print("bestScore:",self.bestScore)
            else:
                notImproved+=1
                route=oldRoute # revert to oldRoute when score is not improved
            self.addScore(localBestScore) # record score
            # restart after not improving for restartCounter steps
            if self.restartCounter>0 and notImproved>=self.restartCounter:
                #print("notImproved:",notImproved)
                break
    
    def unitTest(argv):
        Algorithm.testAlgorithm(HillClimberAlgorithm(30000,300))
        
if __name__ == "__main__":
    HillClimberAlgorithm.unitTest(sys.argv)
