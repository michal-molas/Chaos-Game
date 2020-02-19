import random
from math import *
import matplotlib.pyplot as plt

def plot_k_gon(k):
    #k-kąt
    X = [0]
    Y = [0]
    for n in range(100000):
        r = random.randint(0, k-1)
        a = r/k*2*pi
        px = sin(a)
        py = cos(a)
        x = (px + X[n-1])/(k-1)
        y = (py + Y[n-1])/(k-1)
        X.append(x)
        Y.append(y)

    plt.figure(figsize = [10,20])
    plt.scatter(X, Y, marker = '.',s=0.01)
    plt.show()

plot_k_gon(4)
