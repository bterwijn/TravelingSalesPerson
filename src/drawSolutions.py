from imports import *
from Visualize.VizTSP import *

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

drawSolutions([5,7,10,20,50,100], "Greedy")
# generateResults([5,7], BreadthFirstAlgorithm(),"BreadthFirst",1)
# generateResults([5,7,10],DepthFirstAlgorithm(False),"DepthFirst",1)
# generateResults([5,7,10],DepthFirstAlgorithm(True),"DepthFirstBNB",1)
# generateResults([5,7,10,20],RandomAlgorithm(20000),"Random",5)
# generateResults([5,7,10,20],HillClimberAlgorithm(20000,-1),"HillClimber",5)
# generateResults([5,7,10,20],HillClimberAlgorithm(20000,300),"HillClimberRestart",5)
# generateResults([5,7,10,20],SimulatedAnnealingAlgorithm(20000,-1,True),"SimulatedAnnealing",5)
