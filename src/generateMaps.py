from imports import *

for i in [5,7,10,20,50,100]:
    mapFile=os.path.join("..","maps","map"+str(i).zfill(5)+".txt")
    print("generating '",mapFile,"'")
    mapGenerator(mapFile,i,Position([10,10]))
