import unittest
import numpy as np

from initialize_population import KMA2DInitializer


class TestKMA2DInitializer(unittest.TestCase):
    def test_initialization_shape(self):
        PS = 6  # Example population size
        Nvar = 2  # Example number of variables
        Ra = np.array([0.1, 0.2])  # Example lower bounds
        Rb = np.array([0.9, 0.8])  # Example upper bounds

        initializer = KMA2DInitializer(PS, Ra, Rb, Nvar)
        population = initializer.pop_cons_initialization()

        self.assertEqual(population.shape, (PS, Nvar))

    def test_values_within_bounds(self):
        PS = 10  # Example population size
        Nvar = 3  # Example number of variables
        Ra = np.array([0.1, 0.2, 0.3])  # Example lower bounds
        Rb = np.array([0.9, 0.8, 0.7])  # Example upper bounds

        initializer = KMA2DInitializer(PS, Ra, Rb, Nvar)
        population = initializer.pop_cons_initialization()

        for i in range(PS):
            for j in range(Nvar):
                self.assertTrue(Ra[j] <= population[i, j] <= Rb[j])


if __name__ == "__main__":
    unittest.main()
