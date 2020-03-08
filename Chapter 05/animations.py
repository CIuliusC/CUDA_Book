# -*- coding: utf-8 -*-
"""animations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vcj1jF5tdkNESK91-3o5UK7NNQc2C2JR

https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/

The animation tools center around the ```matplotlib.animation.Animation``` base class. The main interfaces are ```TimedAnimation``` and ```FuncAnimation```. We here consider the ```FuncAnimation``` tool.

Standard imports. Note that ```rc``` is a standard acronym for "run command" or "runtime configuration". Moreover, ```IPython``` is a library for interactive data visualization.
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation, rc
from IPython.display import HTML

"""We need to create a figure window and the line object which will be modified in the animation.

```pyplot.subplots``` creates a figure and a grid of subplots with a single call. ```subplots()``` without arguments returns a Figure and a single Axes. This is actually the simplest and recommended way of creating a single ```Figure``` and ```Axes```.
"""

fig, ax = plt.subplots()
plt.close()

"""Set the ```x```- and ```y```-axis view limits."""

ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))

"""Plot ```y``` versus ```x``` as lines and/or markers. Set the ```linewidth``` or ```lw``` to ```2```. We simply plot an empty line: we will add data to the line later."""

line, = ax.plot([], [], lw = 2)

"""The ```animate``` function has a single parameter as input, namely ```i```, which acts as time and draws a sinusoidal moving right. Once again, we return a tuple of the modified plot objects. This tells the animation framework what parts of the plot should be animated."""

def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return (line, )

"""Create the animation object. The object needs to persist, so it must be assigned to a variable. A ```100``` frames animation with a ```50ms``` delay between frames is run. ```blit``` tells the animation to only re-draw the pieces of the plot which have changed. With ```blit = True```, the animations display much more quickly. Saving option is also set."""

anim = animation.FuncAnimation(fig, animate, frames = 100, interval = 50, blit = True)
anim.save('animationTest.mp4', fps = 30, extra_args=['-vcodec', 'libx264'])

"""Below is the part which makes it work on Colab. ```jshtml``` creates a javascript animation."""

rc('animation', html = 'jshtml')
anim