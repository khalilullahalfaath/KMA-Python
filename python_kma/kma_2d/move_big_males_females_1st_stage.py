import random
import numpy as np
from utils.trimr import trimr
import evaluation, replacement, crossover, mutation


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
                    VM = VM + np.random.rand() * (HQ[ind,] - tempSM[ss,])
                else:
                    VM = VM - np.random.rand() * (tempSM[ss,] - HQ[ind,])
            folHQ += 1
            if folHQ >= maxFolHQ:
                break
        newBM = tempSM[ss,] + VM  # new big males
        newBM = trimr(newBM)
        tempSM[ss,] = newBM
        tempSMFX[ss] = evaluation(newBM)

    # replace the big males with the best ones
    big_males, big_males_fx = replacement(big_males, big_males_fx, tempSM, tempSMFX)

    winnerBM = big_males[0,]
    winnerFX = big_males_fx[0]

    if winnerFX < female_fx or np.random.rand() < 0.5:  # sexual reproduction
        offsprings = crossover(winnerBM, female)

        fx1 = evaluation(offsprings[0,])
        fx2 = evaluation(offsprings[1,])

        # keep the best position for females
        if fx1 < fx2:
            if fx1 < female_fx:
                female = offsprings[0,]
                female_fx = fx1
        else:
            if fx2 < female_fx:
                female = offsprings[1,]
                female_fx = fx2
    else:  # asexual reproduction
        newFemale = mutation
        fx = evaluation(newFemale)

        # keep the best postion of female
        if fx < female_fx:
            female = newFemale
            female_fx = fx
    return big_males, big_males_fx, female, female_fx
