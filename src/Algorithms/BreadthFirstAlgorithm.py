import sys
sys.path.append('..')
from imports import *

class BreadthFirstAlgorithm(ConstructiveAlgorithm):

    def __init__(self):
        super().__init__()

    def run(self,myMap):
        self.startTimer()
        self.bestScore=float('inf')
        self.bestRoute=None
        generation=[myMap.initRoute()] # start with generation of 1 route
        self.breadthFirst(myMap,generation)
        self.stopTimer()
        return self.bestRoute
   
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
                        distance=child.getDistance()
                        self.addScore(distance)
                        if distance<self.bestScore:
                            self.bestScore=distance
                            self.bestRoute=child
            generation=newGeneration # replace current generation
    
    def unitTest(argv):
        myMap=Map()
        myMap.randomizeMap(9,Position([10,10]))
        algo=BreadthFirstAlgorithm()
        route=algo.run(myMap)
        #print(algo.getScores())
        print(route)
        print("time:",algo.getTime())
    
if __name__ == "__main__":
    BreadthFirstAlgorithm.unitTest(sys.argv)
