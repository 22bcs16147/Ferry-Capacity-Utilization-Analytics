import streamlit as st
import pandas as pd

from filters import apply_filters
from kpi import show_kpis

from charts import (
    yearly_activity_chart,
    monthly_activity_chart,
    seasonal_chart,
    timeband_chart,
    weekend_chart,
    hourly_chart,
    operational_load_chart,
    redemption_ratio_chart
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
This dashboard analyzes Toronto Island Ferry ticket activity to identify
capacity utilization, passenger demand, congestion patterns,
operational efficiency and idle periods.
""")

# -------------------------------------------------------
# Apply Filters
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

col1, col2 = st.columns(2)

with col1:
    yearly_activity_chart(filtered_df)

with col2:
    monthly_activity_chart(filtered_df)

col3, col4 = st.columns(2)

with col3:
    seasonal_chart(filtered_df)

with col4:
    timeband_chart(filtered_df)

col5, col6 = st.columns(2)

with col5:
    weekend_chart(filtered_df)

with col6:
    hourly_chart(filtered_df)

col7, col8 = st.columns(2)

with col7:
    operational_load_chart(filtered_df)

with col8:
    redemption_ratio_chart(filtered_df)

# -------------------------------------------------------
# Download Filtered Dataset
# -------------------------------------------------------

st.divider()

st.download_button(
    label="📥 Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_ferry_data.csv",
    mime="text/csv"
)