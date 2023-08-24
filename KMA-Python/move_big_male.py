import random
import numpy as np
from utils.trimr import trimr

def move_big_males_female_first_stage(big_males, big_males_fx, female, female_fx, nvar):
    HQ = big_males
    HQFX = big_males_fx

    tempSM = big_males
    tempSMFX = big_males_fx

    for ss in range(tempSM.shape[0]):
        maxFolHQ = random.randint(2)
        VM = np.zeros((nvar))
        RHQ = np.random.permutation(HQ.shape[0])
        folHQ = 0
        for fs in range(RHQ.shape):
            ind = RHQ[fs]
            if ind != ss:
                # semi randomly select sn individual to define an attraction or a distraction
                if HQFX[ind] < tempSMFX[ss] or np.random.rand() < 0.5:
                    VM = VM + np.random.rand() * (HQ[ind, ] - tempSM[ss, ])
                else:
                    VM = VM - np.random.rand() * (tempSM[ss, ] - HQ[ind, ])
            folHQ += 1
            if folHQ >= maxFolHQ:
                break
        newBM = tempSM[ss, ] + VM # new big males
        newBM = trimr(newBM)
        tempSM[ss, ] = newBM
        tempSMFX[ss] = 



