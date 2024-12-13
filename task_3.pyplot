import matplotlib.pyplot as plt
import numpy as np


def ellipse_plotter(xmin, xmax, n, a=10, b=5):
    x = np.linspace(xmin, xmax, n)
    y = np.linspace(xmin, xmax, n)

    X, Y = np.meshgrid(x, y)
    fxy = (X**2 / a**2) + (Y**2 / b**2) - 1

    plt.contour(X, Y, fxy, levels=[0])  
    plt.xlabel('coord -x')
    plt.ylabel('coord -y')
    plt.title('Ellipse')
    plt.axis('equal') 
    

xmin = -10
xmax = 10
n = 100
ellipse_plotter(xmin, xmax, n)

plt.savefig('fig_7.png')

