from sklearn import datasets
import numpy as np

def log_data():
    iris = datasets.load_iris()
    X = iris["data"][:, 3:]
    Y = (iris["target"] == 2).astype(np.int_)
    return X, Y