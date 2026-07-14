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

st.markdown(
"""
This dashboard analyzes Toronto Island Ferry ticket activity
to identify operational efficiency, congestion patterns,
capacity utilization and idle periods.
"""
)

# -----------------------------------------------------
# Sidebar Filters
# -----------------------------------------------------

st.sidebar.header("Dashboard Filters")

# Date Range Filter
min_date = df["Timestamp"].min().date()
max_date = df["Timestamp"].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Year Filter
years = sorted(df["Year"].unique())

selected_year = st.sidebar.multiselect(
    "Select Year",
    years,
    default=years
)

# Month Filter
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

# Season Filter
season_order = ["Winter", "Spring", "Summer", "Autumn"]

selected_season = st.sidebar.multiselect(
    "Select Season",
    season_order,
    default=season_order
)

# Time Band Filter
timeband_order = ["Morning", "Afternoon", "Evening", "Night"]

selected_timeband = st.sidebar.multiselect(
    "Select Time Band",
    timeband_order,
    default=timeband_order
)

# Weekend Filter
selected_week = st.sidebar.multiselect(
    "Week Type",
    ["Weekday", "Weekend"],
    default=["Weekday", "Weekend"]
)

# -----------------------------------------------------
# Apply Filters
# -----------------------------------------------------

filtered_df = df.copy()

if len(date_range) == 2:
    start_date, end_date = date_range

    filtered_df = filtered_df[
        (filtered_df["Timestamp"].dt.date >= start_date)
        &
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
# KPI Calculations
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

# -----------------------------------------------------
# KPI Cards
# -----------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "🎫 Total Sales",
    f"{total_sales:,.0f}"
)

col2.metric(
    "🚢 Total Redemptions",
    f"{total_redemption:,.0f}"
)

col3.metric(
    "📊 Total Activity",
    f"{total_activity:,.0f}"
)

col4.metric(
    "⚙ Capacity Utilization",
    f"{capacity_utilization:.2f}%"
)

st.markdown("")

col5, col6, col7, col8 = st.columns(4)

col5.metric(
    "💤 Idle Capacity",
    f"{idle_capacity:.2f}%"
)

col6.metric(
    "📈 Avg Operational Load",
    f"{average_oli:.2f}"
)

col7.metric(
    "🔥 Peak Activity",
    f"{peak_activity:,.0f}"
)

col8.metric(
    "🎟 Avg Redemption Ratio",
    f"{average_redemption_ratio:.2f}"
)

# -----------------------------------------------------
# Yearly Trend
# -----------------------------------------------------

yearly = (
    filtered_df
    .groupby("Year")["Total Activity Load"]
    .sum()
    .reset_index()
)

fig = px.line(
    yearly,
    x="Year",
    y="Total Activity Load",
    markers=True,
    title="Yearly Activity Trend"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Monthly Trend
# -----------------------------------------------------

month_order = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]

monthly = (
    filtered_df
    .groupby("Month Name")["Total Activity Load"]
    .sum()
    .reindex(month_order)
    .reset_index()
)

fig = px.bar(
    monthly,
    x="Month Name",
    y="Total Activity Load",
    title="Monthly Activity"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Season vs Activity
# -----------------------------------------------------

season = (
    filtered_df
    .groupby("Season")["Total Activity Load"]
    .sum()
    .reset_index()
)

fig = px.pie(
    season,
    names="Season",
    values="Total Activity Load",
    title="Seasonal Activity"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Time Band Analysis
# -----------------------------------------------------

band = (
    filtered_df
    .groupby("Time Band")["Total Activity Load"]
    .sum()
    .reset_index()
)

fig = px.bar(
    band,
    x="Time Band",
    y="Total Activity Load",
    title="Activity by Time Band"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Weekend Analysis
# -----------------------------------------------------

week = (
    filtered_df
    .groupby("Weekend")["Total Activity Load"]
    .sum()
    .reset_index()
)

fig = px.bar(
    week,
    x="Weekend",
    y="Total Activity Load",
    title="Weekend vs Weekday"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Hourly Activity
# -----------------------------------------------------

hour = (
    filtered_df
    .groupby("Hour")["Total Activity Load"]
    .sum()
    .reset_index()
)

fig = px.line(
    hour,
    x="Hour",
    y="Total Activity Load",
    markers=True,
    title="Hourly Activity"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# Download Filtered Data
# -----------------------------------------------------

st.download_button(
    label="Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_ferry_data.csv",
    mime="text/csv"
)