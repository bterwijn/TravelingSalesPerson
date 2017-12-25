from imports import *

# Greedy
for i in [5,7,10,20,50,100]:
    algoName="Greedy"
    mapFile=os.path.join("Maps","map"+str(i)+".txt")
    print("solving '",mapFile,"' using "+algoName)
    solutionFile=os.path.join("Results",algoName+"_map"+str(i)+"_solution.txt")
    scoreFile   =os.path.join("Results",algoName+"_map"+str(i)+"_scores.txt")
    timeFile    =os.path.join("Results",algoName+"_map"+str(i)+"_times.txt")
    runAlgorithm(GreedyAlgorithm(),mapFile,solutionFile,scoreFile,timeFile,1)

# Breadth First
for i in [5,7]:
    algoName="BreadthFirst"
    mapFile=os.path.join("Maps","map"+str(i)+".txt")
    print("solving '",mapFile,"' using "+algoName)
    solutionFile=os.path.join("Results",algoName+"_map"+str(i)+"_solution.txt")
    scoreFile   =os.path.join("Results",algoName+"_map"+str(i)+"_scores.txt")
    timeFile    =os.path.join("Results",algoName+"_map"+str(i)+"_times.txt")
    runAlgorithm(BreadthFirstAlgorithm(),mapFile,solutionFile,scoreFile,timeFile,1)

# Depth First
for i in [5,7,10]:
    algoName="DepthFirst"
    mapFile=os.path.join("Maps","map"+str(i)+".txt")
    print("solving '",mapFile,"' using "+algoName)
    solutionFile=os.path.join("Results",algoName+"_map"+str(i)+"_solution.txt")
    scoreFile   =os.path.join("Results",algoName+"_map"+str(i)+"_scores.txt")
    timeFile    =os.path.join("Results",algoName+"_map"+str(i)+"_times.txt")
    runAlgorithm(DepthFirstAlgorithm(False),mapFile,solutionFile,scoreFile,timeFile,1)

# Depth First
for i in [5,7,10]:
    algoName="DepthFirstBNB"
    mapFile=os.path.join("Maps","map"+str(i)+".txt")
    print("solving '",mapFile,"' using "+algoName)
    solutionFile=os.path.join("Results",algoName+"_map"+str(i)+"_solution.txt")
    scoreFile   =os.path.join("Results",algoName+"_map"+str(i)+"_scores.txt")
    timeFile    =os.path.join("Results",algoName+"_map"+str(i)+"_times.txt")
    runAlgorithm(DepthFirstAlgorithm(True),mapFile,solutionFile,scoreFile,timeFile,1)

# Random
for i in [5,7,10,20]:
    algoName="Random"
    mapFile=os.path.join("Maps","map"+str(i)+".txt")
    print("solving '",mapFile,"' using "+algoName)
    solutionFile=os.path.join("Results",algoName+"_map"+str(i)+"_solution.txt")
    scoreFile   =os.path.join("Results",algoName+"_map"+str(i)+"_scores.txt")
    timeFile    =os.path.join("Results",algoName+"_map"+str(i)+"_times.txt")
    runAlgorithm(RandomAlgorithm(i*1000),mapFile,solutionFile,scoreFile,timeFile,10)

# Hill Climber Restart
for i in [5,7,10,20]:
    algoName="HillClimberRestart"
    mapFile=os.path.join("Maps","map"+str(i)+".txt")
    print("solving '",mapFile,"' using "+algoName)
    solutionFile=os.path.join("Results",algoName+"_map"+str(i)+"_solution.txt")
    scoreFile   =os.path.join("Results",algoName+"_map"+str(i)+"_scores.txt")
    timeFile    =os.path.join("Results",algoName+"_map"+str(i)+"_times.txt")
    runAlgorithm(HillClimberAlgorithm(i*1000,i*10),mapFile,solutionFile,scoreFile,timeFile,10)

# Simulated Annealling
for i in [5,7,10,20]:
    algoName="SimulatedAnnealing"
    mapFile=os.path.join("Maps","map"+str(i)+".txt")
    print("solving '",mapFile,"' using "+algoName)
    solutionFile=os.path.join("Results",algoName+"_map"+str(i)+"_solution.txt")
    scoreFile   =os.path.join("Results",algoName+"_map"+str(i)+"_scores.txt")
    timeFile    =os.path.join("Results",algoName+"_map"+str(i)+"_times.txt")
    runAlgorithm(SimulatedAnnealingAlgorithm(i*1000,-1,True),mapFile,solutionFile,scoreFile,timeFile,10)
