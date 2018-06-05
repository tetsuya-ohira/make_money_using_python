import matplotlib.pyplot as plt
import numpy as np
import math

e = math.e
print(e)

dx = 0.1
x = np.arange(-5, 5, dx)

plt.plot(x, e**x)
plt.plot(x, (e**(x+dx) - e**x) / dx)
plt.show()
