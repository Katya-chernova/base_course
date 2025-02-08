import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def heart_t(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

def hyperbala(x_min,x_max,N):
    X = np.linspace(0, x_max, N+1)
    Y =  1/X
    return X, Y

fig, ax = plt.subplots()
heart, = plt.plot([], [], lw=2)  

edge = 20
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ax.set_aspect('equal') 

def animate(i):
    heart.set_data(hyperbala(-8, 8, 100, time=i))
    return heart

ani = FuncAnimation(fig, animate, frames=100, interval=50) 
ani.save('animation_7.gif', writer='pillow')