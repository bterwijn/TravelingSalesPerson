import sys
sys.path.append('..')
from imports import *

def drawSolutions(maps,algoName):
    for i in maps:
        mapFile=os.path.join("..","maps","map"+str(i).zfill(5)+".txt")
        myMap=Map()
        myMap.load(mapFile)
        print("drawing solutions for '",mapFile,"' using "+algoName)
        solutionFilesWildcards=os.path.join("..","results","map"+str(i).zfill(5)+"_"+algoName+"_solution.txt_*")
        solutionFiles=glob.glob(solutionFilesWildcards)
        for s in solutionFiles:
            print(s)
            route=Route(1,0)
            route.load(s)
            print(route)
            vizRoute(myMap,route)
            tk_update()
            imageFile=s+".png"
            tk_save(imageFile)

drawSolutions([5,7,10,20,50,100],"Greedy")
drawSolutions([5,7],"BreadthFirst")
drawSolutions([5,7,10],"DepthFirst")
drawSolutions([5,7,10],"DepthFirstBNB")
drawSolutions([5,7,10,20],"Random")
drawSolutions([5,7,10,20],"HillClimber")
drawSolutions([5,7,10,20],"HillClimberRestart")
drawSolutions([5,7,10,20],"SimulatedAnnealing")
