from imports import *

def generateResults(maps,algo,algoName,nrRuns):
    for i in maps:
        mapFile=os.path.join("..","maps","map"+str(i).zfill(5)+".txt")
        print("solving '",mapFile,"' using "+algoName)
        solutionFile=os.path.join("..","results","map"+str(i).zfill(5)+"_"+algoName+"_solution.txt")
        scoreFile   =os.path.join("..","results","map"+str(i).zfill(5)+"_"+algoName+"_scores.txt")
        timeFile    =os.path.join("..","results","map"+str(i).zfill(5)+"_"+algoName+"_times.txt")
        runAlgorithm(algo,mapFile,solutionFile,scoreFile,timeFile,nrRuns)

generateResults([5,7,10,20,50,100], GreedyAlgorithm(),"Greedy",1)
generateResults([5,7], BreadthFirstAlgorithm(),"BreadthFirst",1)
generateResults([5,7,10],DepthFirstAlgorithm(False),"DepthFirst",1)
generateResults([5,7,10],DepthFirstAlgorithm(True),"DepthFirstBNB",1)
generateResults([5,7,10,20],RandomAlgorithm(20000),"Random",5)
generateResults([5,7,10,20],HillClimberAlgorithm(20000,-1),"HillClimber",5)
generateResults([5,7,10,20],HillClimberAlgorithm(20000,300),"HillClimberRestart",5)
generateResults([5,7,10,20],SimulatedAnnealingAlgorithm(20000,-1,True),"SimulatedAnnealing",5)
