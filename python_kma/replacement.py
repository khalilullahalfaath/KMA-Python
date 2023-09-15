import numpy as np

def replacement(x, fx, y, fy):
    LX = x.shape[0]
    XY = np.concatenate((x, y), axis=0)
    FXFY = np.concatenate((fx, fy), axis=0)

    # sort the population
    # TODO: check if this is the correct way to sort, otherwise replace axis with 0
    SortedVal=FXFY.sort(axis=1)
    SortedInd=FXFY.argsort(axis=1)
    z = XY[SortedInd, ]
    fz = SortedVal[:LX]

    return z, fz