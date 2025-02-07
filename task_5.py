import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def star_t(t):
    x = 12 * np.cos(t) + 8 * np.cos(1.5*t)
    y = 12 * np.sin(t) - 8 * np.sin(1.5*t)
    return x, y

def star_t1(x, y, t1):
    X = x * np.cos(t1) - y * np.sin(t1)
    Y = y * np.cos(t1) + x * np.sin(t1)
    return X, Y

fig, ax = plt.subplots()
star, = plt.plot([], [], lw=2)  

edge = 25
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ax.set_aspect('equal') 


def animate(i):
    t = np.linspace(0, 4*np.pi, 200) 
    x, y = star_t(t)
    t1 = 0.05 * i 
    X, Y = star_t1(x, y, t1)
    star.set_data(X, Y)
    return star,  

ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=False) 
ani.save('animation_5.gif', writer='pillow')

plt.show()
