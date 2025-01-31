from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def fractal_point(x0, y0, C, D, n):
    x = [x0]
    y = [y0]
    for i in range(1, n):
        xn = x[i-1]**2 - y[i-1]**2 + C
        yn = 2 * x[i-1] * y[i-1] + D
        x.append(xn)
        y.append(yn)
    return x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')

def animate(i):
    x, y = fractal_point(x0=0.1, y0=0.1, C=0.3, D=0.33, n=i+1)
    ball.set_data(x, y)
    return ball,

edge = 1
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('animation_4.gif', writer="pillow")
