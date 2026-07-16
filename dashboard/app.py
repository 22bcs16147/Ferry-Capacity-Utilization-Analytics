import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="Ferry Capacity Utilization Dashboard",
    page_icon="⛴️",
    layout="wide"
)

# -----------------------------------------------------
# Load Dataset
# -----------------------------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/ferry_processed.csv")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    return df

df = load_data()

# -----------------------------------------------------
# Dashboard Title
# -----------------------------------------------------

st.title("⛴️ Ferry Capacity Utilization & Operational Efficiency Dashboard")

st.markdown("""
This dashboard analyzes Toronto Island Ferry ticket activity
to identify operational efficiency, congestion patterns,
capacity utilization and idle periods.
""")

# -----------------------------------------------------
# Sidebar Filters
# -----------------------------------------------------

st.sidebar.header("Dashboard Filters")

min_date = df["Timestamp"].min().date()
max_date = df["Timestamp"].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date]
)

years = sorted(df["Year"].unique())

selected_year = st.sidebar.multiselect(
    "Select Year",
    years,
    default=years
)

month_order = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]

selected_month = st.sidebar.multiselect(
    "Select Month",
    month_order,
    default=month_order
)

season_order = ["Winter","Spring","Summer","Autumn"]

selected_season = st.sidebar.multiselect(
    "Select Season",
    season_order,
    default=season_order
)

timeband_order = [
    "Morning",
    "Afternoon",
    "Evening",
    "Night"
]

selected_timeband = st.sidebar.multiselect(
    "Select Time Band",
    timeband_order,
    default=timeband_order
)

selected_week = st.sidebar.multiselect(
    "Week Type",
    ["Weekday","Weekend"],
    default=["Weekday","Weekend"]
)

# -----------------------------------------------------
# Apply Filters
# -----------------------------------------------------

filtered_df = df.copy()

if len(date_range) == 2:
    start_date, end_date = date_range

    filtered_df = filtered_df[
        (filtered_df["Timestamp"].dt.date >= start_date) &
        (filtered_df["Timestamp"].dt.date <= end_date)
    ]

filtered_df = filtered_df[
    filtered_df["Year"].isin(selected_year)
]

filtered_df = filtered_df[
    filtered_df["Month Name"].isin(selected_month)
]

filtered_df = filtered_df[
    filtered_df["Season"].isin(selected_season)
]

filtered_df = filtered_df[
    filtered_df["Time Band"].isin(selected_timeband)
]

filtered_df = filtered_df[
    filtered_df["Weekend"].isin(selected_week)
]

# -----------------------------------------------------
# KPI Cards
# -----------------------------------------------------

total_sales = filtered_df["Sales Count"].sum()
total_redemption = filtered_df["Redemption Count"].sum()
total_activity = filtered_df["Total Activity Load"].sum()

capacity_utilization = (
    total_redemption / total_sales * 100
    if total_sales > 0 else 0
)

idle_capacity = (
    (filtered_df["Idle Capacity Indicator"] == "Idle").mean() * 100
)

average_oli = filtered_df["Operational Load Index"].mean()

peak_activity = filtered_df["Total Activity Load"].max()

average_redemption_ratio = filtered_df["Redemption Pressure Ratio"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.metric("🎫 Total Sales", f"{total_sales:,.0f}")
c2.metric("🚢 Total Redemption", f"{total_redemption:,.0f}")
c3.metric("📊 Total Activity", f"{total_activity:,.0f}")
c4.metric("⚙ Capacity Utilization", f"{capacity_utilization:.2f}%")

st.markdown("")

c5, c6, c7, c8 = st.columns(4)

c5.metric("💤 Idle Capacity", f"{idle_capacity:.2f}%")
c6.metric("📈 Avg Operational Load", f"{average_oli:.3f}")
c7.metric("🔥 Peak Activity", f"{peak_activity:,.0f}")
c8.metric("🎟 Redemption Ratio", f"{average_redemption_ratio:.2f}")

# -----------------------------------------------------
# Charts
# -----------------------------------------------------

yearly = filtered_df.groupby("Year")["Total Activity Load"].sum().reset_index()

st.plotly_chart(
    px.line(
        yearly,
        x="Year",
        y="Total Activity Load",
        markers=True,
        title="Yearly Activity Trend"
    ),
    use_container_width=True
)

monthly = (
    filtered_df.groupby("Month Name")["Total Activity Load"]
    .sum()
    .reindex(month_order)
    .reset_index()
)

st.plotly_chart(
    px.bar(
        monthly,
        x="Month Name",
        y="Total Activity Load",
        title="Monthly Activity"
    ),
    use_container_width=True
)

season = filtered_df.groupby("Season")["Total Activity Load"].sum().reset_index()

st.plotly_chart(
    px.pie(
        season,
        names="Season",
        values="Total Activity Load",
        title="Seasonal Activity"
    ),
    use_container_width=True
)

band = filtered_df.groupby("Time Band")["Total Activity Load"].sum().reset_index()

st.plotly_chart(
    px.bar(
        band,
        x="Time Band",
        y="Total Activity Load",
        title="Activity by Time Band"
    ),
    use_container_width=True
)

week = filtered_df.groupby("Weekend")["Total Activity Load"].sum().reset_index()

st.plotly_chart(
    px.bar(
        week,
        x="Weekend",
        y="Total Activity Load",
        title="Weekend vs Weekday"
    ),
    use_container_width=True
)

hour = filtered_df.groupby("Hour")["Total Activity Load"].sum().reset_index()

st.plotly_chart(
    px.line(
        hour,
        x="Hour",
        y="Total Activity Load",
        markers=True,
        title="Hourly Activity"
    ),
    use_container_width=True
)

# -----------------------------------------------------
# Download Button
# -----------------------------------------------------

st.download_button(
    label="📥 Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_ferry_data.csv",
    mime="text/csv"
)