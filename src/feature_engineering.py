import pandas as pd

# =====================================================
# Load Dataset
# =====================================================

df = pd.read_csv("data/raw/Toronto Island Ferry Tickets.csv")

# =====================================================
# Convert Timestamp to Datetime
# =====================================================

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# =====================================================
# Create Date & Time Features
# =====================================================

df["Year"] = df["Timestamp"].dt.year
df["Quarter"] = df["Timestamp"].dt.quarter
df["Month"] = df["Timestamp"].dt.month
df["Month Name"] = df["Timestamp"].dt.month_name()

df["Day"] = df["Timestamp"].dt.day
df["Day Name"] = df["Timestamp"].dt.day_name()

df["Hour"] = df["Timestamp"].dt.hour
df["Minute"] = df["Timestamp"].dt.minute

# =====================================================
# Weekday / Weekend
# =====================================================

weekend_days = ["Saturday", "Sunday"]

df["Weekend"] = df["Day Name"].apply(
    lambda day: "Weekend" if day in weekend_days else "Weekday"
)

# =====================================================
# Create Season Column
# =====================================================

def get_season(month):

    if month in [12, 1, 2]:
        return "Winter"

    elif month in [3, 4, 5]:
        return "Spring"

    elif month in [6, 7, 8]:
        return "Summer"

    else:
        return "Autumn"


df["Season"] = df["Month"].apply(get_season)

# =====================================================
# Create Time Band
# =====================================================

def get_time_band(hour):

    if 5 <= hour < 12:
        return "Morning"

    elif 12 <= hour < 17:
        return "Afternoon"

    elif 17 <= hour < 21:
        return "Evening"

    else:
        return "Night"


df["Time Band"] = df["Hour"].apply(get_time_band)

# =====================================================
# Business Features
# =====================================================

# Total passenger activity during each interval
df["Total Activity Load"] = (
    df["Sales Count"] + df["Redemption Count"]
)

# Ratio of redeemed tickets to sold tickets
df["Redemption Pressure Ratio"] = (
    df["Redemption Count"] / (df["Sales Count"] + 1)
)

# Normalize activity between 0 and 1
maximum_activity = df["Total Activity Load"].max()

df["Operational Load Index"] = (
    df["Total Activity Load"] / maximum_activity
)

# Identify low activity intervals
idle_threshold = 20

df["Idle Capacity Indicator"] = df["Total Activity Load"].apply(
    lambda value: "Idle" if value < idle_threshold else "Active"
)

# =====================================================
# Display Information
# =====================================================

print("\nFeature Engineering Completed Successfully")

print("\nDataset Shape:")
print(df.shape)

print("\nNew Columns Added:")

new_columns = [
    "Year",
    "Quarter",
    "Month",
    "Month Name",
    "Day",
    "Day Name",
    "Hour",
    "Minute",
    "Weekend",
    "Season",
    "Time Band",
    "Total Activity Load",
    "Redemption Pressure Ratio",
    "Operational Load Index",
    "Idle Capacity Indicator"
]

for column in new_columns:
    print(column)

print("\nPreview of Dataset:")
print(df.head())

# =====================================================
# Save Processed Dataset
# =====================================================

output_path = "data/processed/ferry_processed.csv"

df.to_csv(output_path, index=False)

print("\nProcessed dataset saved successfully.")
print(f"File Location: {output_path}")