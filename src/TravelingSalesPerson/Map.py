import sys
sys.path.append('..')
from imports import *

class Map:
    """represents a Map with multiple cities"""
    
    def __init__(self):
        """initialize"""
        self.cities=[]
        self.distanceCache={} # dictonary to remember distances computes between cities

    def __repr__(self):
        """defines what is printed by print() function"""
        return str(self.cities)
    def __str__(self):
        return repr(self)
        
    def randomizeMap(self,nrCities,mapSize):
        """sets the map to nrCities cities each with a random position in a mapSize area"""
        self.cities=[]
        for i in range(nrCities):
            self.cities.append(City("city"+str(i),mapSize.random()))

    def getNrCities(self):
        """get number of cities on the map"""
        return len(self.cities)

    def getCity(self,c):
        """get city with index c"""
        return self.cities[c]

    def getDistance(self,c1,c2):
        """get distance between city with index c1 and c2"""
        if c1>c2:
            temp=c1
            c1=c2
            c2=temp
        distance=0
        if (c1,c2) not in self.distanceCache:
            p1=self.cities[c1].getPosition()
            p2=self.cities[c2].getPosition()
            distance=p1.distance(p2)
            self.distanceCache[(c1,c2)]=distance # cache the computed distance for future invocations
            return distance
        return self.distanceCache[(c1,c2)]

    def initRoute(self):
        return Route(self.getNrCities(),0)
    
    def save(self,filename):
        """save Map to file"""
        with open(filename, "w") as f:
            for i in self.cities:
                f.write("\""+i.getName()+"\"")
                position=i.getPosition()
                for i in position.getCoordinates():
                    f.write(", "+str(i))
                f.write("\n")

    def load(self,filename):
        """load Map from file"""
        self.cities=[]
        with open(filename, "r") as f:
            for line in f:
                splitLine=line.split(",")
                name=splitLine[0].replace('\"','')
                coordinates=[]
                for i in range(1,len(splitLine)):
                    coordinates.append(float(splitLine[i]))
                self.cities.append(City(name,Position(coordinates)))                

    def unitTest():
        m=Map()
        m.randomizeMap(10,Position([10,10]))
        m.save("testMap.txt")
        m.load("testMap.txt")
        m.save("testMap2.txt")
        
def main(argv):
    Map.unitTest()

if __name__ == "__main__":
    main(sys.argv)
