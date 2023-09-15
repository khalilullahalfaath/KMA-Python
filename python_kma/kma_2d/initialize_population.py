"""
pop_cons_initialization is a function to initialize the population of KMA algorithm.
this function takes 4 arguments:
PS (integer) is the size of the population.
Ra (array) is the upper bound of the input variables.
Rb (array) is the lower bound of the input variables.
Nvar (integer) is the number of input variables.
pop_cons_initialization returns the initial population of size PS x NVAR
"""

import numpy as np

class KMA2DInitializer:
    def __init__(self, PS, Ra, Rb, Nvar):
        self.PS = PS
        self.Ra = Ra
        self.Rb = Rb
        self.Nvar = Nvar

    def pop_cons_initialization(self):
        print("Initializing the population...")

        F1 = np.array([0.01, 0.01, 0.99, 0.99])
        F2 = np.array([0.01, 0.99, 0.01, 0.99])

        x = np.zeros((self.PS, self.Nvar))
        IndX = 0

        for nn in range(1, self.PS + 1, 4):
            if self.PS - nn >= 4:
                NL = 4
            else:
                NL = self.PS - nn + 1

            ss = 0
            while ss < NL:
                Temp = np.zeros(self.Nvar)

                for i in range(self.Nvar // 2):
                    Temp[i] = self.Rb[i] + (self.Ra[i] - self.Rb[i]) * (
                        F1[ss] + (np.random.rand() * 2 - 1) * 0.01
                    )

                for i in range(self.Nvar // 2, self.Nvar):
                    Temp[i] = self.Rb[i] + (self.Ra[i] - self.Rb[i]) * (
                        F2[ss] + (np.random.rand() * 2 - 1) * 0.01
                    )

                x[IndX, :] = Temp
                IndX += 1
                ss += 1
        return x
