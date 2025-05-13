import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

phi = np.linspace(0, 2*np.pi, 100)
theta = np.linspace(0, np.pi, 100) 
R = 5  

x = R * np.outer(np.cos(phi), np.sin(theta))
y = R * np.outer(np.sin(phi), np.sin(theta))
z = R * np.outer(np.ones(np.size(phi)), np.cos(theta))

ax.plot_wireframe(x, y, z, rstride=10, cstride=10)

x_1 = R * np.cos(phi)
y_1 = R * np.sin(phi)
z_1 = np.zeros(100)
ax.plot(x_1, y_1, z_1, color='r', linestyle='--')

a = np.radians(-10)      
b = np.radians(50)
t = np.radians(-10)

def Ox(x1, y1, z1, a):
    a_rad = np.radians(a)
    x2 = x1
    y2 = y1 * np.cos(a_rad) - z1 * np.sin(a_rad) 
    z2 = y1 * np.sin(a_rad) + z1 * np.cos(a_rad) 
    return x2, y2, z2

def Oy(x1, y1, z1, b): 
    b_rad = np.radians(b)
    y2 = y1
    x2 = x1 * np.cos(b_rad) + z1 * np.sin(b_rad)  
    z2 = -x1 * np.sin(b_rad) + z1 * np.cos(b_rad) 
    return x2, y2, z2

def Oz(x1, y1, z1, t): 
    t_rad = np.radians(t)
    z2 = z1
    x2 = x1 * np.cos(t_rad) - y1 * np.sin(t_rad)   
    y2 = x1 * np.sin(t_rad) + y1 * np.cos(t_rad)   
    return x2, y2, z2

x2, y2, z2 = Oz(x_1, y_1, z_1, t)
x3, y3, z3 = Oy(x2, y2, z2, b)
x4, y4, z4 = Ox(x3, y3, z3, a)

ax.scatter(x4, y4, z4, c='r')

x_1_tilted = x_1
y_1_tilted = y_1 * np.cos(a) - z_1 * np.sin(a)
z_1_tilted = y_1 * np.sin(a) + z_1 * np.cos(a)


x1 = x_1
y1 = y_1 * np.cos(a) - z_1 * np.sin(a)
z1 = y_1 * np.sin(a) + z_1 * np.cos(a)


x2 = x1 * np.cos(b) + z1 * np.sin(b)
y2 = y1
z2 = -x1 * np.sin(b) + z1 * np.cos(b)


x_3 = x2 * np.cos(t) - y2 * np.sin(t)
y_3 = x2 * np.sin(t) + y2 * np.cos(t)
z_3 = z2


ax.plot(x_1, y_1, z_1, 'gray', linestyle='--')
ax.plot(x_1_tilted, y_1_tilted, z_1_tilted, 'y')
ax.scatter(x_3, y_3, z_3, color='green')


plt.savefig("fig_7.png")
