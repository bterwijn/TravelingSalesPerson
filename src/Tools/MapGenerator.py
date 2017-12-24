import sys
sys.path.append('..')
from imports import *

def mapGenerator(filename,nrCities,maxPosition):
        myMap=Map()
        myMap.randomizeMap(nrCities,maxPosition)
        myMap.save(filename)

def mainMapGenerator(argv):
    if len(sys.argv)<4 or sys.argv[1]=="-h" or sys.argv[1]=="--help":
        print("Generates a map with a number of cities and saves it to file.")
        print("The positions of cities have an arbitrary dimension")
        print("A city's first coordinate is randomly choosen between 0 and c1")
        print("        second coordinate is randomly choosen between 0 and c2")
        print("        etc.")
        print("  usage: "+sys.argv[0]+" <filename> <nrCities> <c1> [<c2> [...]")
        print("  example: "+sys.argv[0]+" myMap.txt 20 10.0 10.0")
        exit()
        
    filename=sys.argv[1]
    nrCities=int(sys.argv[2])
    coordinates=[float(i) for i in sys.argv[3:]]
    maxPosition=Position(coordinates)
    mapGenerator(filename,nrCities,maxPosition)
    
if __name__ == "__main__":
    mainMapGenerator(sys.argv)
    print("done")

