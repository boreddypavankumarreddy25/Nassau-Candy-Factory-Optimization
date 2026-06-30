import pandas as pd

# Load dataset
df = pd.read_csv("Nassau Candy Distributor.csv")

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

print("\nDATA TYPES")
print(df.info())

print("\nMISSING VALUES")
print(df.isnull().sum())