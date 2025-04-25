import numpy as np
import matplotlib.pyplot as plt

fix, ax = plt.subplots (subplot_kw={"projection": "3d"})
t = np.arange(0.01, 4*np.pi, 0.01)
R= 1
x = R* np.cos(t)
y = R * t **0.5
z=R*np.log10(t)
ax.plot(x, y, z, label="Dich")

plt.savefig("fig_1.png")