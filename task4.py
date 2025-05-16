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

a = np.radians(40)      
H = np.radians(250) 
A = np.radians(50)

x1 = x_1
y1 = y_1 * np.cos(a) - z_1 * np.sin(a)
z1 = y_1 * np.sin(a) + z_1 * np.cos(a)

x2 = x1 * np.cos(H) + z1 * np.sin(H)
y2 = y1
z2 = -x1 * np.sin(H) + z1 * np.cos(H)

x3 = x2 * np.cos(A) - y2 * np.sin(A)
y3 = x2 * np.sin(A) + y2 * np.cos(A)
z3 = z2

ax.plot(x_1, y_1, z_1, 'r')

ax.plot(x1, y1, z1, 'orange')

ax.plot(x3, y3, z3, color='y')

x0 = R * np.cos(a) * np.cos(A)
y0 = R * np.cos(a) * np.sin(A)
z0 = R * np.sin(a)

x1_tok = x0
y1_tok = y0 * np.cos(a) - z0 * np.sin(a)
z1_tok = y0 * np.sin(a) + z0 * np.cos(a)

x2_tok = x1_tok * np.cos(H) + z1_tok * np.sin(H)
y2_tok = y1_tok
z2_tok = -x1_tok * np.sin(H) + z1_tok * np.cos(H)

new_A_tok = A + 5  
A_tok = np.radians(new_A_tok)

x3_tok = x2_tok * np.cos(A_tok) - y2_tok * np.sin(A_tok)
y3_tok = x2_tok * np.sin(A_tok) + y2_tok * np.cos(A_tok)
z3_tok = z2_tok

ax.scatter(x3_tok, y3_tok, z3_tok, s=50, color='red')

plt.savefig("fig_7.png")
