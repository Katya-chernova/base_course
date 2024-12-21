import numpy as np
import matplotlib.pyplot as plt

def polar_sist(r, phi):
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return x, y





phi = np.linspace(0.01, 8 * np.pi, 800) 
r = 8/np.sqrt(phi) 
x, y = polar_sist(r, phi)
plt.plot(x, y, label='Спираль "жезл"')





plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

plt.savefig('fig_43.png')