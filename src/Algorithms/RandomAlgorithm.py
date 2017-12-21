import sys
sys.path.append('..')
from imports import *

class RandomAlgorithm(IterativeAlgorithm):
    
    def __init__(self,nrIterations):
        super().__init__(nrIterations)

    def run(self,myMap):
        self.startTimer()
        bestScore=float('inf')
        bestRoute=None
        route=myMap.initRoute()
        for i in range(self.nrIterations):
            route.randomize(myMap)
            distance=route.getDistance()
            self.addScore(distance) # record score 
            if distance<bestScore:
                bestScore=distance
                bestRoute=copy.deepcopy(route)
                print(bestScore)
        self.stopTimer()
        return bestRoute

    def unitTest(argv):
        myMap=Map()
        myMap.randomizeMap(10,Position([10,10]))
        algo=RandomAlgorithm(10000)
        route=algo.run(myMap)
        #print(algo.getScores())
        print(route)
        print("time:",algo.getTime())
    
if __name__ == "__main__":
    RandomAlgorithm.unitTest(sys.argv)
