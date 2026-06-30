import pandas as pd

print("="*80)
print("NASSAU CANDY AI RECOMMENDATION ENGINE")
print("="*80)

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_excel("Nassau_Candy_Clustered.xlsx")

# =====================================================
# PRODUCT - FACTORY MAPPING
# =====================================================

factory_mapping = {
    "Wonka Bar - Nutty Crunch Surprise": "Lot's O' Nuts",
    "Wonka Bar - Fudge Mallows": "Lot's O' Nuts",
    "Wonka Bar -Scrumdiddlyumptious": "Lot's O' Nuts",
    "Wonka Bar - Milk Chocolate": "Wicked Choccy's",
    "Wonka Bar - Triple Dazzle Caramel": "Wicked Choccy's",
    "Laffy Taffy": "Sugar Shack",
    "SweeTARTS": "Sugar Shack",
    "Nerds": "Sugar Shack",
    "Fun Dip": "Sugar Shack",
    "Fizzy Lifting Drinks": "Sugar Shack",
    "Everlasting Gobstopper": "Secret Factory",
    "Lickable Wallpaper": "Secret Factory",
    "Wonka Gum": "Secret Factory",
    "Hair Toffee": "The Other Factory",
    "Kazookles": "The Other Factory"
}

df["Current Factory"] = df["Product Name"].map(factory_mapping)

# =====================================================
# PRODUCT SUMMARY
# =====================================================

summary = df.groupby("Product Name").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Gross Profit", "sum"),
    Average_Lead_Time=("Lead Time", "mean"),
    Average_Profit_Margin=("Profit Margin (%)", "mean"),
    Total_Units=("Units", "sum"),
    Total_Orders=("Order ID", "count"),
    Cluster=("Cluster", lambda x: x.mode()[0]),
    Current_Factory=("Current Factory", "first")
).reset_index()

# =====================================================
# RISK SCORE
# =====================================================

def risk_score(lead_time):
    if lead_time >= 1325:
        return "High"
    elif lead_time >= 1315:
        return "Medium"
    else:
        return "Low"

summary["Risk Score"] = summary["Average_Lead_Time"].apply(risk_score)

# =====================================================
# PRIORITY SCORE
# =====================================================

def priority(sales):
    if sales >= 25000:
        return "Critical"
    elif sales >= 10000:
        return "High"
    elif sales >= 3000:
        return "Medium"
    else:
        return "Low"

summary["Priority"] = summary["Total_Sales"].apply(priority)

# =====================================================
# NORMALIZED SCORES
# =====================================================

summary["Sales Score"] = (
    summary["Total_Sales"] /
    summary["Total_Sales"].max()
) * 100

summary["Profit Score"] = (
    summary["Total_Profit"] /
    summary["Total_Profit"].max()
) * 100

summary["Lead Score"] = (
    summary["Average_Lead_Time"] /
    summary["Average_Lead_Time"].max()
) * 100

summary["Unit Score"] = (
    summary["Total_Units"] /
    summary["Total_Units"].max()
) * 100

# =====================================================
# AI RECOMMENDATION SCORE
# =====================================================

summary["Recommendation Score"] = (

    summary["Sales Score"] * 0.35 +

    summary["Profit Score"] * 0.35 +

    summary["Unit Score"] * 0.20 +

    summary["Lead Score"] * 0.10

)

summary["Recommendation Score"] = summary["Recommendation Score"].round(2)

# =====================================================
# RECOMMENDATION LOGIC
# =====================================================

def recommendation(row):

    if row["Priority"] == "Critical" and row["Risk Score"] == "High":
        return "Reassign Immediately"

    elif row["Priority"] == "High":
        return "Consider Reassignment"

    elif row["Risk Score"] == "High":
        return "Optimize Shipping Route"

    else:
        return "Keep Current Factory"

summary["Recommendation"] = summary.apply(
    recommendation,
    axis=1
)

# =====================================================
# ALTERNATIVE FACTORY
# =====================================================

all_factories = [
    "Lot's O' Nuts",
    "Wicked Choccy's",
    "Sugar Shack",
    "Secret Factory",
    "The Other Factory"
]

recommended = []

for factory in summary["Current_Factory"]:

    choices = [f for f in all_factories if f != factory]

    recommended.append(choices[0])

summary["Recommended Factory"] = recommended

# =====================================================
# EXPECTED IMPROVEMENTS
# =====================================================

summary["Expected Lead Time Reduction (%)"] = (
    summary["Recommendation Score"] / 10
).round(1)

summary["Expected Profit Improvement (%)"] = (
    summary["Recommendation Score"] / 20
).round(1)

# =====================================================
# SORT RESULTS
# =====================================================

summary = summary.sort_values(
    by="Recommendation Score",
    ascending=False
)

# =====================================================
# DISPLAY RESULTS
# =====================================================

print("\nTOP AI RECOMMENDATIONS\n")

print(summary[[
    "Product Name",
    "Current_Factory",
    "Recommended Factory",
    "Recommendation Score",
    "Priority",
    "Risk Score",
    "Recommendation"
]])

# =====================================================
# SAVE FILE
# =====================================================

summary.to_excel(
    "AI_Factory_Recommendations.xlsx",
    index=False
)

print("\n" + "="*80)
print("AI RECOMMENDATION ENGINE COMPLETED")
print("="*80)

print("\nOutput File Saved:")
print("AI_Factory_Recommendations.xlsx")