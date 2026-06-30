import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

# ============================================
# LOAD DATA
# ============================================

df = pd.read_excel("Nassau_Candy_Cleaned.xlsx")

print("="*60)
print("PREPROCESSING STARTED")
print("="*60)

# ============================================
# ENCODE CATEGORICAL COLUMNS
# ============================================

label_encoders = {}

categorical_columns = [
    "Ship Mode",
    "Division",
    "Region",
    "Country/Region",
    "City",
    "State/Province",
    "Product Name"
]

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    label_encoders[col] = le

print("\nCategorical Encoding Completed")

# ============================================
# SELECT FEATURES
# ============================================

features = [
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

X = df[features]

# Target Variable
y = df["Lead Time"]

print("\nFeature Matrix Shape:", X.shape)
print("Target Shape:", y.shape)

# ============================================
# TRAIN TEST SPLIT
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ============================================
# FEATURE SCALING
# ============================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nFeature Scaling Completed")

# ============================================
# SAVE FILES
# ============================================

joblib.dump(scaler, "scaler.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")

print("\nScaler Saved")
print("Label Encoders Saved")

print("\nPreprocessing Completed Successfully")