import numpy as np

import data
import linreg

X_new = np.array([[0], [2]])
X, Y = data.gen_data()
Y_predict = linreg.predict(X, Y, X_new)
data.plot(X, Y, X_new, Y_predict)