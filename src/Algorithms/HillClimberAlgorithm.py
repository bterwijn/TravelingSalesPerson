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
            route.randomSwap2Cities(myMap) # do single hill climber step
            distance=route.getDistance()
            self.addScore(distance) # record score
            if distance<self.bestScore: # if better update best
                self.bestScore=distance
                self.bestRoute=copy.deepcopy(route)
                print("bestScore:",self.bestScore)
            if distance<localBestScore: # if better update local best
                localBestScore=distance
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
        algo=HillClimberAlgorithm(30000,300)
        route=algo.run(myMap)
        #print(algo.getScores())
        print(route)
        print("time:",algo.getTime())
        
if __name__ == "__main__":
    HillClimberAlgorithm.unitTest(sys.argv)
