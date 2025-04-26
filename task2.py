import numpy as np
import matplotlib.pyplot as plt
fix, ax = plt.subplots(subplot_kw={"projection": "3d"})

phi = np.linspace(0, 2*np.pi, 100)
theta = np.linspace(0, np.pi, 100)
R = 5
x = R * np.outer(np.cos(phi), np.sin(theta))
y = R * np.outer (np.sin(phi), np.sin(theta))
z = R * np.outer(np.ones(np.size(phi)), np.cos(theta))

ax.plot_wireframe(x, y, z, rstride=10, cstride=10)

x1 = R * np.cos(phi)
y1 = R * np.sin(phi)
z1 = np.zeros(100) 

def Ox(x1, y1, z1, alpha):
    x2 = x1
    y2 = y1 * np.cos(alpha) - z1 * np.sin(alpha)
    z2 = y1 * np.sin(alpha) + z1 * np.cos(alpha)
    return x2, y2, z2

def Oy(x1, y1, z1, alpha):
    y2 = y1
    x2 = x1 * np.cos(alpha) + z1 * np.sin(alpha)
    z2 = -x1 * np.sin(alpha) + z1 * np.cos(alpha)
    return x2, y2, z2

def Oz(x1, y1, z1, alpha):
    z2 = z1
    x2 = x1 * np.cos(alpha) - y1 * np.sin(alpha)
    y2 = x1 * np.sin(alpha) + y1 * np.cos(alpha)
    return x2, y2, z2

alpha = 80
Ox, Oy, Oz = Ox(x1, y1, z1, alpha)

ax.scatter(Ox, Oy, Oz, color='r') 

plt.savefig("fig_5.png")

