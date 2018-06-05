import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.1)
y = 2**x
z = 3**x

print(x)
print(y)

plt.plot(x, y)
plt.plot(x, z)
plt.show()
