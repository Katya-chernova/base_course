import numpy as np

g =  9.8

def energy(a,b,c):
    x1 = (a * (c**2))/2
    x2 = a * g * b

    return x1, x2

tmp = energy(3, 4, 8)

print(tmp[0]+tmp[1])

 
