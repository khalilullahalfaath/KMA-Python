"""
Created on Wed Apr  1 15:00:00 2020
KMA2D.py
KMA2D is a Python function for solving optimization problems with KMA algorithm.
KMA2D is based on the following paper:
https://www.sciencedirect.com/science/article/pii/S1568494621009637
KMA2D is developed in Python 3.9.12, and tested on Windows 11.
Originally written by Suyanto Suyanto, Alifya Aisyah Ariyanto, Alifya Fatimah Ariyanto in 2021 using matlab.
Then translated to Python by Khalilullah Al Faath in 2023.
"""
import numpy as np

global n_var, f_treshold_fx, max_num_eva
global pop_size, min_ada_pop_size, max_ada_pop_size
global big_males, big_males_fx
global female, female_fx
global small_males, small_males_fx
global all_hq, all_hq_fx
global mlipir_rate, mut_rate, mut_radius
global one_elit_fx


def pop_cons_initialization(PS, Ra, Rb, Nvar):
    # pop_cons_initialization is a function to initialize the population of KMA algorithm.
    # PS is the size of the population.
    # pop_cons_initialization returns the initial population.
    # NL (integer) is the number of locations.

    # f1 and f2 are the vectors of the random numbers contains contants value for initialization.
    F1 = np.array([0.01, 0.01, 0.99, 0.99])
    F2 = np.array([0.01, 0.99, 0.01, 0.99])

    # create the initial population with matrix size PS x NVAR filled with zeros.
    # examples with Ps = 6 and NVAR = 2:
    # [[0, 0],
    #  [0, 0],
    #  [0, 0],
    #  [0, 0],
    #  [0, 0],
    #  [0, 0]]
    # each row is an individual komodo, and each column is a variable or input variable.
    x = np.zeros((PS, Nvar))
    IndX = 0

    # this outer loop iterate from 0 to PS with step 4
    for nn in range(1, PS + 1, 4):
        if PS - nn >= 4:
            NL = 4
        else:
            NL = PS - nn + 1
        
        ss = 0
        while ss < NL:
            Temp = np.zeros(Nvar)
            
            for i in range(Nvar // 2):
                Temp[i] = Rb[i] + (Ra[i] - Rb[i]) * (F1[ss] + (np.random.rand() * 2 - 1) * 0.01)
            
            for i in range(Nvar // 2, Nvar):
                Temp[i] = Rb[i] + (Ra[i] - Rb[i]) * (F2[ss] + (np.random.rand() * 2 - 1) * 0.01)
            
            x[IndX, :] = Temp
            IndX += 1
            ss += 1
    return x 

