from sklearn.linear_model import LinearRegression

def predict(X, Y, X_new):
    lin_reg = LinearRegression()
    lin_reg.fit(X, Y)
    return lin_reg.predict(X_new)