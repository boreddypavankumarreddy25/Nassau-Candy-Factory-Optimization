import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import numpy as np

print("="*70)
print("NASSAU CANDY - MACHINE LEARNING")
print("="*70)

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_excel("Nassau_Candy_Cleaned.xlsx")

# ==========================================
# Encode Categorical Columns
# ==========================================

categorical_columns = [
    "Ship Mode",
    "Division",
    "Region",
    "Country/Region",
    "City",
    "State/Province",
    "Product Name"
]

encoders = {}

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

# ==========================================
# Feature Selection
# ==========================================

X = df[
[
"Ship Mode",
"Division",
"Region",
"Product Name",
"Sales",
"Units",
"Cost",
"Gross Profit",
"Profit Margin (%)"
]
]

y = df["Lead Time"]

# ==========================================
# Train Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ==========================================
# Models
# ==========================================

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),
    "Gradient Boosting": GradientBoostingRegressor(
        random_state=42
    )
}

best_model = None
best_r2 = -999

print("\nMODEL PERFORMANCE\n")

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    r2 = r2_score(y_test, predictions)

    print("="*50)
    print(name)
    print("="*50)

    print("MAE :", round(mae,2))
    print("RMSE:", round(rmse,2))
    print("R2  :", round(r2,4))

    if r2 > best_r2:
        best_r2 = r2
        best_model = model

# ==========================================
# Save Best Model
# ==========================================

joblib.dump(best_model,"best_model.pkl")

print("\nBest Model Saved Successfully!")

print("\nBest R² Score:", round(best_r2,4))