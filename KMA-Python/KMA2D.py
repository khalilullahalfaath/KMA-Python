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
global n_var, f_treshold_fx, max_num_eva
global pop_size, min_ada_pop_size, max_ada_pop_size
global big_males, big_males_fx
global female, female_fx
global small_males, small_males_fx
global all_hq, all_hq_fx
global mlipir_rate, mut_rate, mut_radius
global one_elit_fx

def kma_2d(best_indiv, opt_val, num_eva, f_opt, f_mean, proc_time, evo_pop_size):
    

