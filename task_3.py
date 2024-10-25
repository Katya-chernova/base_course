import numpy as np
import task_1 

x0 = 0  
y0 = 0  
v0x = 5 
v0y = 10
t = np.arange(0, 6, 1) 
g = task_1.G  


x = x0 + v0x * t
y = y0 + v0y * t - 0.5 *( g*(t**2))


results  = np.ndarray((t, x, y))

print(results)
