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

RA = 100
RB = -100

def pop_cons_initialization(PS):
    # pop_cons_initialization is a function to initialize the population of KMA algorithm.
    # PS is the size of the population.
    # pop_cons_initialization returns the initial population.
    # NL (integer) is the number of locations.

    global NVAR
    global RA 
    global RB 

    f1 = np.array([0.01, 0.01, 0.99, 0.09])
    f2 = np.array([0.01, 0.99, 0.01, 0.99])

    x = np.zeros((PS, NVAR))
    IndX = 0

    for nn in range(0, PS + 1, 4):
        if PS - nn >= 4:
            NL = 4
        else:
            NL = PS - nn + 1
        ss = 0
        while ss <= NL:
            temp = np.zeros((NVAR))
            for i in range(1, np.floor(n_var/2)):
                temp[i] = RB + ((RA - RB) * f1[i]) * (f1[ss] + ((np.random.rand()*2)-1) * 0.01)
            for i in range(np.floor(n_var/2), n_var):
                temp[i] = RB + ((RA - RB) * f2[i]) * (f2[ss] + ((np.random.rand()*2)-1) * 0.01)
            x[IndX] = temp
            IndX += 1
            index += 1
    return x 



# def kma_2d(best_indiv, opt_val, num_eva, f_opt, f_mean, proc_time, evo_pop_size):
    

