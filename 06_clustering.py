import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

print("="*70)
print("NASSAU CANDY - ROUTE CLUSTERING")
print("="*70)

# =====================================
# LOAD DATA
# =====================================

df = pd.read_excel("Nassau_Candy_Cleaned.xlsx")

# =====================================
# SELECT FEATURES FOR CLUSTERING
# =====================================

cluster_data = df[
    [
        "Sales",
        "Units",
        "Gross Profit",
        "Cost",
        "Lead Time"
    ]
]

# =====================================
# SCALE FEATURES
# =====================================

scaler = StandardScaler()

scaled_data = scaler.fit_transform(cluster_data)

# =====================================
# ELBOW METHOD
# =====================================

wcss = []

for i in range(1,11):

    kmeans = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )

    kmeans.fit(scaled_data)

    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8,5))

plt.plot(range(1,11), wcss, marker="o")

plt.title("Elbow Method")

plt.xlabel("Number of Clusters")

plt.ylabel("WCSS")

plt.grid(True)

plt.show()

# =====================================
# KMEANS MODEL
# =====================================

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(scaled_data)

print("\nCluster Counts\n")

print(df["Cluster"].value_counts())

# =====================================
# CLUSTER SUMMARY
# =====================================

summary = df.groupby("Cluster")[
[
"Sales",
"Units",
"Gross Profit",
"Cost",
"Lead Time"
]
].mean()

print("\nCluster Summary\n")

print(summary)

# =====================================
# VISUALIZATION
# =====================================

plt.figure(figsize=(9,6))

scatter = plt.scatter(
    df["Sales"],
    df["Gross Profit"],
    c=df["Cluster"]
)

plt.xlabel("Sales")

plt.ylabel("Gross Profit")

plt.title("Route Clusters")

plt.colorbar(scatter)

plt.show()

# =====================================
# SAVE DATASET
# =====================================

df.to_excel(
    "Nassau_Candy_Clustered.xlsx",
    index=False
)

print("\nClustered Dataset Saved Successfully!")