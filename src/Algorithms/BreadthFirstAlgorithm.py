import sys
sys.path.append('..')
from imports import *

class BreadthFirstAlgorithm(ConstructiveAlgorithm):

    def __init__(self):
        super().__init__()

    def run(self,myMap):
        self.startTimer()
        self.reset()
        generation=[myMap.initRoute()] # start with generation of 1 route
        self.breadthFirst(myMap,generation)
        self.stopTimer()
        return self.getBestRoute()
   
    def breadthFirst(self,myMap,generation):
        while len(generation)>0:
            print("generation size:",len(generation))
            newGeneration=[]
            while len(generation)>0: # make new generation
                route=generation.pop() # for each individual in the generation
                for nextCity in route.getRemainingCities(): # create all childeren
                    child=copy.deepcopy(route)           # copy parent
                    child.selectNextCity(myMap,nextCity) # update child
                    if not child.isComplete():
                        newGeneration.append(child)      # add child to new generation
                    else:
                        self.updateBestRoute(child)
            generation=newGeneration # replace current generation
    
    def unitTest(argv):
        Algorithm.testAlgorithm(BreadthFirstAlgorithm())
    
if __name__ == "__main__":
    BreadthFirstAlgorithm.unitTest(sys.argv)
