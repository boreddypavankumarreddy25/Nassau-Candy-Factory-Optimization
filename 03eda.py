import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================
# LOAD DATA
# ============================================

df = pd.read_excel("Nassau_Candy_Cleaned.xlsx")

print("="*70)
print("NASSAU CANDY DATASET")
print("="*70)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst Five Rows:")
print(df.head())

# ============================================
# BUSINESS OVERVIEW
# ============================================

print("\n" + "="*70)
print("BUSINESS OVERVIEW")
print("="*70)

print("Total Sales            : $", round(df["Sales"].sum(),2))
print("Total Gross Profit     : $", round(df["Gross Profit"].sum(),2))
print("Total Orders           :", df["Order ID"].nunique())
print("Total Customers        :", df["Customer ID"].nunique())
print("Total Products         :", df["Product Name"].nunique())
print("Average Lead Time      :", round(df["Lead Time"].mean(),2))
print("Average Profit Margin  :", round(df["Profit Margin (%)"].mean(),2),"%")

# ============================================
# SALES BY DIVISION
# ============================================

sales_division = df.groupby("Division")["Sales"].sum().sort_values(ascending=False)

print("\nSales by Division")
print(sales_division)

plt.figure(figsize=(8,5))
sales_division.plot(kind="bar")
plt.title("Sales by Division")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ============================================
# SALES BY REGION
# ============================================

sales_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print("\nSales by Region")
print(sales_region)

plt.figure(figsize=(8,5))
sales_region.plot(kind="bar", color="orange")
plt.title("Sales by Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ============================================
# GROSS PROFIT BY REGION
# ============================================

profit_region = df.groupby("Region")["Gross Profit"].sum().sort_values(ascending=False)

print("\nGross Profit by Region")
print(profit_region)

plt.figure(figsize=(8,5))
profit_region.plot(kind="bar", color="green")
plt.title("Gross Profit by Region")
plt.ylabel("Gross Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ============================================
# SHIP MODE DISTRIBUTION
# ============================================

ship_mode = df["Ship Mode"].value_counts()

print("\nShip Mode Distribution")
print(ship_mode)

plt.figure(figsize=(7,7))
plt.pie(
    ship_mode,
    labels=ship_mode.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Ship Mode Distribution")
plt.show()

# ============================================
# TOP 10 PRODUCTS BY SALES
# ============================================

top_sales = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Sales")
print(top_sales)

plt.figure(figsize=(12,5))
top_sales.plot(kind="bar", color="purple")
plt.title("Top 10 Products by Sales")
plt.ylabel("Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# ============================================
# TOP 10 PRODUCTS BY PROFIT
# ============================================

top_profit = (
    df.groupby("Product Name")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Gross Profit")
print(top_profit)

plt.figure(figsize=(12,5))
top_profit.plot(kind="bar", color="red")
plt.title("Top 10 Products by Gross Profit")
plt.ylabel("Gross Profit")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# ============================================
# LEAD TIME BY REGION
# ============================================

lead_region = (
    df.groupby("Region")["Lead Time"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Lead Time by Region")
print(lead_region)

plt.figure(figsize=(8,5))
lead_region.plot(kind="bar", color="teal")
plt.title("Average Lead Time by Region")
plt.ylabel("Lead Time")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ============================================
# LEAD TIME BY SHIP MODE
# ============================================

lead_ship = (
    df.groupby("Ship Mode")["Lead Time"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Lead Time by Ship Mode")
print(lead_ship)

plt.figure(figsize=(8,5))
lead_ship.plot(kind="bar", color="brown")
plt.title("Average Lead Time by Ship Mode")
plt.ylabel("Lead Time")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# ============================================
# SALES DISTRIBUTION
# ============================================

plt.figure(figsize=(8,5))
plt.hist(df["Sales"], bins=30)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ============================================
# PROFIT MARGIN DISTRIBUTION
# ============================================

plt.figure(figsize=(8,5))
plt.hist(df["Profit Margin (%)"], bins=30)
plt.title("Profit Margin Distribution")
plt.xlabel("Profit Margin (%)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ============================================
# CORRELATION HEATMAP
# ============================================

corr = df[
    [
        "Sales",
        "Units",
        "Cost",
        "Gross Profit",
        "Lead Time",
        "Profit Margin (%)"
    ]
].corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# ============================================
# SALES VS PROFIT
# ============================================

plt.figure(figsize=(8,5))
plt.scatter(df["Sales"], df["Gross Profit"])
plt.title("Sales vs Gross Profit")
plt.xlabel("Sales")
plt.ylabel("Gross Profit")
plt.tight_layout()
plt.show()

# ============================================
# UNITS VS SALES
# ============================================

plt.figure(figsize=(8,5))
plt.scatter(df["Units"], df["Sales"])
plt.title("Units vs Sales")
plt.xlabel("Units")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

print("\n" + "="*70)
print("EDA COMPLETED SUCCESSFULLY")
print("="*70)