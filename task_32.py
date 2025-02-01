import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def heart_coords(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

t = np.linspace(0, 12 * np.pi, 100)
x, y = heart_coords(t)

fig, ax = plt.subplots()
heart, = plt.plot([], [], 'o', color ="r", label = 'heart' )
heart_line, = plt.plot([], [], '-', color = 'r', label = "heart")
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
plt.axis('equal')

def animate(i):
    
    heart_line.set_data(x[:i], y[:i])
    return heart_line,


ani = FuncAnimation(fig, animate, frames=len(t), interval=30)
ani.save('animation_32.gif', writer = "pillow")