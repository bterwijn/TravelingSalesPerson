import sys
sys.path.append('../')
from imports import *

class Route:
    """represents a Route over cities in the Map"""
    
    def __init__(self,myMap,nrCities,startCity):
        """initialize with the number of cities and the city the Route starts with"""
        self.myMap=myMap
        self.distance=0
        self.route=[startCity]
        self.remainingCities={x for x in range(0,nrCities)}
        self.remainingCities.remove(startCity)

    def getRoute(self):
        """get the route"""
        return self.route

    def getRemainingCities(self):
        """get set of cities not yet visited"""
        return self.remainingCities

    def getCurrentCity(self):
        """get the current city on the route"""
        return self.route[-1]

    def selectNextCity(self,nextCity):
        """select the next city on the route"""
        c=self.getCurrentCity()
        self.distance+=self.myMap.getDistance(c,nextCity)
        self.route.append(c)
        self.remainingCities.remove(c)
        
    def unselectLastCity(self):
        """unselect the last selected city on the route"""

        
        last=self.route.pop()
        c=self.getCurrentCity()
        self.distance-=self.myMap.getDistance(c,last)
        self.remainingCities.add(last)

    def unitTest():
        """run unit tests"""
        
def main(argv):
    Route.unitTest()

if __name__ == "__main__":
    main(sys.argv)
