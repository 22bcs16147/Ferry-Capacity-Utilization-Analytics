import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/Toronto Island Ferry Tickets.csv")

# Convert Timestamp to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Display first five rows
print(df.head())

# Dataset shape
print("\nShape of Dataset:")
print(df.shape)

# Data types
print("\nData Types:")
print(df.dtypes)

# Date Range
print("\nDate Range:")
print("Start Date :", df["Timestamp"].min())
print("End Date   :", df["Timestamp"].max())

# Check for negative values
print("\nNegative Values:")

print("Negative Sales Count:",
      (df["Sales Count"] < 0).sum())

print("Negative Redemption Count:",
      (df["Redemption Count"] < 0).sum())

# Check descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Check minimum and maximum values
print("\nMinimum Values:")
print(df.min())

print("\nMaximum Values:")
print(df.max())