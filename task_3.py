import numpy as np
import task_1 

g = task_1.G 
x0 = 0  
y0 = 0  
v0x = 2
v0y = 4


t = np.arange(0,5, 0/001)

for t in range(0, 6, 1): 
    x = x0 + v0x * t
    y = y0 + v0y * t - 0.5 *( g*(t**2))


results  = np.array((t, x, y))

print(results)
