import sys
sys.path.append('..')
from imports import *

if len(sys.argv)<6 or sys.argv[1]=="-h" or sys.argv[1]=="--help":
    print("Runs an algorithm to solve a TSP map and saves the best")
    print("solution and appends score and time to file.")
    print("  usage: "+sys.argv[0]+" <algo-name> <nrRuns> <map-file> <solution-file> <score-file> <time-file> [<nrIteration> [<restartCounter>]]")
    print("         algo-name        'random', 'hillClimber', 'greedy', 'breadthFirst' or 'depthFirst'")
    print("         nrRuns           number of runs")
    print("         nrIteration      number of iterations per run, only used for random and hillClimber")
    print("         restartCounter   no improvement restart counter, only used for hillClimber")
    print("  example: "+sys.argv[0]+" greedy myMap.txt solution.txt scores.txt time.txt")
    exit()

algoName=sys.argv[1]
nrRuns=int(sys.argv[2])
mapFile=sys.argv[3]
solutionFile=sys.argv[4]
scoreFile=sys.argv[5]
timeFile=sys.argv[6]
nrIteration=1000
if len(sys.argv)>7:
    nrIteration=int(sys.argv[7])
restartCounter=-1
if len(sys.argv)>8:
    restartCounter=int(sys.argv[8])

def getAlgorithm(algoName):
    algo=None
    if algoName=="random":
        algo=RandomAlgorithm(nrIteration)
    elif algoName=="hillClimber":
        algo=HillClimberAlgorithm(nrIteration,restartCounter)
    elif algoName=="greedy":
        algo=GreedyAlgorithm()
    elif algoName=="breadthFirst":
        algo=BreadthFirstAlgorithm()
    elif algoName=="depthFirst":
        algo=DepthFirstAlgorithm()
    else:
        print("algo-name '"+algoName+"' not valid")
    return algo
    
def runAlgorith():#,mapFile,solutionFile,scoreFile,timeFile,):
    myMap=Map()
    myMap.load(mapFile)
    for i in range(nrRuns):
        algo=getAlgorithm(algoName)
        route=algo.run(myMap)
        route.save(solutionFile+"_"+str(i).zfill(5))
        Algorithm.appendList(scoreFile,algo.getScores())
        Algorithm.appendList(timeFile,[algo.getTime()])

runAlgorith()
print("done")
