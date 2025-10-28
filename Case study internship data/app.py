import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# --------------------------
# 1. PAGE CONFIG
# --------------------------
st.set_page_config(page_title="NexGen Predictive Delivery Optimizer", layout="wide")

# --------------------------
# 2. LOAD DATA
# --------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("merged_master_dataset.csv")
    # Clean column names
    df.columns = df.columns.str.strip()
    return df

df = load_data()
df.rename(columns={"Product_Category_x": "Product_Category"}, inplace=True)


st.title("🚚 NexGen Predictive Delivery Optimizer Dashboard")
st.markdown("Transforming logistics operations with **AI + Data-Driven Insights**")

# --------------------------
# 3. SIDEBAR FILTERS
# --------------------------
st.sidebar.header("🔍 Filters")

warehouse_filter = st.sidebar.multiselect(
    "Select Warehouse Location", options=df["Origin"].dropna().unique()
)

carrier_filter = st.sidebar.multiselect(
    "Select Carrier", options=df["Carrier"].dropna().unique()
)

priority_filter = st.sidebar.multiselect(
    "Select Delivery Priority", options=df["Priority"].dropna().unique()
)

if warehouse_filter:
    df = df[df["Origin"].isin(warehouse_filter)]
if carrier_filter:
    df = df[df["Carrier"].isin(carrier_filter)]
if priority_filter:
    df = df[df["Priority"].isin(priority_filter)]

# --------------------------
# 4. KPI METRICS
# --------------------------
st.subheader("📈 Key Metrics Overview")

col1, col2, col3, col4 = st.columns(4)

df["Delivery_Delay_Days"] = df["Actual_Delivery_Days"] - df["Promised_Delivery_Days"]
avg_delay = round(df["Delivery_Delay_Days"].mean(), 2)
on_time = round((df["Delivery_Delay_Days"] <= 0).mean() * 100, 2)
avg_cost = round(df["Delivery_Cost_INR"].mean(), 2)
avg_rating = round(df["Customer_Rating"].mean(), 2)

col1.metric("📦 Avg. Delivery Delay (Days)", avg_delay)
col2.metric("✅ On-time Delivery %", f"{on_time}%")
col3.metric("💰 Avg. Delivery Cost (INR)", avg_cost)
col4.metric("⭐ Avg. Customer Rating", avg_rating)

st.markdown("---")

# --------------------------
# 5. VISUALIZATIONS
# --------------------------
st.subheader("📊 Operational Insights")

# 1️⃣ Delay vs Priority
fig1 = px.box(df, x="Priority", y="Delivery_Delay_Days", color="Priority",
              title="Delivery Delay Distribution by Priority")
st.plotly_chart(fig1, use_container_width=True)

# 2️⃣ Actual vs Promised Days
fig2 = px.scatter(df, x="Promised_Delivery_Days", y="Actual_Delivery_Days",
                  color="Priority", trendline="ols",
                  title="Promised vs Actual Delivery Days")
st.plotly_chart(fig2, use_container_width=True)

# 3️⃣ Cost vs Distance
fig3 = px.scatter(df, x="Distance_KM", y="Delivery_Cost_INR",
                  color="Product_Category", size="Order_Value_INR",
                  title="Delivery Cost vs Distance")
st.plotly_chart(fig3, use_container_width=True)

# 4️⃣ Warehouse Performance
warehouse_perf = df.groupby("Origin").agg({
    "Delivery_Delay_Days": "mean",
    "Delivery_Cost_INR": "mean",
    "Customer_Rating": "mean"
}).reset_index()

fig4 = px.bar(warehouse_perf, x="Origin", y="Delivery_Delay_Days",
              color="Customer_Rating", title="Warehouse Performance (Delay vs Rating)",
              text_auto=".2f")
st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# --------------------------
# 6. MACHINE LEARNING: Predict Delay
# --------------------------
st.subheader("🤖 Predictive Model: Delivery Delay Prediction")

df_ml = df.dropna(subset=["Promised_Delivery_Days", "Actual_Delivery_Days", "Delivery_Cost_INR", "Distance_KM"])
df_ml["Is_Delayed"] = (df_ml["Actual_Delivery_Days"] > df_ml["Promised_Delivery_Days"]).astype(int)

features = ["Promised_Delivery_Days", "Delivery_Cost_INR", "Distance_KM", "Fuel_Consumption_L", "Traffic_Delay_Minutes"]
X = df_ml[features].fillna(0)
y = df_ml["Is_Delayed"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
st.write(f"✅ **Model Accuracy:** {acc*100:.2f}%")

# Feature importance chart
feat_imp = pd.DataFrame({"Feature": features, "Importance": model.feature_importances_}).sort_values(by="Importance", ascending=False)
fig5 = px.bar(feat_imp, x="Importance", y="Feature", orientation="h", title="Feature Importance")
st.plotly_chart(fig5, use_container_width=True)

# --------------------------
# 7. DOWNLOAD FILTERED DATA
# --------------------------
st.markdown("### 📥 Export Filtered Data")
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("Download Current View (CSV)", csv, "filtered_data.csv", "text/csv")

st.markdown("---")
st.markdown("Developed by **Vatsal Birla** 🚀 | NexGen Logistics Innovation Challenge")

