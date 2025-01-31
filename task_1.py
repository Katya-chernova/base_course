import matplotlib.pyplot as plt
import numpy as np

def circle_plotter(R=8):
    t = np.arange (-2*np.pi, 2*np.pi, 0.1)

    x = R * (t - np.sin(t)**3)
    y = R * (1 - np.cos(t)**3)

    plt.plot(x, y, ls='--', lw=3)
    plt.axis('equal')
    plt.savefig('fig_21.png')

if __name__ == '__main__':
    circle_plotter()