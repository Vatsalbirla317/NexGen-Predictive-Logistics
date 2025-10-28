import pandas as pd

def merge_datasets(orders, delivery, routes, fleet, warehouse, feedback, cost):
    print("🔹 Merging datasets...")

    # Step 1: Merge order-level data with delivery performance
    master = orders.merge(delivery, on="Order_ID", how="left")

    # Step 2: Merge with route-level metrics
    master = master.merge(routes, on="Order_ID", how="left")

    # Step 3: Merge with customer feedback
    master = master.merge(feedback, on="Order_ID", how="left")

    # Step 4: Merge with cost breakdown
    master = master.merge(cost, on="Order_ID", how="left")

    # Step 5: Map warehouse info — match 'Origin' with warehouse 'Location'
    master = master.merge(warehouse, left_on="Origin", right_on="Location", how="left")

    # Step 6: Add vehicle fleet — optional join (no direct key)
    # We'll assign vehicle info based on Current_Location matching Origin
    master = master.merge(fleet, left_on="Origin", right_on="Current_Location", how="left")

    print(f"✅ Merge completed. Final dataset shape: {master.shape}")
    return master


def main():
    print("🔹 Loading CSV files...")

    orders = pd.read_csv("orders.csv")
    delivery = pd.read_csv("delivery_performance.csv")
    routes = pd.read_csv("routes_distance.csv")
    fleet = pd.read_csv("vehicle_fleet.csv")
    warehouse = pd.read_csv("warehouse_inventory.csv")
    feedback = pd.read_csv("customer_feedback.csv")
    cost = pd.read_csv("cost_breakdown.csv")

    dfs = [orders, delivery, routes, fleet, warehouse, feedback, cost]

    # Merge all datasets
    master = merge_datasets(*dfs)

    # Save final dataset
    master.to_csv("merged_master_dataset.csv", index=False)
    print("💾 Saved merged file as 'merged_master_dataset.csv'.")


if __name__ == "__main__":
    main()
