import sys
sys.path.append('..')
from imports import *

from MyTK import *

def minMaxMap(myMap):
    posMin=Position([ float("inf"), float("inf")])
    posMax=Position([-float("inf"),-float("inf")])
    for c in range(myMap.getNrCities()):
        myMap.getCity(c).getPosition().updatePosMin(posMin)
        myMap.getCity(c).getPosition().updatePosMax(posMax)
    return posMin,posMax

def vizMap(myMap):
    posMin,posMax=minMaxMap(myMap)
    w=cv.winfo_width() # window knows its own size
    h=cv.winfo_height()
    border=50 # border in which not to draw
    wm=(w-border*2)/(posMax[0]-posMin[0]) # multipliers to scale coordinate to canvas
    hm=(h-border*2)/(posMax[1]-posMin[1])
    for c in range(myMap.getNrCities()):
        pos=myMap.getCity(c).getPosition()
        x=border+(pos[0]-posMin[0])*wm # convert to canvas coordinates
        y=border+(pos[1]-posMin[1])*hm
        color="white"
        if c==0:
            color="green"
        cv.create_oval(x-10,
                       y-10,
                       x+10,
                       y+10,
                       fill=color)
    
def vizRoute(myMap,route):
    vizMap(myMap)
    r=route.getRoute()
    lastPos=None
    posMin,posMax=minMaxMap(myMap)
    w=cv.winfo_width() # window knows its own size
    h=cv.winfo_height()
    border=50 # border in which not to draw
    wm=(w-border*2)/(posMax[0]-posMin[0]) # multipliers to scale coordinate to canvas
    hm=(h-border*2)/(posMax[1]-posMin[1])
    for i in r:
        pos=myMap.getCity(i).getPosition()
        if lastPos is not None:
            cv.create_line(border+(lastPos[0]-posMin[0])*wm, # convert to canvas coordinates
                           border+(lastPos[1]-posMin[1])*hm,
                           border+(pos[0]-posMin[0])*wm,
                           border+(pos[1]-posMin[1])*hm,
                           fill="blue",arrow=LAST,arrowshape=(12,14,5),width=3,dash=())
        lastPos=pos # remember last position to draw next line
        
if __name__ == "__main__":
    myMap=Map()
    myMap.randomizeMap(20,Position([10,10]))
    algo=GreedyAlgorithm()
    route=algo.run(myMap)
    vizRoute(myMap,route)
    tk.mainloop()
