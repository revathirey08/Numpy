import numpy as np
from sklearn.linear_model import LogisticRegression


X = np.array([[1], [2], [3], [4], [5], [6]])


y = np.array([0, 0, 0, 1, 1, 1])


model = LogisticRegression()


model.fit(X, y)

new_data = np.array([[5]])


result = model.predict(new_data)

print("Prediction:", result[0])