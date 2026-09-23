import pandas as pd


data = {
    "Name": ["Revathi", "Priya", "Divya", "Anu", "Kavi"],
    "Age": [20, 21, 20, 22, 21],
    "Mark": [90, 85, 95, 88, 92],
    "City": ["Cuddalore", "Chennai", "Pondy", "Salem", "Madurai"]
}

df = pd.DataFrame(data)

print("\nOriginal DataFrame:")
print(df)



df["Grade"] = ["A", "B", "A+", "B+", "A"]

print("\nAfter Adding Grade:")
print(df)



df["Mark"] = [95, 88, 96, 90, 94]

print("\nAfter Updating Marks:")
print(df)



df.loc[0, "Mark"] = 100

print("\nAfter Updating Revathi Mark:")
print(df)



df.loc[len(df)] = ["Meena", 20, 89, "Trichy", "B+"]

print("\nAfter Adding New Student:")
print(df)



df.loc[0:2, "Grade"] = ["A+", "A", "A+"]

print("\nAfter Updating Multiple Grades:")
print(df)



df = df.drop("Age", axis=1)

print("\nAfter Deleting Age Column:")
print(df)


df = df.drop(2, axis=0)

print("\nAfter Deleting Row 2:")
print(df)



df = df.rename(columns={"Name": "Student_Name"})

print("\nAfter Renaming Name Column:")
print(df)



df = df.reset_index(drop=True)

print("\nAfter Resetting Index:")
print(df)



new_df = df.copy()

print("\nCopied DataFrame:")
print(new_df)