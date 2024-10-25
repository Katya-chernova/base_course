import numpy as np
import task_1 

H = 100  
alpha = np.radians(45)  
beta = np.radians(35)  
g = task_1.G

v = np.sqrt((g*H*np.tan(beta)**2)/(2*np.cos(alpha)**2*(1-np.tan(beta)*np.tan(alpha)**2)))
print(v)








