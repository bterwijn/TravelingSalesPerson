import sys
sys.path.append('..')
from imports import *

class IterativeAlgorithm(Algorithm):
    
    def __init__(self,nrIterations):
        super().__init__()
        self.scores=[]
        self.nrIterations=nrIterations

    def addScore(self,score):
        self.scores.append(score)
        
    def getScores(self):
        return self.scores

    def unitTest(argv):
        algo=IterativeAlgorithm(1000,100)
        for i in range(10):
            algo.addScore(i)
        print(algo.getScores())
    
if __name__ == "__main__":
    IterativeAlgorithm.unitTest(sys.argv)
