import sys
sys.path.append('..')
from imports import *

class IterativeAlgorithm(Algorithm):
    
    def __init__(self,nrIterations):
        super().__init__()
        self.nrIterations=nrIterations
