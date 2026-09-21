import pandas as pd

# Pandas version
print("Pandas Version:")
print(pd.__version__)



marks = [80, 75, 90, 85, 95]

series = pd.Series(marks)

print("\nSeries:")
print(series)



print("\nFirst Mark:")
print(series[0])

print("\nThird Mark:")
print(series[2])



data = {
    "Name": ["Revathi", "Priya", "Divya", "Anu"],
    "Age": [20, 21, 20, 22],
    "Mark": [90, 85, 95, 88]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)


print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)



print("\nNames:")
print(df["Name"])

print("\nMarks:")
print(df["Mark"])


print("\nFirst Student Name:")
print(df["Name"][0])

print("\nFirst Student Mark:")
print(df["Mark"][0])


print("\nFirst 2 Rows:")
print(df.head(2))

print("\nLast 2 Rows:")
print(df.tail(2))



print("\nDataFrame Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())