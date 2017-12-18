import sys
sys.path.append('..')
from imports import *

class Route:
    """represents a Route over cities in the Map"""
    
    def __init__(self,nrCities,startCity):
        """initialize with the number of cities and the city the Route starts with"""
        self.distance=0
        self.route=[startCity]
        self.remainingCities={x for x in range(0,nrCities)}
        self.remainingCities.remove(startCity)

    def __repr__(self):
        """defines what is printed by print() function"""
        return str("route:"+str(self.route)+" distance:"+str(self.distance)+" remaining:"+str(self.remainingCities))
    def __str__(self):
        return repr(self)
        
    def getRoute(self):
        """get the route"""
        return self.route

    def getDistance(self):
        """get the distance"""
        return self.distance

    def getRemainingCities(self):
        """get set of cities not yet visited"""
        return self.remainingCities

    def getCurrentCity(self):
        """get the current city on the route"""
        return self.route[-1]

    def selectNextCity(self,myMap,nextCity):
        """select the next city on the route"""
        self.selectNextCityHelper(myMap,nextCity)
        self.remainingCities.remove(nextCity)
        if (len(self.remainingCities)==0): # if all cities visited
            self.selectNextCityHelper(myMap,self.route[0]) # then go back to start city

    def selectNextCityHelper(self,myMap,nextCity):
        """helper function to select the next city on the route"""
        c=self.getCurrentCity()
        self.distance+=myMap.getDistance(c,nextCity)
        self.route.append(nextCity)
            
    def unselectLastCity(self,myMap):
        """unselect the last selected city on the route"""
        if (len(self.remainingCities)==0): # if all cities visited
            self.unselectLastCityHelper(myMap) # then first unselect start city
        last=self.route[-1]
        self.unselectLastCityHelper(myMap)
        self.remainingCities.add(last)

    def unselectLastCityHelper(self,myMap):
        last=self.route.pop()
        c=self.getCurrentCity()
        self.distance-=myMap.getDistance(c,last)

    def unitTest():
        """run unit tests"""
        myMap=Map()
        nrCities=10
        myMap.randomizeMap(nrCities,Position([1,1]))
        route=myMap.initRoute()
        Route.recursiveTest(0,nrCities-1,myMap,route)

    def recursiveTest(dept,maxDepth,myMap,route):
        if dept<maxDepth:
            dist1=route.getDistance()
            c=next(iter(route.getRemainingCities())) # select first element
            print(route)
            route.selectNextCity(myMap,c)
            Route.recursiveTest(dept+1,maxDepth,myMap,route)
            route.unselectLastCity(myMap)
            dist2=route.getDistance()
            assert dist1-dist2<0.000001, "Error in recursive distance test"
            print(route)
        else:
            print(route)
        
def main(argv):
    Route.unitTest()

if __name__ == "__main__":
    main(sys.argv)
