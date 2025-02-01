import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ex = plt.subplots()

anim_object, = plt.plot ([], [], '-', lw=2)

x, y = [], []
frames_interval = np.linspace(0, 2*np.pi, 100)

ex.set_xlim(-8, 8)
ex.set_ylim(-8, 8)
plt.axis('equal')
a = 3

def update(frame):
    r = a * frame
    x = r * np.cos(np.linspace(0, 2 * np.pi, 100)) 
    y = r * np.sin(np.linspace(0, 2 * np.pi, 100))

    anim_object.set_data(x, y)
    return anim_object,

ani = FuncAnimation(fig, update, frames=frames_interval, interval = 50)

ani.save('animatioin_21.gif', writer="pillow")