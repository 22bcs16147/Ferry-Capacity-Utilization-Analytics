import streamlit as st
import pandas as pd

from filters import apply_filters
from kpi import show_kpis
from insights import show_insights

from charts import (
    yearly_activity_chart,
    monthly_activity_chart,
    seasonal_chart,
    timeband_chart,
    weekend_chart,
    hourly_chart,
    operational_load_chart,
    redemption_ratio_chart,
)

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Ferry Capacity Utilization Dashboard",
    page_icon="⛴️",
    layout="wide"
)

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv("data/processed/ferry_processed.csv")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    return df


df = load_data()

# -------------------------------------------------------
# Dashboard Title
# -------------------------------------------------------

st.title("⛴️ Ferry Capacity Utilization & Operational Efficiency Dashboard")

st.markdown("""
This dashboard analyzes Toronto Island Ferry ticket activity to understand
capacity utilization, operational efficiency, passenger demand,
congestion patterns and idle periods.
""")

# -------------------------------------------------------
# Sidebar Filters
# -------------------------------------------------------

filtered_df = apply_filters(df)

# -------------------------------------------------------
# KPI Section
# -------------------------------------------------------

show_kpis(filtered_df)

st.divider()

# -------------------------------------------------------
# Charts
# -------------------------------------------------------

left, right = st.columns(2)

with left:
    yearly_activity_chart(filtered_df)

with right:
    monthly_activity_chart(filtered_df)

left, right = st.columns(2)

with left:
    seasonal_chart(filtered_df)

with right:
    timeband_chart(filtered_df)

left, right = st.columns(2)

with left:
    weekend_chart(filtered_df)

with right:
    hourly_chart(filtered_df)

left, right = st.columns(2)

with left:
    operational_load_chart(filtered_df)

with right:
    redemption_ratio_chart(filtered_df)

st.divider()

# -------------------------------------------------------
# Business Insights
# -------------------------------------------------------

show_insights(filtered_df)

st.divider()

# -------------------------------------------------------
# Download Dataset
# -------------------------------------------------------

st.download_button(
    label="📥 Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_ferry_data.csv",
    mime="text/csv",
)