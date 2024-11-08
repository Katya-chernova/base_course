import numpy as np
import task_1 

g = task_1.gravity_constant
x0 = 0  
y0 = 0  
v0x = 2
v0y = 4


t = np.arange(0,5.01, 0.01)
x = x0 + v0x * t
y = y0 + v0y * t - 0.5 *( g*(t**2))

a = [t, x, y]
b = np.array([t, x, y])

print(b)