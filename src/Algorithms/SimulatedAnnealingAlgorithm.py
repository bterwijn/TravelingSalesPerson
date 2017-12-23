import sys
sys.path.append('..')
from imports import *

class SimulatedAnnealingAlgorithm(HillClimberAlgorithm):
    
    def __init__(self,nrIterations,restartCounter,startTemperature):
        super().__init__(nrIterations,restartCounter)
        self.startTemperature=startTemperature

    def acceptNewRoute(self,oldRoute,newRoute):
        improvement=oldRoute.getDistance()-newRoute.getDistance()
        if improvement>0:
            return True # accept new route
        else:
            T=self.startTemperature*(self.nrIterations+1-self.iteration)/self.nrIterations # linear cooling schema
            if random.random()<math.exp(improvement/T):
                return True # accept new route
        return False # don't accept new route
    
    def unitTest(argv):
        Algorithm.testAlgorithm(SimulatedAnnealingAlgorithm(30000,300))
        
if __name__ == "__main__":
    SimulatedAnnealingAlgorithm.unitTest(sys.argv)
