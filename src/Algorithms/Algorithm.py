import sys
sys.path.append('..')
from imports import *

class Algorithm:
    
    def __init__(self):
        self.timeStart=0
        self.timeStop=0
        self.reset()
        
    def run(self,myMap):
        return None

    def reset(self):
        self.scores=[]
        self.bestScore=float('inf')
        self.bestRoute=None

    def updateBestRoute(self,route):
        self.addScore(route.getDistance())
        if route.getDistance()<self.bestScore:
            self.bestScore=route.getDistance()
            self.bestRoute=copy.deepcopy(route) # deepcopy to avoid later changes
            print("bestScore: ",self.bestScore)
            return True
        return False

    def getBestRoute(self):
        return self.bestRoute
    
    def startTimer(self):
        self.timeStart=time.time()

    def stopTimer(self):
        self.timeStop=time.time()

    def getTime(self):
        return self.timeStop-self.timeStart

    def addScore(self,score):
        self.scores.append(score)
        
    def getScores(self):
        return self.scores

    def appendList(filename,myList):
        with open(filename, "a") as f:
            for i in myList:
                f.write(str(i)+" ")
            f.write("\n")

    def testAlgorithm(algo):
        myMap=Map()
        random.seed(1) # fix random numbers
        myMap.randomizeMap(9,Position([10,10]))
        print(myMap)
        route=algo.run(myMap)
        #print(algo.getScores())
        print(route)
        print("time:",algo.getTime())
        return route

    def unitTest(argv):
        algo=Algorithm()
        algo.startTimer()
        time.sleep(.300)
        algo.stopTimer()
        print(algo.getTime())
        for i in range(10):
            algo.addScore(i)
        print(algo.getScores())
    
if __name__ == "__main__":
    Algorithm.unitTest(sys.argv)
