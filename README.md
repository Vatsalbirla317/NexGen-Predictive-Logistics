# 🚚 NexGen Predictive Logistics Dashboard

### Transforming logistics operations with AI + Data-Driven Insights

This project is part of the **NexGen Logistics Innovation Challenge**.  
It leverages **data analytics and machine learning** to analyze logistics data, optimize delivery efficiency, and predict potential delays — empowering smarter decision-making for supply chain operations.

---

## 📊 Features

✅ **Interactive Streamlit Dashboard** – built with Python  
✅ **Multi-dataset Integration** – merges order, delivery, route, warehouse, and cost data  
✅ **Dynamic Filters** – by warehouse, carrier, and delivery priority  
✅ **Predictive Model** – AI model predicts delivery delays  
✅ **Business KPIs** – on-time performance, cost metrics, and customer satisfaction  
✅ **Interactive Visuals** – 4+ interactive charts using Plotly  
✅ **Data Export** – download filtered data as CSV  

---

## 🧠 Key Insights Displayed

- Average Delivery Delay (Days)  
- On-Time Delivery %  
- Average Delivery Cost (INR)  
- Customer Rating Trends  
- Cost vs Distance Relationship  
- Warehouse Performance  
- Feature Importance for Delivery Delay  

---

## 🧩 Tech Stack

- **Python 3.12+**
- **Streamlit** – Dashboard UI  
- **Pandas / NumPy** – Data processing and manipulation  
- **Plotly Express** – Interactive charts  
- **Scikit-learn** – Machine Learning (Random Forest)  
- **Statsmodels** – Regression and trendline analysis  

---

## 📁 Project Structure

📂 NexGen Predictive Logistics Dashboard/
│
├── app.py # Main Streamlit dashboard
├── merge_datasets.py # Script to combine all CSV files
├── merged_master_dataset.csv # Final dataset (auto-generated)
│
├── orders.csv
├── delivery_performance.csv
├── routes_distance.csv
├── vehicle_fleet.csv
├── warehouse_inventory.csv
├── customer_feedback.csv
├── cost_breakdown.csv
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/nexgen-logistics-dashboard.git
cd nexgen-logistics-dashboard
2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Merge datasets (if not already merged)
python merge_datasets.py

4️⃣ Run the Streamlit dashboard
streamlit run app.py

5️⃣ Open in browser

Local URL → http://localhost:8501

🧮 Predictive Model: Delivery Delay Prediction

The app includes a Random Forest Classifier trained to predict if a delivery will be delayed or on-time using:

Promised Delivery Days

Actual Delivery Days

Distance (KM)

Delivery Cost (INR)

Fuel Consumption

Traffic Delay Minutes

Model Metrics:

Accuracy displayed in dashboard

Feature importance visualized via bar chart

📈 Sample Visualizations

Delivery Delay Distribution by Priority

Promised vs Actual Delivery Days (Trendline)

Delivery Cost vs Distance (Bubble Chart)

Warehouse Performance (Delay vs Rating)

Feature Importance (ML Insights)

💡 Challenges & Learnings

During development, several challenges were encountered and solved:

🧩 1. Merging Multi-Source Data

Challenge: Each dataset had different key columns and inconsistent formats.

Solution: Created a clean merge_datasets.py pipeline to merge on Order_ID, Origin, and Location while handling missing values and duplicates.

📉 2. Handling Missing & Skewed Data

Challenge: Some datasets had missing delivery times or cost data.

Solution: Used imputation, type correction, and filtered invalid records before analysis.

🧠 3. Model Feature Selection

Challenge: Many overlapping numeric features led to overfitting.

Solution: Selected the top 5 business-relevant features based on correlation and feature importance.

🖥️ 4. Streamlit Performance Optimization

Challenge: Large CSV merges caused long load times.

Solution: Used @st.cache_data for efficient caching and faster reruns.

🎨 5. Visual Design & Interactivity

Challenge: Presenting data in a clean, meaningful way.

Solution: Used Plotly for dynamic interactivity, color-based grouping, and responsive layout.

💡 6. Realistic Business Insights

Learned how logistics metrics (delay, cost, distance) interact in real-world scenarios.

Designed the dashboard to simulate how operations managers would track KPIs and predict delivery issues.

🚀 Future Enhancements

Integrate live data API for real-time tracking

Add cost optimization models

Include CO₂ emission analytics per route

Build alert system for delay predictions

👨‍💻 Developed By

Vatsal Birla
