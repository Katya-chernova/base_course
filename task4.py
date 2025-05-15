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

x1 = R * np.cos(phi)
y1 = R * np.sin(phi)
z1 = np.zeros_like(phi)

x_1 = R * np.cos(phi)
y_1 = R * np.sin(phi)
z_1 = np.zeros(100)

a = np.radians(40)    
A = np.radians(250) 
H = np.radians(50) 

x_2 = x_1
y_2 = y_1 * np.cos(a) - z_1 * np.sin(a)
z_2 = y_1 * np.sin(a) + z_1 * np.cos(a)

x2 = x1
y2 = y1 * np.cos(a) - z1 * np.sin(a)
z2 = y1 * np.sin(a) + z1 * np.cos(a)

x3 = x2 * np.cos(H) + z2 * np.sin(H)
y3 = y2
z3 = -x2 * np.sin(H) + z2 * np.cos(H)

x_3 = x3 * np.cos(A) - y3 * np.sin(A)
y_3 = x3 * np.sin(A) + y3 * np.cos(A)
z_3 = z3
ax.plot(x_1, y_1, z_1, color='r' )

ax.plot(x_2, y_2, z_2, color='orange')

ax.plot(x_3, y_3, z_3, color='y')


a_tok = (40)  
b_tok = 250  
t_tok = (50)  

a_rad = np.radians(a_tok)
b_rad = np.radians(b_tok)
t_rad = np.radians(t_tok)

x0 = R * np.cos(b_rad) * np.cos(t_rad)  
y0 = R * np.cos(b_rad) * np.sin(t_rad)
z0 = R * np.sin(b_rad)

x1_tok = x0
y1_tok = y0 * np.cos(a_rad) - z0 * np.sin(a_rad)
z1_tok = y0 * np.sin(a_rad) + z0 * np.cos(a_rad)

x2_tok = x1_tok * np.cos(A) + z1_tok * np.sin(A) 
y2_tok = y1_tok
z2_tok = -x1_tok * np.sin(A) + z1_tok * np.cos(A)

x_3_tok = x2_tok * np.cos(H) - y2_tok * np.sin(H)
y_3_tok = x2_tok * np.sin(H) + y2_tok * np.cos(H)
z_3_tok = z2_tok


x0 = R * np.cos(np.radians(b_tok)) * np.cos(np.radians(a_tok))
y0 = R * np.cos(np.radians(b_tok)) * np.sin(np.radians(a_tok))
z0 = R * np.sin(np.radians(b_tok))

ax.scatter(x0, y0, z0,s=50, color='red')
plt.savefig("fig_7.png")