import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split



data = {
    "Name": ["Revathi", "Priya", "Divya", "Anu", "Kavi", "Revathi"],
    "Age": [20, 21, 20, None, 21, 20],
    "Gender": ["Female", "Female", "Female", "Female", "Female", "Female"],
    "StudyHours": [5, 6, 4, 7, 8, 5],
    "Attendance": [85, 90, 80, 95, 92, 85],
    "Mark": [85, 90, 78, 95, 88, 85]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)




print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)



print("\nMissing Values:")
print(df.isnull().sum())




df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nAfter Filling Missing Value:")
print(df)



df = df.drop_duplicates()

print("\nAfter Removing Duplicate:")
print(df)




encoder = LabelEncoder()

df["Gender"] = encoder.fit_transform(df["Gender"])

print("\nAfter Encoding:")
print(df)



X = df[["Age", "Gender", "StudyHours", "Attendance"]]

y = df["Mark"]

print("\nFeatures:")
print(X)

print("\nTarget:")
print(y)



scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nScaled Features:")
print(X_scaled)




X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)

print("\nTraining Target:")
print(y_train)

print("\nTesting Target:")
print(y_test)