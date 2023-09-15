import numpy as np
from utils.trimr import trimr

def mutation():
    global FEMALE
    global NVAR, RB, RA

    global MUTRATE, MUTRADIUS

    newFemale = FEMALE # initialize newFemale
    MaxStep = MUTRADIUS*(RA-RB) # maximum step size

    for ii in range(NVAR):
        if np.random.rand() < MUTRATE:
            newFemale[:,ii] = FEMALE[:,ii] + (2*np.random.rand()-1)*MaxStep[ii]
    newFemale = trimr(newFemale)
    return newFemale