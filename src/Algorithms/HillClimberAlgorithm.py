import sys
sys.path.append('..')
from imports import *

class HillClimberAlgorithm(IterativeAlgorithm):
    
    def __init__(self,nrIterations,restartCounter):
        super().__init__(nrIterations)
        self.restartCounter=restartCounter
        self.bestScore=float('inf')
        self.bestRoute=None
        self.iteration=0
        
    def run(self,myMap):
        self.bestScore=float('inf')
        self.bestRoute=None
        self.iteration=0
        route=myMap.initRoute()
        while self.iteration<self.nrIterations:
            self.hillClimberRun(route,myMap)
        return self.bestRoute

    def hillClimberRun(self,route,myMap):
        localBestScore=float('inf')
        localBestRoute=None
        route.randomize(myMap) # restart hill climber with random route
        notImproved=0
        while self.iteration<self.nrIterations:
            self.iteration+=1
            route.randomSwap2Cities(myMap) # do single hill climber step
            dist=route.getDistance()
            self.addScore(dist) # record score
            if dist<self.bestScore: # if better update best
                self.bestScore=dist
                self.bestRoute=copy.deepcopy(route)
                print("bestScore:",self.bestScore)
            if dist<localBestScore: # if better update local best
                localBestScore=dist
                localBestRoute=copy.deepcopy(route)
                print("localBestScore:",localBestScore)
                print("notImproved:",notImproved)
                notImproved=0
            else:
                notImproved+=1
            # restart after not improving for restartCounter steps
            if self.restartCounter>0 and notImproved>=self.restartCounter:
                print("notImproved:",notImproved)
                break
    
    def unitTest(argv):
        myMap=Map()
        myMap.randomizeMap(10,Position([10,10]))
        algo=HillClimberAlgorithm(10000,500)
        route=algo.run(myMap)
        #print(algo.getScores())
        print(route)
    
if __name__ == "__main__":
    HillClimberAlgorithm.unitTest(sys.argv)
