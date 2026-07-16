import streamlit as st


def show_insights(df):
    """
    Display business insights based on filtered ferry data.
    """

    st.subheader("📊 Executive Insights")

    if df.empty:
        st.warning("No data available for the selected filters.")
        return

    # -----------------------------
    # Highest Activity Year
    # -----------------------------

    yearly = (
        df.groupby("Year")["Total Activity Load"]
        .sum()
        .sort_values(ascending=False)
    )

    best_year = yearly.index[0]
    best_year_value = yearly.iloc[0]

    # -----------------------------
    # Busiest Month
    # -----------------------------

    monthly = (
        df.groupby("Month Name")["Total Activity Load"]
        .sum()
        .sort_values(ascending=False)
    )

    busiest_month = monthly.index[0]

    # -----------------------------
    # Peak Hour
    # -----------------------------

    hourly = (
        df.groupby("Hour")["Total Activity Load"]
        .sum()
        .sort_values(ascending=False)
    )

    peak_hour = hourly.index[0]

    # -----------------------------
    # Idle Capacity
    # -----------------------------

    idle_percentage = (
        (df["Idle Capacity Indicator"] == "Idle")
        .mean()
        * 100
    )

    # -----------------------------
    # Capacity Utilization
    # -----------------------------

    total_sales = df["Sales Count"].sum()
    total_redemption = df["Redemption Count"].sum()

    if total_sales > 0:
        capacity = (total_redemption / total_sales) * 100
    else:
        capacity = 0

    # -----------------------------
    # Average Operational Load
    # -----------------------------

    avg_load = df["Operational Load Index"].mean()

    # ==================================================
    # Display Insights
    # ==================================================

    st.success(
        f"📈 Highest operational activity was observed in **{best_year}**, "
        f"with **{best_year_value:,.0f}** passenger activities."
    )

    st.info(
        f"📅 **{busiest_month}** recorded the highest passenger activity."
    )

    st.info(
        f"🕒 Peak passenger movement generally occurred around **{peak_hour}:00**."
    )

    if idle_percentage > 40:
        st.warning(
            f"💤 Idle Capacity is **{idle_percentage:.2f}%**. "
            "Large portions of ferry operations remain under-utilized."
        )
    else:
        st.success(
            f"✅ Idle Capacity remains at **{idle_percentage:.2f}%**, "
            "indicating efficient utilization."
        )

    if capacity > 95:
        st.error(
            "🚨 Capacity utilization is extremely high. "
            "Additional ferry deployment should be considered."
        )

    elif capacity > 80:
        st.warning(
            "⚠ Ferry operations are approaching maximum capacity."
        )

    else:
        st.success(
            "✅ Ferry capacity utilization is within acceptable limits."
        )

    st.markdown("---")

    st.subheader("💡 Business Recommendations")

    recommendations = []

    if idle_percentage > 40:
        recommendations.append(
            "Reduce ferry frequency during prolonged idle periods to optimize operating costs."
        )

    if capacity > 90:
        recommendations.append(
            "Increase ferry frequency during peak operating hours."
        )

    recommendations.append(
        "Continue monitoring seasonal demand for future scheduling improvements."
    )

    recommendations.append(
        "Use Operational Load Index to identify congestion-prone intervals."
    )

    recommendations.append(
        "Review ticket redemption behaviour for better resource allocation."
    )

    for rec in recommendations:
        st.write("✔", rec)