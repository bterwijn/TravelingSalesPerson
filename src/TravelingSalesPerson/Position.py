import sys
sys.path.append('..')
from imports import *

class Position:
    """represents positions in coordinates with arbitrary dimension"""
    
    def __init__(self,coordinates):
        """initialize with list coordinates"""
        self.coordinates=coordinates

    def __repr__(self):
        """defines what is printed by print() function"""
        return str(self.coordinates)
    def __str__(self):
        return repr(self)

    def getCoordinates(self):
        return self.coordinates
    
    def distance(self,p2):
        """compute distance to p2"""
        return math.sqrt(self.squareDistance(p2))
        
    def squareDistance(self,p2):
        """compute square distance to p2 using pythagoras"""
        mySum=0
        for i in range(len(self.coordinates)):
            d=self.coordinates[i]-p2.coordinates[i]
            mySum=d*d
        return mySum

    def random(self):
        """return a new Position with coordinates between 0 and the coordinates of this object"""
        c=[]
        for i in self.coordinates:
            c.append(random.uniform(0,i))
        return Position(c)
        
    def unitTest():
        """run unit tests"""
        print("Position.test() ", end='', flush=True)
        p1=Position([i for i in range(3)])
        assert (p1.distance(p1)==0), "Error, distance to it self should be 0"
        p1=Position([0,0,1])
        p2=Position([0,1,0])
        assert (p1.distance(p1)-math.sqrt(2)<0.00001), "Error, distance incorrect"
        p1=Position([2,0,0])
        assert (p1.distance(p1)-math.sqrt(5)<0.00001), "Error, distance incorrect"
        print("success")

def main(argv):
    Position.unitTest()

if __name__ == "__main__":
    main(sys.argv)
