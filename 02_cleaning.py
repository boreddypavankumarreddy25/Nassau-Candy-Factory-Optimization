import pandas as pd

# Load dataset
df = pd.read_csv("Nassau Candy Distributor.csv")

# -------------------------------
# Convert dates
# -------------------------------
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

# -------------------------------
# Create Lead Time
# -------------------------------
df["Lead Time"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

# -------------------------------
# Profit Margin (%)
# -------------------------------
df["Profit Margin (%)"] = (
    df["Gross Profit"] / df["Sales"]
) * 100

# -------------------------------
# Cost Per Unit
# -------------------------------
df["Cost Per Unit"] = (
    df["Cost"] / df["Units"]
)

# -------------------------------
# Sales Per Unit
# -------------------------------
df["Sales Per Unit"] = (
    df["Sales"] / df["Units"]
)

# -------------------------------
# Check New Dataset
# -------------------------------
print(df.head())

print("\nNew Columns:")
print(df.columns)

print("\nLead Time Statistics:")
print(df["Lead Time"].describe())

print("\nProfit Margin Statistics:")
print(df["Profit Margin (%)"].describe())

# Save cleaned dataset
df.to_excel("Nassau_Candy_Cleaned.xlsx", index=False)

print("\nCleaned dataset saved successfully.")