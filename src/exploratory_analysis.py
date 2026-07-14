import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Processed Dataset
# -----------------------------

df = pd.read_csv("data/processed/ferry_processed.csv")

# -----------------------------
# Dashboard Style
# -----------------------------

plt.style.use("ggplot")
sns.set_theme()

# -----------------------------
# Dataset Overview
# -----------------------------

print("="*60)
print("DATASET OVERVIEW")
print("="*60)

print(f"Total Records : {len(df)}")
print(f"Total Years   : {df['Year'].nunique()}")
print(f"Total Sales   : {df['Sales Count'].sum():,}")
print(f"Total Redemption : {df['Redemption Count'].sum():,}")

# -----------------------------
# Create Chart Folder
# -----------------------------

import os

os.makedirs("assets/charts", exist_ok=True)

# -----------------------------
# Yearly Activity
# -----------------------------

yearly = df.groupby("Year")["Total Activity Load"].sum()

plt.figure(figsize=(10,5))
yearly.plot(marker="o")

plt.title("Yearly Total Activity")
plt.xlabel("Year")
plt.ylabel("Activity")

plt.tight_layout()

plt.savefig("assets/charts/yearly_activity.png")

plt.show()

# -----------------------------
# Monthly Activity
# -----------------------------

monthly = df.groupby("Month Name")["Total Activity Load"].sum()

month_order = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]

monthly = monthly.reindex(month_order)

plt.figure(figsize=(12,5))

monthly.plot(kind="bar")

plt.title("Monthly Activity")

plt.ylabel("Activity")

plt.tight_layout()

plt.savefig("assets/charts/monthly_activity.png")

plt.show()

# -----------------------------
# Weekend vs Weekday
# -----------------------------

week = df.groupby("Weekend")["Total Activity Load"].sum()

plt.figure(figsize=(6,5))

week.plot(kind="bar")

plt.title("Weekend vs Weekday Activity")

plt.tight_layout()

plt.savefig("assets/charts/weekend_vs_weekday.png")

plt.show()

# -----------------------------
# Time Band
# -----------------------------

timeband = df.groupby("Time Band")["Total Activity Load"].sum()

plt.figure(figsize=(8,5))

timeband.plot(kind="bar")

plt.title("Activity by Time Band")

plt.tight_layout()

plt.savefig("assets/charts/time_band.png")

# plt.show()
plt.close()
print("\nEDA Completed Successfully")
print("Charts saved inside assets/charts/")