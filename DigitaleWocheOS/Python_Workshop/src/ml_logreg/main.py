from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
import data


log_reg = LogisticRegression()
X, Y = data.log_data()
log_reg.fit(X, Y)
X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
y_proba = log_reg.predict_proba(X_new)

plt.ioff()
plt.plot(X_new, y_proba[:, 1], "g--", label="Iris virginica")
plt.plot(X_new, y_proba[:, 0], "b--", label="Nicht Iris virginica")
plt.show()