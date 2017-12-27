import sys
sys.path.append('..')
from imports import *

def loadMatrix(filename):
    mat=[]
    with open(filename, "r") as f:
        for line in f:
            splitline=line.split(" ")
            mat.append([float(i) for i in splitline[0:-1]])
    return mat

def plotMatrix(mat,title="title",xlabel="xlabel",ylabel="ylabel",filename=""):
    for v in mat:
        plt.plot(v)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if filename=="":
        plt.show()
    else:
        fig = plt.gcf()
        fig.savefig(filename)
    plt.clf()
