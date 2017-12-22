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
        Algorithm.testAlgorithm(RandomAlgorithm(10000))
    
if __name__ == "__main__":
    RandomAlgorithm.unitTest(sys.argv)
