#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

#compute the x and y coords for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.title("Sine wave form")

#Plot the points using matplotlib
plt.plot(x,y)
plt.show()
