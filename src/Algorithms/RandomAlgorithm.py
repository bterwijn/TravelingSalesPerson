import sys
sys.path.append('..')
from imports import *

class RandomAlgorithm(IterativeAlgorithm):
    
    def __init__(self,nrIterations):
        super().__init__(nrIterations)

    def run(self,myMap):
        self.startTimer()
        self.reset()
        route=myMap.initRoute()
        for i in range(self.nrIterations):
            route.randomize(myMap)      # randomize route
            self.updateBestRoute(route) # update best score
        self.stopTimer()
        return self.getBestRoute()

    def unitTest(argv):
        Algorithm.testAlgorithm(RandomAlgorithm(10000))
    
if __name__ == "__main__":
    RandomAlgorithm.unitTest(sys.argv)
