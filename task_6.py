import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

side = 10 
frames = 360  
interval = 20  

def square(side):
    x_coords = [-side/2, side/2, side/2, -side/2, -side/2]
    y_coords = [-side/2, -side/2, side/2, side/2, -side/2]
    return x_coords, y_coords

def square_angle(x, y, angle):
    radians = np.radians(angle)
    X = x * np.cos(radians) - y * np.sin(radians)
    Y = x * np.sin(radians) + y * np.cos(radians)
    return X, Y

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

ax.set_xlim(-15, 15)  
ax.set_ylim(-15, 15) 
ax.set_aspect('equal') 

def animate(frame):
    angle = frame  
    x_coords, y_coords = square(side)
    angle_x = []
    angle_y = []
    for i in range(len(x_coords)):
        x, y = x_coords[i], y_coords[i]
        X, Y = square_angle(x, y, angle)  
        angle_x.append(X)
        angle_y.append(Y)

    line.set_data(angle_x, angle_y)  
    return line,

ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 360, 1), interval=interval, blit=False)
ani.save("animation_6.gif", writer='pillow')

plt.show()
