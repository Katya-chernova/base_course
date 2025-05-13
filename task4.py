import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

phi = np.linspace(0, 2*np.pi, 100) # Угол phi (азимут)
theta = np.linspace(0, np.pi, 100)  # Угол theta (зенит)
R = 5  

x = R * np.outer(np.cos(phi), np.sin(theta))
y = R * np.outer(np.sin(phi), np.sin(theta))
z = R * np.outer(np.ones(np.size(phi)), np.cos(theta))

ax.plot_wireframe(x, y, z, rstride=10, cstride=10)

x_1 = R * np.cos(phi)
y_1 = R * np.sin(phi)
z_1 = np.zeros(100)
ax.plot(x_1, y_1, z_1, color='g', linestyle='--')

a = 40  
A = 250 
H = 50  

x1 = R * np.cos(A/180*np.pi) * np.cos(a/180*np.pi)  # Перевод градусов в радианы
y1 = R * np.cos(A/180*np.pi) * np.sin(a/180*np.pi)
z1 = R * np.sin(A/180*np.pi)

def Ox(x1, y1, z1, a): 
    a_rad = np.radians(a)
    x2 = x1
    y2 = y1 * np.cos(a_rad) - z1 * np.sin(a_rad)
    z2 = y1 * np.sin(a_rad) + z1 * np.cos(a_rad)
    return x2, y2, z2

def Oy(x1, y1, z1, A): 
    b_rad = np.radians(A)
    y2 = y1
    x2 = x1 * np.cos(b_rad) + z1 * np.sin(b_rad)
    z2 = -x1 * np.sin(b_rad) + z1 * np.cos(b_rad)
    return x2, y2, x2

def Oz(x1, y1, z1, H): 
    t_rad = np.radians(H)
    z2 = z1
    x2 = x1 * np.cos(t_rad) - y1 * np.sin(t_rad)
    y2 = x1 * np.sin(t_rad) + y1 * np.cos(t_rad)
    return x2, y2, z2

x2, y2, z2 = Oz(x1, y1, z1, H)
x3, y3, z3 = Oy(x2, y2, z2, A)
x4, y4, z4 = Ox(x3, y3, z3, a)

ax.scatter(x4, y4, z4, c='r')

x1 = R * np.cos(a/180*np.pi) * np.cos(a/180*np.pi) 
y1 = R * np.cos(a/180*np.pi) * np.sin(a/180*np.pi)
z1 = R * np.sin(a/180*np.pi)

ygt = np.linspace(0, 2*np.pi, 100)
x_2 = x1
y_2 = y1 * np.cos(ygt) - z1 * np.sin(ygt)
z_2 = y1 * np.sin(ygt) + z1 * np.cos(ygt)
ax.plot(x_2, y_2, z_2, color='y', linestyle='--')

x2 = R * np.cos(A/180*np.pi) * np.cos(a/180*np.pi)
y2 = R * np.cos(A/180*np.pi) * np.sin(a/180*np.pi)
z2 = R * np.sin(A/180*np.pi)

frt = np.linspace(0, 2*np.pi, 100)
x_3 =  y2
y_3 = x2 * np.cos(frt) + z2 * np.sin(frt)
z_3 = -x2 * np.sin(frt) + z2 * np.cos(frt)
ax.plot(x_3, y_3, z_3, color='b', linestyle='--')

x3 = R * np.cos(H/180*np.pi) * np.cos(a/180*np.pi)
y3 = R * np.cos(H/180*np.pi) * np.sin(a/180*np.pi)
z3 = R * np.sin(H/180*np.pi)

qaz = np.linspace(0, 2*np.pi, 100)
x_4 =  z3
y_4 = x3 * np.cos(qaz) - y3 * np.sin(qaz)
z_4 = x3 * np.sin(qaz) + y3 * np.cos(qaz)
ax.plot(x_4, y_4, z_4, color='c', linestyle='--')

plt.savefig("fig_7.png")


