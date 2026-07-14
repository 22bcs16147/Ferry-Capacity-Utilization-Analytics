import pandas as pd


def calculate_kpis(df):
    """
    Calculate all dashboard KPIs.
    """

    total_sales = df["Sales Count"].sum()

    total_redemption = df["Redemption Count"].sum()

    total_activity = df["Total Activity Load"].sum()

    capacity_utilization = (
        (total_redemption / total_sales) * 100
        if total_sales > 0 else 0
    )

    idle_capacity = (
        (df["Idle Capacity Indicator"] == "Idle").mean() * 100
    )

    average_oli = df["Operational Load Index"].mean()

    peak_activity = df["Total Activity Load"].max()

    average_redemption_ratio = (
        df["Redemption Pressure Ratio"].mean()
    )

    return {
        "Total Sales": total_sales,
        "Total Redemption": total_redemption,
        "Total Activity": total_activity,
        "Capacity Utilization": capacity_utilization,
        "Idle Capacity": idle_capacity,
        "Average OLI": average_oli,
        "Peak Activity": peak_activity,
        "Average Redemption Ratio": average_redemption_ratio,
    }