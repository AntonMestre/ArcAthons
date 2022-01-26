import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

mpl.rcParams['lines.color'] = 'k'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])

x = np.linspace(-1, 1, 400)
y = np.linspace(-1, 1, 400)
x, y = np.meshgrid(x, y)

def axes():
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)

def parabole1(x,y) :
    return 4*(deltaD12**2)*((x-x2)**2+(y-y2)**2) - ((x-x1)**2 + (y-y1)**2 - (x-x2)**2 - (y-y2)**2 - deltaD12**2)**2

def parabole2(x,y) :
    return 4*(deltaD13**2)*((x-x3)**2+(y-y3)**2) - ((x-x1)**2 + (y-y1)**2 - (x-x3)**2 - (y-y3)**2 - deltaD13**2)**2


def f(input):
    xi,yi = input
    res = np.zeros(2)
    res[0] = parabole1(xi,yi)
    res[1] = parabole2(xi,yi)
    return res


x1 = -1
y1 = 1
x2 = 1
y2 = 1
x3 = 1
y3 = -1
deltaD12 = 0.9
deltaD13 = 0.5

x0 = np.array([-1, 1])
solution = fsolve(f, x0)
print(solution)

axes()

plt.contour(x, y, parabole1(x,y), [0], colors='k')
plt.contour(x, y, parabole2(x,y), [0], colors='r')

plt.show()