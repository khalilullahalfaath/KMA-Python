import numpy as np
from utils.trimr import trimr

def crossover(parent1, parent2):
    global Nvar

    # initialize the offsprings
    offsprings = np.zeros((2,Nvar))

    for ii in range(Nvar):
        rval = np.random.rand()
        offsprings[0,ii] = rval * parent1[ii] + (1 - rval) * parent2[ii]
        offsprings[1,ii] = rval * parent2[ii] + (1 - rval) * parent1[ii]
    
    offsprings[0,:] = trimr(offsprings[0,:])
    offsprings[1,:] = trimr(offsprings[1,:])