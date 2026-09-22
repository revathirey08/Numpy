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




print("\nName Column:")
print(df["Name"])




print("\nName and Mark Columns:")
print(df[["Name", "Mark"]])




print("\nFirst Row using loc:")
print(df.loc[0])


print("\nThird Row using loc:")
print(df.loc[2])



print("\nFirst Row using iloc:")
print(df.iloc[0])


print("\nThird Row using iloc:")
print(df.iloc[2])




print("\nFirst Student Name:")
print(df.loc[0, "Name"])


print("\nThird Student Mark:")
print(df.loc[2, "Mark"])



print("\nFirst 3 Rows:")
print(df.iloc[0:3])


print("\nRows 2 to 4:")
print(df.iloc[1:4])



print("\nFirst 2 Columns:")
print(df.iloc[:, 0:2])


print("\nName to Mark:")
print(df.loc[:, "Name":"Mark"])



print("\nSelected Rows and Columns:")
print(df.loc[0:2, ["Name", "Mark"]])



print("\nUsing loc:")
print(df.loc[1, "Name"])


print("\nUsing iloc:")
print(df.iloc[1, 0])