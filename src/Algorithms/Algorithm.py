import sys
sys.path.append('..')
from imports import *

class Algorithm:
    
    def __init__(self):
        self.timeStart=0
        self.timeStop=0
        self.scores=[]
        
    def run(self,myMap):
        return None
    
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
