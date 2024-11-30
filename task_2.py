import numpy as np
import task_1 

H = 100  
a = np.radians(45)  
b = np.radians(35)  
g = task_1.gravity_constant

v = np.sqrt((g*H*np.tan(b)**2)/(2*np.cos(a)**2*(1-np.tan(b)*np.tan(a))))
print(v)


from task_1 import Planck_constant as h
from task_1 import Euler_number as e
from task_1 import Boltzmann_constant as k

T=200
ε = 300

N = (2/np.sqrt(np.pi))*(h/(k*T)**(3/2))*(e**(-ε/(k*T)) * (ε**(T/2)))
print(N)




