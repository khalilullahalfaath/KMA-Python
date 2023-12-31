import numpy as np

def evaluation(x):
    global function_ID
    dim = len(x)

    match function_ID:
        ############# unimodal function ################
        case 1:
            # sphere function
            fx = np.sum(x ** 2)
        case 2:
            # schwefel 2.22 function
            fx = np.sum(np.abs(x)) + np.prod(np.abs(x))
        case 3:
            # schwefel 1.2 function
            fx = 0
            for i in range(dim):
                fx += sum(x[:i])**2
        case 4:
            # schwefel 2.21 function
            fx = np.max(np.abs(x))
        case 5:
            # rosenbrock function
            fx = 0
            for i in range(1,dim-1):
                fx += 100 * (x[i+1]-x[i]**2)**2 + (x[i]-1)**2
        case 6:
            # step function
            fx = np.sum(np.floor((x + 0.5)) ** 2)
        case 7:
            # quartic function
            fx = 0
            for i in range(dim):
                fx += (i + 1) * x[i] ** 4
            fx += np.random.rand()

    ############# multimodal function ################
        case 8:
            # Schwefel function
            fx = sum(-x * np.sin(np.sqrt(abs(x))))
        case 9:
            # Rastrigin function
            fx = sum(x ** 2 - 10 * np.cos(2 * np.pi * x)) + 10*dim
        case 10:
            # Ackley function
            fx = -20 * np.exp(-0.2 * np.sqrt(sum(x ** 2) / dim)) - np.exp(sum(np.cos(2 * np.pi * x)) / dim) + 20 + np.exp(1)
        case 11:
            # Griewank function
            fx = sum(x ** 2) / 4000 - np.prod(np.cos(x / np.sqrt(np.arange(1, dim + 1)))) + 1
        case 12:
            # Penalized function
            a = 10; k = 100; m = 4; dim = len(x)
            yi = 1 + (x[0]+1)/4

            u = sum(np)

            fx = (np.pi/dim) * (10 * ((np.sin(np.pi * (1+(x[0]+1)/4))**2)) + np.sum((np.power((x[:dim-1]+1)*1/4))) )

    return fx