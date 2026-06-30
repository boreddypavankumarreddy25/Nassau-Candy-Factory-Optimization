import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Nassau Candy Factory Optimization",
    page_icon="🍬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main{
    background-color:#f8f9fa;
}

[data-testid="stSidebar"]{
    background-color:#1f2937;
}

[data-testid="stSidebar"] *{
    color:white;
}

.kpi{
    background:white;
    padding:20px;
    border-radius:10px;
    box-shadow:0px 0px 8px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():

    df = pd.read_excel("Nassau_Candy_Clustered.xlsx")
    rec = pd.read_excel("AI_Factory_Recommendations.xlsx")

    return df, rec


df, rec = load_data()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🍬 Nassau Candy")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📊 Sales Analytics",
        "🤖 Machine Learning",
        "📈 Route Clustering",
        "🏭 Factory Optimization",
        "📋 AI Recommendations"
    ]
)

st.sidebar.markdown("---")

region = st.sidebar.multiselect(
    "Region",
    sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

division = st.sidebar.multiselect(
    "Division",
    sorted(df["Division"].unique()),
    default=sorted(df["Division"].unique())
)

ship_mode = st.sidebar.multiselect(
    "Ship Mode",
    sorted(df["Ship Mode"].unique()),
    default=sorted(df["Ship Mode"].unique())
)

# =====================================================
# FILTER DATA
# =====================================================

filtered = df[
    (df["Region"].isin(region)) &
    (df["Division"].isin(division)) &
    (df["Ship Mode"].isin(ship_mode))
]

# =====================================================
# DASHBOARD
# =====================================================

if page == "🏠 Dashboard":

    st.title("🍬 Nassau Candy Factory Optimization Dashboard")

    st.markdown("### Executive Overview")

    k1, k2, k3, k4, k5 = st.columns(5)

    k1.metric(
        "Total Sales",
        f"${filtered['Sales'].sum():,.2f}"
    )

    k2.metric(
        "Gross Profit",
        f"${filtered['Gross Profit'].sum():,.2f}"
    )

    k3.metric(
        "Orders",
        filtered["Order ID"].nunique()
    )

    k4.metric(
        "Customers",
        filtered["Customer ID"].nunique()
    )

    k5.metric(
        "Avg Lead Time",
        round(filtered["Lead Time"].mean(),2)
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        sales_region = (
            filtered.groupby("Region")["Sales"]
            .sum()
            .reset_index()
        )

        fig =px.bar(
            sales_region,
            x="Region",
            y="Sales",
            color="Region",
            text_auto=".2s",
            title="Sales by Region"
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        sales_division = (
            filtered.groupby("Division")["Sales"]
            .sum()
            .reset_index()
        )

        fig = px.pie(
            sales_division,
            names="Division",
            values="Sales",
            hole=0.45,
            title="Sales by Division"
        )

        fig.update_layout(height=420)

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:

        ship = (
            filtered["Ship Mode"]
            .value_counts()
            .reset_index()
        )

        ship.columns = ["Ship Mode", "Orders"]

        fig = px.bar(
            ship,
            x="Ship Mode",
            y="Orders",
            color="Ship Mode",
            text="Orders",
            title="Ship Mode Distribution"
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(fig, use_container_width=True)

    with col4:

        top_products = (
            filtered.groupby("Product Name")["Sales"]
            .sum()
            .nlargest(10)
            .reset_index()
        )

        fig = px.bar(
            top_products,
            x="Product Name",
            y="Sales",
            color="Sales",
            text_auto=".2s",
            title="Top 10 Products by Sales"
        )

        fig.update_layout(
            xaxis_tickangle=-35,
            template="plotly_white",
            height=420
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    col5, col6 = st.columns(2)

    with col5:

        lead = (
            filtered.groupby("Region")["Lead Time"]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            lead,
            x="Region",
            y="Lead Time",
            color="Region",
            text_auto=".1f",
            title="Average Lead Time by Region"
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(fig, use_container_width=True)

    with col6:

        profit = (
            filtered.groupby("Division")["Gross Profit"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            profit,
            x="Division",
            y="Gross Profit",
            color="Division",
            text_auto=".2s",
            title="Gross Profit by Division"
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(fig, use_container_width=True)

 # =====================================================
# SALES ANALYTICS
# =====================================================

elif page == "📊 Sales Analytics":

    st.title("📊 Sales Analytics Dashboard")

    st.markdown("### Sales Performance Analysis")

    # ==========================
    # KPIs
    # ==========================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Sales",
        f"${filtered['Sales'].sum():,.2f}"
    )

    c2.metric(
        "Total Profit",
        f"${filtered['Gross Profit'].sum():,.2f}"
    )

    c3.metric(
        "Average Sales",
        f"${filtered['Sales'].mean():,.2f}"
    )

    c4.metric(
        "Average Lead Time",
        f"{filtered['Lead Time'].mean():.2f} Days"
    )

    st.markdown("---")

    # ==========================
    # Sales Trend
    # ==========================

    sales_trend = (
        filtered.groupby("Order Date")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        sales_trend,
        x="Order Date",
        y="Sales",
        markers=True,
        title="Sales Trend Over Time"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ==========================
    # Region vs Profit
    # ==========================

    col1, col2 = st.columns(2)

    with col1:

        region_sales = (
            filtered.groupby("Region")["Gross Profit"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            region_sales,
            x="Region",
            y="Gross Profit",
            color="Region",
            text_auto=".2s",
            title="Gross Profit by Region"
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        division_sales = (
            filtered.groupby("Division")["Sales"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            division_sales,
            x="Division",
            y="Sales",
            color="Division",
            text_auto=".2s",
            title="Sales by Division"
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ==========================
    # Product Performance
    # ==========================

    product_sales = (
        filtered.groupby("Product Name")[["Sales", "Gross Profit"]]
        .sum()
        .sort_values("Sales", ascending=False)
        .reset_index()
    )

    fig = px.scatter(
        product_sales,
        x="Sales",
        y="Gross Profit",
        size="Sales",
        color="Gross Profit",
        hover_name="Product Name",
        title="Product Performance Analysis"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ==========================
    # Top Products Table
    # ==========================

    st.subheader("Top Performing Products")

    st.dataframe(
        product_sales.head(15),
        use_container_width=True
    )

    csv = product_sales.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Sales Report",
        csv,
        "Sales_Analytics.csv",
        "text/csv"
    )
    # =====================================================
# MACHINE LEARNING
# =====================================================

elif page == "🤖 Machine Learning":

    st.title("🤖 Machine Learning Dashboard")

    st.markdown("### Predictive Model Performance")

    # =====================================================
    # MODEL RESULTS
    # =====================================================

    model_results = pd.DataFrame({

        "Model": [
            "Linear Regression",
            "Random Forest",
            "Gradient Boosting"
        ],

        "MAE": [
            214.96,
            224.98,
            216.14
        ],

        "RMSE": [
            266.07,
            277.25,
            267.90
        ],

        "R² Score": [
            -0.001,
            -0.087,
            -0.015
        ]

    })

    st.dataframe(model_results, use_container_width=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        fig = px.bar(
            model_results,
            x="Model",
            y="RMSE",
            color="Model",
            text="RMSE",
            title="RMSE Comparison"
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.bar(
            model_results,
            x="Model",
            y="MAE",
            color="Model",
            text="MAE",
            title="MAE Comparison"
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    fig = px.bar(
        model_results,
        x="Model",
        y="R² Score",
        color="Model",
        text="R² Score",
        title="R² Score Comparison"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.subheader("📌 Model Evaluation Summary")

    best_model = model_results.loc[
        model_results["RMSE"].idxmin()
    ]

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Best Model",
        best_model["Model"]
    )

    col2.metric(
        "Lowest RMSE",
        f"{best_model['RMSE']:.2f}"
    )

    col3.metric(
        "Lowest MAE",
        f"{best_model['MAE']:.2f}"
    )

    st.markdown("---")

    st.subheader("📈 Model Performance Comparison")

    fig = px.scatter(
        model_results,
        x="RMSE",
        y="MAE",
        size="RMSE",
        color="Model",
        hover_name="Model",
        text="Model"
    )

    fig.update_traces(textposition="top center")

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.info("""
### Interpretation

The predictive models were trained using the available academic dataset.

The current dataset does not contain logistics variables such as:

• Factory Capacity

• Transportation Distance

• Warehouse Location

• Carrier Performance

• Traffic Conditions

• Inventory Levels

Because these variables strongly influence shipping lead time, the models show low predictive performance (low R² scores).

This dashboard is intended to demonstrate the complete machine learning workflow, including preprocessing, model training, evaluation, and comparison, rather than to provide production-ready forecasts.
""")


    # =====================================================
# ROUTE CLUSTERING
# =====================================================

elif page == "📈 Route Clustering":

    st.title("📈 Route Clustering Dashboard")

    st.markdown("### Route Performance Segmentation")

    # =====================================================
    # KPIs
    # =====================================================

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Total Clusters",
        filtered["Cluster"].nunique()
    )

    c2.metric(
        "Total Orders",
        len(filtered)
    )

    c3.metric(
        "Average Lead Time",
        f"{filtered['Lead Time'].mean():.2f} Days"
    )

    st.markdown("---")

    # =====================================================
    # Cluster Distribution
    # =====================================================

    cluster_count = (
        filtered["Cluster"]
        .value_counts()
        .reset_index()
    )

    cluster_count.columns = ["Cluster", "Orders"]

    col1, col2 = st.columns(2)

    with col1:

        fig = px.pie(
            cluster_count,
            names="Cluster",
            values="Orders",
            hole=0.45,
            title="Cluster Distribution"
        )

        fig.update_layout(height=420)

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.bar(
            cluster_count,
            x="Cluster",
            y="Orders",
            color="Cluster",
            text="Orders",
            title="Orders per Cluster"
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # =====================================================
    # Scatter Plot
    # =====================================================

    fig = px.scatter(
        filtered,
        x="Sales",
        y="Gross Profit",
        color=filtered["Cluster"].astype(str),
        size="Units",
        hover_name="Product Name",
        title="Cluster Analysis (Sales vs Gross Profit)"
    )

    fig.update_layout(
        template="plotly_white",
        height=550
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # =====================================================
    # Lead Time by Cluster
    # =====================================================

    lead_cluster = (
        filtered.groupby("Cluster")["Lead Time"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        lead_cluster,
        x="Cluster",
        y="Lead Time",
        color="Cluster",
        text_auto=".2f",
        title="Average Lead Time by Cluster"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # =====================================================
    # Cluster Summary
    # =====================================================

    st.subheader("Cluster Summary")

    summary = (
        filtered.groupby("Cluster")[
            [
                "Sales",
                "Gross Profit",
                "Lead Time",
                "Units"
            ]
        ]
        .mean()
        .round(2)
    )

    st.dataframe(summary, use_container_width=True)

    st.markdown("---")

    # =====================================================
    # Business Insights
    # =====================================================

    st.subheader("Business Insights")

    highest_sales = summary["Sales"].idxmax()
    highest_profit = summary["Gross Profit"].idxmax()
    lowest_lead = summary["Lead Time"].idxmin()

    st.success(f"""
✅ Cluster **{highest_sales}** generates the highest average sales.

💰 Cluster **{highest_profit}** delivers the highest average gross profit.

🚚 Cluster **{lowest_lead}** has the lowest average lead time.

These insights help identify high-performing routes and prioritize operational improvements.
""")

    # =====================================================
# FACTORY OPTIMIZATION SIMULATOR
# =====================================================

elif page == "🏭 Factory Optimization":

    st.title("🏭 Factory Optimization Simulator")

    st.markdown(
        """
Select a product to compare its current factory with the AI recommended factory.
The recommendation is generated based on operational score, risk level,
and optimization priority.
"""
    )

    st.markdown("---")

    # Product Selection

    product = st.selectbox(
        "Select Product",
        sorted(rec["Product Name"].unique())
    )

    result = rec[rec["Product Name"] == product].iloc[0]

    st.markdown("---")

    # KPI Cards

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Current Factory",
        result["Current_Factory"]
    )

    c2.metric(
        "Recommended Factory",
        result["Recommended Factory"]
    )

    c3.metric(
        "Priority",
        result["Priority"]
    )

    c4.metric(
        "Risk Score",
        result["Risk Score"]
    )

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Recommendation Score",
            round(float(result["Recommendation Score"]), 2)
        )

    with c2:

        st.metric(
            "Recommendation",
            result["Recommendation"]
        )

    st.markdown("---")

    # Recommendation Details

    st.subheader("Recommendation Details")

    details = pd.DataFrame({

        "Parameter": [

            "Product",

            "Current Factory",

            "Recommended Factory",

            "Recommendation Score",

            "Priority",

            "Risk Score",

            "Recommendation"

        ],

        "Value": [

            result["Product Name"],

            result["Current_Factory"],

            result["Recommended Factory"],

            round(float(result["Recommendation Score"]),2),

            result["Priority"],

            result["Risk Score"],

            result["Recommendation"]

        ]

    })

    st.dataframe(
        details,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # Gauge Progress

    score = float(result["Recommendation Score"])

    st.subheader("Optimization Score")

    st.progress(min(score / 100, 1.0))

    st.write(f"Optimization Score : **{score:.2f}/100**")

    st.markdown("---")

    # Business Decision

    st.subheader("AI Decision")

    recommendation = result["Recommendation"]

    if recommendation == "Reassign Immediately":

        st.error(
            """
Current factory assignment is inefficient.

AI strongly recommends moving production to the suggested factory
to improve logistics efficiency.
"""
        )

    elif recommendation == "Consider Reassignment":

        st.warning(
            """
Current assignment is acceptable but can be improved.

Management should evaluate reassignment after cost analysis.
"""
        )

    elif recommendation == "Optimize Shipping Route":

        st.info(
            """
Factory reassignment is not mandatory.

Improving transportation routes may provide better efficiency.
"""
        )

    else:

        st.success(
            """
Current factory assignment is already efficient.

No immediate action is required.
"""
        )

    st.markdown("---")

    st.subheader("Recommendation Record")

    st.dataframe(
        rec,
        use_container_width=True
    )

# =====================================================
# AI RECOMMENDATIONS
# =====================================================

# =====================================================
# AI RECOMMENDATIONS DASHBOARD
# =====================================================

else:

    st.title("🤖 AI Recommendation Dashboard")

    st.markdown(
        """
This dashboard summarizes all AI-generated factory reassignment
recommendations and allows decision makers to download the results.
"""
    )

    st.markdown("---")

    # =====================================================
    # KPI CARDS
    # =====================================================

    total_products = rec["Product Name"].nunique()
    total_recommendations = len(rec)

    critical = (rec["Priority"] == "Critical").sum()
    high = (rec["Priority"] == "High").sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Products",
        total_products
    )

    c2.metric(
        "Recommendations",
        total_recommendations
    )

    c3.metric(
        "Critical Priority",
        critical
    )

    c4.metric(
        "High Priority",
        high
    )

    st.markdown("---")

    # =====================================================
    # PRIORITY CHART
    # =====================================================

    priority = rec["Priority"].value_counts().reset_index()
    priority.columns = ["Priority", "Count"]

    fig = px.bar(
        priority,
        x="Priority",
        y="Count",
        color="Priority",
        text="Count",
        title="Recommendation Priority Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    # =====================================================
    # RISK CHART
    # =====================================================

    risk = rec["Risk Score"].value_counts().reset_index()
    risk.columns = ["Risk Score", "Count"]

    fig = px.pie(
        risk,
        names="Risk Score",
        values="Count",
        hole=0.45,
        title="Risk Score Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # =====================================================
    # FACTORY COMPARISON
    # =====================================================

    st.subheader("Current vs Recommended Factory")

    compare = rec[[
        "Product Name",
        "Current_Factory",
        "Recommended Factory"
    ]]

    st.dataframe(
        compare,
        use_container_width=True
    )

    st.markdown("---")

    # =====================================================
    # COMPLETE RECOMMENDATIONS
    # =====================================================

    st.subheader("Complete AI Recommendation Table")

    st.dataframe(
        rec,
        use_container_width=True
    )

    st.markdown("---")

    # =====================================================
    # DOWNLOAD BUTTONS
    # =====================================================

    csv = rec.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download CSV",
        data=csv,
        file_name="AI_Factory_Recommendations.csv",
        mime="text/csv"
    )

    excel = pd.ExcelWriter("Recommendations.xlsx", engine="openpyxl")
    rec.to_excel(excel, index=False)
    excel.close()

    with open("Recommendations.xlsx", "rb") as file:

        st.download_button(
            label="⬇ Download Excel",
            data=file,
            file_name="Recommendations.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    st.markdown("---")

    # =====================================================
    # EXECUTIVE SUMMARY
    # =====================================================

    st.success(
        """
### Executive Summary

• AI analyzed every product assignment.

• Products with **Critical** priority should be reviewed immediately.

• Medium and Low priority products can continue under current assignments.

• This recommendation engine helps reduce operational costs,
improve shipping efficiency, and support strategic factory allocation.

• The dashboard provides data-driven decision support for management.
"""
    )