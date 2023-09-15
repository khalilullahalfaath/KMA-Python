from initialize_population import KMA2DInitializer
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

initializer = KMA2DInitializer(PS, RA, RB, NVAR)
population = initializer.pop_cons_initialization()