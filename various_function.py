import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 15, 0.1)
y2d = x**2 - 10 * x  + 10
y3d = x**3 - 10*x**2  + 10

plt.plot(x, y2d)
plt.plot(x, y3d)
plt.show()
