import numpy as np
import matplotlib.pyplot as plt

def polar_sist(r, phi):
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return x, y


phi = np.linspace(0, 8 * np.pi, 800)  
r = np.exp(phi/8)
x, y = polar_sist(r, phi)
plt.plot(x, y, label='Логарифмическая спираль')




plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

plt.savefig('fig_41.png')