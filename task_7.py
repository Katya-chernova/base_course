import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def heart_t(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

def heart_t1(x, y, t1):
    X = x * np.cos(t1) - y * np.sin(t1)
    Y = y * np.cos(t1) + x * np.sin(t1)
    return X, Y

fig, ax = plt.subplots()
heart, = plt.plot([], [], lw=2)  

edge = 20
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ax.set_aspect('equal') 
  
def animate(i):
    t = np.linspace(0, 2*np.pi, 200) 
    x, y = heart_t(t)
    t1 = 0.5 * i 
    X, Y = heart_t1(x, y, t1)
    heart.set_data(X, Y)
    return heart, 

ani = FuncAnimation(fig, animate, frames=100, interval=50) 
ani.save('animation_5.gif', writer='pillow')

