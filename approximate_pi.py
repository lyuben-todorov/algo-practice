import matplotlib.pyplot as plt
import numpy as np
import random as rand
import math as math
from matplotlib.animation import FuncAnimation as animation


fig, (ax1, ax2) = plt.subplots(2)

xdata, ydata = [], []
approxdata = []

quadrant = plt.Circle((0, 0), 1, color='r', fill=False, lw=2)
ax1.add_artist(quadrant)

it = 0;
ax2.axhline(3.14159265359, color = 'r',)

def approx_pi():
    global it
    inside = 0
    n = len(xdata)
    for i in range(n):
        if (math.sqrt(ydata[i]*ydata[i] + xdata[i]*xdata[i])) < 1:
            inside += 1
    approximation = 4*(inside/n)
    approxdata.append(approximation)
    ax2.clear()
    ax2.axhline(3.14159265359, color = 'r',)
    ax2.plot(approxdata, '-b')
    #ax2.plot([it],[approximation], '-o', color = 'red')
    plt.title(' n = ' + str(n) + ' PI = {0:.16f}' .format(approximation))
    # print( str(it) + ". n = " + str(n) + " PI = "  + str(approximation))
    # print(approximation)
    # print('\n')
    it+=1


def animate(i):
    framex, framey = [], []
    for i in range(0, 100):
        x = rand.random()
        y = rand.random()
        framex.append(x)
        framey.append(y)
    ax1.scatter(framex, framey, marker='.')
    xdata.extend(framex)
    ydata.extend(framey) 
    approx_pi()

ani = animation(fig, animate, interval=1, frames=500, repeat=False)


plt.show()
