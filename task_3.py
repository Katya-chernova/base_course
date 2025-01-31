import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def butterfly_coords(t):
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + np.sin(t/12)**5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + np.sin(t/12)**5)
    return x, y

t = np.linspace(0, 12 * np.pi, 100)
x, y = butterfly_coords(t)

fig, ax = plt.subplots()
butterfly, = plt.plot([], [], 'o', color ="r", label = 'butterfly' )
butterfly_line, = plt.plot([], [], '-', color = 'r', label = "butterfly")
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')

def animate(i):
    
    butterfly_line.set_data(x[:i], y[:i])
    return butterfly_line,

ani = FuncAnimation(fig, animate, frames=len(t), interval=30)
ani.save('animation_31.gif', writer = "pillow")