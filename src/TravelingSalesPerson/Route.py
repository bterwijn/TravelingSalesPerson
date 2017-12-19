import sys
sys.path.append('..')
from imports import *

class Route:
    """represents a Route over cities in the Map"""
    
    def __init__(self,nrCities,startCity):
        """initialize with the number of cities and the city the Route starts with"""
        self.initHelper(nrCities,startCity)

    def initHelper(nrCities,startCity):
        """initialize with the number of cities and the city the Route starts with"""
        self.distance=float(0)
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
            self.unselectLastCityHelper(myMap) # then first unselect end==start city
        last=self.route[-1]
        self.unselectLastCityHelper(myMap)
        self.remainingCities.add(last)

    def unselectLastCityHelper(self,myMap):
        """helper function to unselect the last selected city on the route"""
        last=self.route.pop()
        c=self.getCurrentCity()
        self.distance-=myMap.getDistance(c,last)
        
    def randomize(self,myMap):
        """randomize the route but keep the start and end city fixed"""
        self.initHelper(myMap.getNrCities(),self.route[0])
        while True:
            nextCity=random.sample(self.remainingCities,1)
            self.selectNextCity(myMap,nextCity):
            if len(self.remainingCities)==0:
                break;

    def randomSwapTwoCities(self,myMap):
        """randomly swap two cities in the route but don't swap the start
           city, and don't swap the end city if the route is a loop"""
            end=len(self.route)-1
            if route[0]==route[-1]: # route is a loop
                end-=1 
            if end>2: # if there are a least 2 different cities to swap
                index1=randomint(1,end) # select first city to swap
                while True:
                    index2=randomint(1,end)  # select second city to swap
                    if index2!=index1: # until index2 is different from index1
                        break
                # now swap cities on index1 and index2
                c1=self.removeCityHelper(myMap,index1)
                c2=self.removeCityHelper(myMap,index2)
                self.addCityHelper(myMap,index1,c2)
                self.addCityHelper(myMap,index2,c1)
                
    def removeCityHelper(self,myMap,index):
        """helper to remove city at index and update distance, and return removed city"""
        c=self.route[index]
        cPrev=self.route[index-1]
        distance-=myMap.getDistance(cPrev,c)
        if index<len(self.route)-1: # is not last city in the route
            cNext=self.route[index+1]
            distance-=myMap.getDistance(c,cNext)
        return c
        
    def addCityHelper(self,myMap,index,c):
        """helper to add city c at index and update distance"""
        self.route[index]=c
        cPrev=self.route[index-1]
        distance+=myMap.getDistance(cPrev,c)
        if index<len(self.route)-1: # is not last city in the route
            cNext=self.route[index+1]
            distance+=myMap.getDistance(c,cNext)

    def save(self,filename):
        """save Map to file"""
        with open(filename, "w") as f:
            f.write("route: "+str(self.route)+"\n")
            f.write("distance: "+str(self.distance)+"\n")
            f.write("remainingCities: ")
            if (len(self.remainingCities)==0):
                f.write("{}\n") # otherwise it writes "set()"
            else:
                f.write(str(self.remainingCities)+"\n")

    def load(self,filename):
        """load Map from file"""
        self.distance=0
        self.route=[]
        self.remainingCities=set()
        with open(filename, "r") as f:
            line=f.readline()
            line=line[line.index("[")+1:]
            line=line[:line.index("]")]
            print(line)
            for i in line.split(","):
                if (len(i))>0:
                    self.route.append(int(i))
            self.distance=float(f.readline().split(" ")[1])
            line=f.readline()
            line=line[line.index("{")+1:]
            line=line[:line.index("}")]
            print(line)
            for i in line.split(","):
                if (len(i))>0:
                    self.remainingCities.add(int(i))
                
    def unitTest():
        """run unit tests"""
        myMap=Map()
        nrCities=10
        myMap.randomizeMap(nrCities,Position([1,1]))
        route=myMap.initRoute()
        Route.recursiveDistanceTest(0,nrCities-1,myMap,route)

    def recursiveDistanceTest(depth,maxDepth,myMap,route):
        """test is selecting and unselecting results in the same distance"""
        if depth<maxDepth:
            dist1=route.getDistance()
            c=next(iter(route.getRemainingCities())) # select first element of set
            print(route)
            route.selectNextCity(myMap,c)
            Route.recursiveDistanceTest(depth+1,maxDepth,myMap,route)
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
