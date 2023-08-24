import numpy as np

def evaluation(x):
    global function_ID
    dim = len(x)

    match function_ID:
        case 1:
            fx = sum(x ** 2)
        case 2:
            fx = sum(abs(x)) + np.prod(abs(x))
        case 3:
            fx = 0
            for i in range(dim):
                fx += sum(x[:i]) ** 2
        case 4:
            fx = max(abs(x))
        case 5:
            fx = sum(100 * (x[1:] - x[:-1] ** 2) ** 2 + (x[:-1] - 1) ** 2)

    return fx