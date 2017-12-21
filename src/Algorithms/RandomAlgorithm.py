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
            dist=route.getDistance()
            self.addScore(dist) # record score 
            if dist<bestScore:
                bestScore=dist
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
