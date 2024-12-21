import numpy as np
import matplotlib.pyplot as plt

def polar_sist(r, phi):
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return x, y




k = 8
phi = np.linspace(0, 2 * np.pi, 800)
r = np.sin(k * phi)
x, y = polar_sist(r, phi)
plt.plot(x, y, label=f'Роза (k={k})')


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

plt.savefig('fig_44.png')


    