import sys
sys.path.append('..')
from imports import *

if len(sys.argv)<6 or sys.argv[1]=="-h" or sys.argv[1]=="--help":
    print("Runs an algorithm to solve a TSP map and saves the best")
    print("solution and appends score and time to file.")
    print("  usage: "+sys.argv[0]+" <algo-name> <map-file> <solution-file> <score-file> <time-file> [-r <nrRuns>] [-i <nrIteration>] [-r <restartCounter>] [-t startTemperature] [-b]")
    print("         algo-name        'random', 'hillClimber', 'simAnneal', 'greedy', 'breadthFirst' or 'depthFirst'")
    print("         r                number of runs (default 1)")
    print("         i                number of iterations per run, only used for random and hillClimber (default 1000)")
    print("         c                no improvement restart counter, only used for hillClimber (default -1)")
    print("         t                start temperature for simulated annealing (default 0.5)")
    print("         b                branch and bound (default False)")
    print("  example: "+sys.argv[0]+" random myMap.txt solution.txt scores.txt time.txt")
    exit()

algoName=sys.argv[1]
mapFile=sys.argv[2]
solutionFile=sys.argv[3]
scoreFile=sys.argv[4]
timeFile=sys.argv[5]

nrRuns=1
nrIteration=1000
restartCounter=-1
startTemperature=0.5
branchAndBound=False
for i in range(6,len(sys.argv)):
    if sys.argv[i]=="-r":
        i+=1
        nrRuns=int( sys.argv[i])
    if sys.argv[i]=="-i":
        i+=1
        nrIteration=int( sys.argv[i])
    if sys.argv[i]=="-c":
        i+=1
        restartCounter=int( sys.argv[i])
    if sys.argv[i]=="-t":
        i+=1
        startTemperature=float( sys.argv[i])
    if sys.argv[i]=="-b":
        branchAndBound=True

def getAlgorithm(algoName):
    algo=None
    if algoName=="random":
        algo=RandomAlgorithm(nrIteration)
    elif algoName=="hillClimber":
        algo=HillClimberAlgorithm(nrIteration,restartCounter)
    elif algoName=="simAnneal":
        algo=SimulatedAnnealingAlgorithm(nrIteration,restartCounter,startTemperature)
    elif algoName=="greedy":
        algo=GreedyAlgorithm()
    elif algoName=="breadthFirst":
        algo=BreadthFirstAlgorithm()
    elif algoName=="depthFirst":
        algo=DepthFirstAlgorithm(branchAndBound)
    else:
        print("algo-name '"+algoName+"' not valid")
    return algo
    
def runAlgorith():#,mapFile,solutionFile,scoreFile,timeFile,):
    myMap=Map()
    myMap.load(mapFile)
    for i in range(nrRuns):
        print("run ",i+1,"/",nrRuns)
        algo=getAlgorithm(algoName)
        route=algo.run(myMap)
        route.save(solutionFile+"_"+str(i).zfill(5))
        Algorithm.appendList(scoreFile,algo.getScores())
        Algorithm.appendList(timeFile,[algo.getTime()])

runAlgorith()
print("done")

