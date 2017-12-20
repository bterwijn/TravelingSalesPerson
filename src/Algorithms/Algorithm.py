import sys
sys.path.append('..')
from imports import *

class Algorithm:
    
    def __init__(self):
        self.time=[]

    def run(self,myMap):
        return None
    
    def startTimer(self):
        self.time.append(time.time())
        return len(self.time)-1

    def readTimer(self,timerID):
        return time.time()-self.time[timerID]

    def unitTest(argv):
        algo=Algorithm()
        timerID=algo.startTimer()
        time.sleep(.300)
        print(algo.readTimer(timerID))
    
if __name__ == "__main__":
    Algorithm.unitTest(sys.argv)
