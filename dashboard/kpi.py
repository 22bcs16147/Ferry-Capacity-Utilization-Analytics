print("KPI FILE LOADED:", __file__)
import streamlit as st

def show_kpis(df):
    total_sales = df["Sales Count"].sum()

    total_redemption = df["Redemption Count"].sum()

    total_activity = df["Total Activity Load"].sum()

    capacity_utilization = (
        (total_redemption / total_sales) * 100
        if total_sales > 0
        else 0
    )

    idle_capacity = (
        (df["Idle Capacity Indicator"] == "Idle").mean() * 100
    )

    average_oli = df["Operational Load Index"].mean()

    peak_activity = df["Total Activity Load"].max()

    average_redemption_ratio = (
        df["Redemption Pressure Ratio"].mean()
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🎫 Total Sales", f"{total_sales:,.0f}")

    c2.metric("🚢 Total Redemption", f"{total_redemption:,.0f}")

    c3.metric("📊 Total Activity", f"{total_activity:,.0f}")

    c4.metric(
        "⚙ Capacity Utilization",
        f"{capacity_utilization:.2f}%"
    )

    st.markdown("")

    c5, c6, c7, c8 = st.columns(4)

    c5.metric(
        "💤 Idle Capacity",
        f"{idle_capacity:.2f}%"
    )

    c6.metric(
        "📈 Avg Operational Load",
        f"{average_oli:.3f}"
    )

    c7.metric(
        "🔥 Peak Activity",
        f"{peak_activity:,.0f}"
    )

    c8.metric(
        "🎟 Avg Redemption Ratio",
        f"{average_redemption_ratio:.2f}"
    )