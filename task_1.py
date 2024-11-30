import numpy as np

def average(a):
    b = 0
    for i in range(len(a)):
        b = b + a[i]
    return b/len(a)

a = [1, 2, 3]

print(average(a))

