from initialize_population import pop_cons_initialization
import numpy as np

# Path: KMA-Python\KMA2D.py
PS = 6
RA = 100
RB = -100
NVAR = 2

RA = np.ones((NVAR)) * RA
RB = np.ones((NVAR)) * RB

# print(RA)
# print(RB)

pop = pop_cons_initialization(PS, RA, RB, NVAR)
print(pop)
