import numpy as np
import matplotlib.pyplot as plt
fix, ax = plt.subplots(subplot_kw={"projection": "3d"})

R = 5  

phi = np.linspace(0, 2 * np.pi, 100)  
theta = np.linspace(0, np.pi, 100)  

x = R * np.outer(np.cos(phi), np.sin(theta))
y = R * np.outer(np.sin(phi), np.sin(theta))
z = R * np.outer(np.ones(np.size(phi)), np.cos(theta))

ax.plot_wireframe(x, y, z, rstride=10, cstride=10)

x_1 = R * np.cos(phi)
y_1 = R * np.sin(phi)
z_1 = np.zeros(100)

a = np.radians(10)      
b = np.radians(-50) 
t = np.radians(10)

x1 = x_1
y1 = y_1 * np.cos(a) - z_1 * np.sin(a)
z1 = y_1 * np.sin(a) + z_1 * np.cos(a)

x2 = x1 * np.cos(b) + z1 * np.sin(b)
y2 = y1
z2 = -x1 * np.sin(b) + z1 * np.cos(b)

x3 = x2 * np.cos(t) - y2 * np.sin(t)
y3 = x2 * np.sin(t) + y2 * np.cos(t)
z3 = z2

ax.plot(x1, y1, z1, 'r')

ax.plot(x2, y2, z2, 'orange')

ax.plot(x3, y3, z3, color='y')

x0 = R * np.cos(a) * np.cos(t)
y0 = R * np.cos(a) * np.sin(t)
z0 = R * np.sin(a)

x1_tok = x0
y1_tok = y0 * np.cos(a) - z0 * np.sin(a)
z1_tok = y0 * np.sin(a) + z0 * np.cos(a)

x2_tok = x1_tok * np.cos(b) + z1_tok * np.sin(b)
y2_tok = y1_tok
z2_tok = -x1_tok * np.sin(b) + z1_tok * np.cos(b)

x3_tok = x2_tok * np.cos(t) - z2_tok * np.sin(t)
y3_tok = x2_tok * np.sin(t) + z2_tok * np.cos(t)
z3_tok = z2_tok



ax.scatter(x3_tok, y3_tok, z3_tok, s=50, color='red')

plt.savefig("fig_6.png") 