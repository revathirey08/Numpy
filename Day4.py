import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score


data = {
    "StudyHours": [2, 3, 4, 5, 6, 7, 8, 9],
    "Attendance": [70, 75, 80, 85, 88, 90, 95, 98],
    "Mark": [45, 50, 55, 62, 68, 75, 82, 90]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)


X = df[["StudyHours", "Attendance"]]


y = df["Mark"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)


model = LinearRegression()


model.fit(X_train, y_train)


prediction = model.predict(X_test)

print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(prediction)

new_student = pd.DataFrame(
    [[7, 92]],
    columns=["StudyHours", "Attendance"]
)

result = model.predict(new_student)

print("\nNew Student Predicted Mark:")
print(result[0])



data2 = {
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [50, 55, 60, 65, 70, 80, 90, 95],
    "Selected": [0, 0, 0, 0, 1, 1, 1, 1]
}

df2 = pd.DataFrame(data2)

print("\n\nSelection Dataset:")
print(df2)

# Features
X = df2[["StudyHours", "Attendance"]]


y = df2["Selected"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)


model2 = LogisticRegression()


model2.fit(X_train, y_train)


prediction2 = model2.predict(X_test)

print("\nActual Selection:")
print(y_test.values)

print("\nPredicted Selection:")
print(prediction2)


accuracy = accuracy_score(y_test, prediction2)

print("\nAccuracy:")
print(accuracy)


new_candidate = pd.DataFrame(
    [[6, 85]],
    columns=["StudyHours", "Attendance"]
)

result2 = model2.predict(new_candidate)

print("\nNew Candidate Prediction:")

if result2[0] == 1:
    print("Selected")
else:
    print("Not Selected")