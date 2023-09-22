import numpy as np
import matplotlib.pyplot as plt

def gen_data():
    X = 3 * np.random.rand(1000, 1)
    Y = 4 + 3 * X + np.random.randn(1000, 1)
    return (X, Y)

def plot(X, Y, X_new, Y_predict):
    plt.plot(X_new, Y_predict, "r-")
    plt.plot(X, Y, "b.")
    plt.axis([0, 2, 0, 15])
    plt.ioff()
    plt.show()
