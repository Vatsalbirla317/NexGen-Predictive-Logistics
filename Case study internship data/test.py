import pandas as pd

# List all your CSVs
files = [
    "orders.csv",
    "delivery_performance.csv",
    "routes_distance.csv",
    "vehicle_fleet.csv",
    "warehouse_inventory.csv",
    "customer_feedback.csv",
    "cost_breakdown.csv"
]

for f in files:
    df = pd.read_csv(f)
    print(f"\n📄 {f} → Columns:")
    print(df.columns.tolist())
