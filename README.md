# 🍬 Nassau Candy Factory Optimization using AI & Machine Learning

## 📌 Project Overview

This project develops an AI-based Factory Optimization System for Nassau Candy Distributor.

The objective is to optimize factory-product assignments by predicting shipping performance, analyzing business data, clustering routes, and generating AI-based factory recommendations. The project includes a Streamlit dashboard for interactive visualization and decision support.

---

## 🎯 Objectives

- Predict shipping lead time
- Analyze sales and profit performance
- Cluster routes based on operational characteristics
- Recommend optimal factory assignments
- Compare current vs recommended factories
- Visualize business KPIs using Streamlit

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Streamlit
- OpenPyXL
- Joblib

---

## 📂 Project Structure

```
Nassau-Candy-Factory-Optimization/
│
├── Dataset/
│   ├── Nassau_Candy.xlsx
│   ├── Nassau_Candy_Cleaned.xlsx
│   └── Nassau_Candy_Clustered.xlsx
│
├── Models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   └── label_encoders.pkl
│
├── Output/
│   ├── AI_Factory_Recommendations.xlsx
│   └── Business_KPIs.xlsx
│
├── 01_data_cleaning.py
├── 02_feature_engineering.py
├── 03_eda.py
├── 04_preprocessing.py
├── 05_machine_learning.py
├── 06_clustering.py
├── 07_factory_optimization.py
├── 08_ai_recommendation.py
├── 09_kpi_analysis.py
├── app.py
├── requirements.txt
└── README.md
```

---

## 📊 Features

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Machine Learning Models
  - Linear Regression
  - Random Forest
  - Gradient Boosting
- Route Clustering (K-Means)
- Factory Optimization Engine
- AI Recommendation Engine
- Business KPI Dashboard
- Interactive Streamlit Dashboard

---

## 📈 Dashboard Modules

- 🏠 Dashboard
- 📊 Sales Analytics
- 🤖 Machine Learning Performance
- 📈 Route Clustering
- 🏭 Factory Optimization
- 📋 AI Recommendations

---

## 📊 Key Performance Indicators

- Total Sales
- Gross Profit
- Average Lead Time
- Profit Margin
- Sales by Region
- Sales by Division
- Top Selling Products
- Ship Mode Distribution

---

## 🤖 Machine Learning

Models evaluated:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

Evaluation Metrics:

- MAE
- RMSE
- R² Score

---

## 🏭 Factory Optimization

The optimization engine recommends the best factory for each product by considering:

- Lead Time
- Profit Impact
- Risk Score
- Recommendation Score
- Business Priority

---

## ▶️ How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py




## 📌 Future Enhancements

- Real-time logistics data integration
- Distance-based optimization
- Transportation cost prediction
- Inventory optimization
- Cloud deployment
- Advanced AI optimization models

---

## 👩‍💻 Author

**Boreddy pavan kumar reddy**

