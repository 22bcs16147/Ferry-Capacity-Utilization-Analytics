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

st.sidebar.header("Filters")

years = sorted(df["Year"].unique())

selected_year = st.sidebar.multiselect(
    "Select Year",
    years,
    default=years
)

seasons = sorted(df["Season"].unique())

selected_season = st.sidebar.multiselect(
    "Select Season",
    seasons,
    default=seasons
)

timebands = sorted(df["Time Band"].unique())

selected_timeband = st.sidebar.multiselect(
    "Select Time Band",
    timebands,
    default=timebands
)

filtered_df = df[
    (df["Year"].isin(selected_year))
    &
    (df["Season"].isin(selected_season))
    &
    (df["Time Band"].isin(selected_timeband))
]

# -----------------------------------------------------
# KPI Cards
# -----------------------------------------------------

total_sales = filtered_df["Sales Count"].sum()

total_redemption = filtered_df["Redemption Count"].sum()

total_activity = filtered_df["Total Activity Load"].sum()

average_load = filtered_df["Operational Load Index"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Sales",
    f"{total_sales:,.0f}"
)

col2.metric(
    "Total Redemption",
    f"{total_redemption:,.0f}"
)

col3.metric(
    "Total Activity",
    f"{total_activity:,.0f}"
)

col4.metric(
    "Average OLI",
    f"{average_load:.2f}"
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