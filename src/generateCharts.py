import sys
sys.path.append('..')
from imports import *

scoreFilesWildcards=os.path.join("..","results","*scores*.txt")
scoreFiles=glob.glob(scoreFilesWildcards)
for i in scoreFiles:
    out=os.path.splitext(i)[0]+'.pdf'
    print(i," -> ",out)
    plotMatrix(loadMatrix(i),i,"state","score",filename=out)
