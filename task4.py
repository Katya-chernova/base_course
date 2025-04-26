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

a = 40
A = 250
H = 50 

x1 = R * np.cos(A) * np.cos(a)
y1 = R * np.cos(A) * np.sin(a)
z1 = R * np.sin(A)

def Ox(x1, y1, z1, a):
    a_rad = np.radians(a)
    x2 = x1
    y2 = y1 * np.cos(a) - z1 * np.sin(a)
    z2 = y1 * np.sin(a) + z1 * np.cos(a)
    return x2, y2, z2

def Oy(x1, y1, z1, A):
    b_rad = np.radians(A)
    y2 = y1
    x2 = x1 * np.cos(A) + z1 * np.sin(A)
    z2 = -x1 * np.sin(A) + z1 * np.cos(A)
    return x2, y2, z2

def Oz(x1, y1, z1, H): 
    t_rad = np.radians(H)
    z2 = z1
    x2 = x1 * np.cos(H) - y1 * np.sin(H)
    y2 = x1 * np.sin(H) + y1 * np.cos(H)
    return x2, y2, z2

x2, y2, z2 = Oz(x1, y1, z1, H)  
x3, y3, z3 = Oy(x2, y2, z2, A) 
x4, y4, z4 = Ox(x3, y3, z3, a) 

ax.scatter(x4, y4, z4, c='r') 

plt.savefig("fig_7.png")