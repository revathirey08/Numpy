import numpy as np
from sklearn.linear_model import LinearRegression


X = np.array([[1], [2], [3], [4], [5]])


y = np.array([10, 20, 30, 40, 50])


model = LinearRegression()


model.fit(X, y)


new_data = np.array([[6]])

result = model.predict(new_data)

print("Predicted value:", result[0])