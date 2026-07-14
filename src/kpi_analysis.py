import pandas as pd

# =====================================================
# Load Processed Dataset
# =====================================================

df = pd.read_csv("data/processed/ferry_processed.csv")

# =====================================================
# KPI Calculations
# =====================================================

# Total passenger activity
total_activity = df["Total Activity Load"].sum()

# Total ticket sales
total_sales = df["Sales Count"].sum()

# Total ticket redemptions
total_redemptions = df["Redemption Count"].sum()

# Average activity per 15-minute interval
average_activity = df["Total Activity Load"].mean()

# Capacity Utilization Ratio
capacity_utilization_ratio = (
    total_redemptions / total_sales
) * 100

# Idle Capacity Percentage
idle_capacity_percentage = (
    (df["Idle Capacity Indicator"] == "Idle").mean()
) * 100

# Congestion Threshold (Top 10% of activity)
congestion_threshold = df["Total Activity Load"].quantile(0.90)

# Congested Intervals
congested_intervals = (
    df["Total Activity Load"] >= congestion_threshold
).sum()

# Congestion Pressure Index
congestion_pressure_index = (
    congested_intervals / len(df)
) * 100

# Operational Variability Score
operational_variability_score = (
    df["Total Activity Load"].std()
)

# Peak Activity
peak_activity = df["Total Activity Load"].max()

# Average Operational Load Index
average_oli = df["Operational Load Index"].mean()

# =====================================================
# Display KPI Dashboard
# =====================================================

print("=" * 60)
print("FERRY OPERATIONAL KPI SUMMARY")
print("=" * 60)

print(f"Total Activity Load           : {total_activity:,.0f}")
print(f"Total Ticket Sales            : {total_sales:,.0f}")
print(f"Total Ticket Redemptions      : {total_redemptions:,.0f}")
print(f"Average Activity / Interval   : {average_activity:.2f}")

print("\nOperational KPIs")
print("-" * 60)

print(f"Capacity Utilization Ratio    : {capacity_utilization_ratio:.2f}%")
print(f"Idle Capacity Percentage      : {idle_capacity_percentage:.2f}%")
print(f"Congestion Pressure Index     : {congestion_pressure_index:.2f}%")
print(f"Operational Variability Score : {operational_variability_score:.2f}")
print(f"Peak Activity Load            : {peak_activity}")
print(f"Average Operational Load Index: {average_oli:.4f}")

print("=" * 60)
print("KPI Analysis Completed Successfully")