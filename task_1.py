import numpy as np

def average(a):
    c = np.sum(np.array(a)) / len(np.array(a))
    return c

a = [1, 2, 4]



b = np.array(a)
print(average(a))

