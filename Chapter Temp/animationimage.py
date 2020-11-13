# -*- coding: utf-8 -*-
"""animationImage.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GXlQWresL3jX8MN7f2Krdw78YAAzuBtQ
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import animation, rc
from IPython.display import HTML

fig = plt.figure()

def f(x, y):
    return np.sin(x) + np.cos(y)

x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)

im = plt.imshow(f(x, y), interpolation = 'none')

def animate(i):
    global x, y
    x += np.pi / 15.
    y += np.pi / 20.
    a = im.get_array()
    a = f(x, y)
    im.set_array(a)
    return [im]
    
anim = animation.FuncAnimation(fig, animate, frames = 60, interval = 50, blit = True)

rc('animation', html = 'jshtml')
anim
