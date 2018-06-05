#coding: UTF-8
import matplotlib.pyplot as plt
import numpy as np
import math

def sigmoid(a):
	return ( 1 / (1 + math.e**-a))

def dsigmoid(a):
    return sigmoid(a)*(1-sigmoid(a))

dx = 0.1
x = np.arange(-8, 8, dx)
sig = sigmoid(x)
dsig = (sigmoid(x + dx) - sigmoid(x)) / dx
dsig2 = dsigmoid(x)

plt.plot(x , sig)
plt.plot(x , dsig)
plt.plot(x , dsig2)
plt.show()
