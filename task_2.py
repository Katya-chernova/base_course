import numpy as np

def mult_func(a):
    b = 1
    for c in a:
        b = b * c

    return b

a = np.array([1,4,6,2,5])
print(mult_func(a))
