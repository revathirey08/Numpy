import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering, DBSCAN


data = {
    "StudyHours": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Attendance": [60, 65, 70, 72, 78, 82, 85, 90, 94, 96],
    "Marks": [45, 50, 55, 60, 68, 72, 78, 85, 90, 95]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)


X = df[["StudyHours", "Attendance", "Marks"]]




scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nScaled Data:")
print(X_scaled)



kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

df["Cluster"] = kmeans.fit_predict(X_scaled)

print("\nK-Means Result:")
print(df)




print("\nCluster Centers:")
print(kmeans.cluster_centers_)



inertia = []

for k in range(1, 7):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)

    inertia.append(model.inertia__)


plt.plot(range(1, 7), inertia, marker="o")

plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method")

plt.show()



