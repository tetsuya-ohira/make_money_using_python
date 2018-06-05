import matplotlib.pyplot as plt
import numpy as np
import math

def sigmoid(a):
	return ( 1 / (1 + math.e**-a))

dx = 0.1
x = np.arange(-8, 8, dx)

plt.plot(x , sigmoid(x))
plt.show()
