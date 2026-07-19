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
# Executive Summary
# -----------------------------------------------------

st.markdown("---")
st.subheader("📌 Executive Summary")

# Analysis Period
analysis_start = filtered_df["Timestamp"].min().date()
analysis_end = filtered_df["Timestamp"].max().date()

# Total Years
total_years = filtered_df["Year"].nunique()

# Busiest Year
busiest_year = (
    filtered_df.groupby("Year")["Total Activity Load"]
    .sum()
    .idxmax()
)

# Busiest Season
busiest_season = (
    filtered_df.groupby("Season")["Total Activity Load"]
    .sum()
    .idxmax()
)

# Peak Hour
peak_hour = (
    filtered_df.groupby("Hour")["Total Activity Load"]
    .sum()
    .idxmax()
)

# Average Daily Activity
daily_activity = (
    filtered_df.groupby(filtered_df["Timestamp"].dt.date)["Total Activity Load"]
    .sum()
    .mean()
)

summary1, summary2, summary3 = st.columns(3)

summary1.info(
    f"""
**Analysis Period**

{analysis_start}

to

{analysis_end}
"""
)

summary2.success(
    f"""
**Coverage**

Years Covered: **{total_years}**

Busiest Year: **{busiest_year}**
"""
)

summary3.warning(
    f"""
**Operations**

Peak Hour: **{peak_hour}:00**

Busiest Season: **{busiest_season}**

Average Daily Activity: **{daily_activity:,.0f}**
"""
)

st.markdown("---")

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
    width="stretch"
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
    width="stretch"
)

season = filtered_df.groupby("Season")["Total Activity Load"].sum().reset_index()

st.plotly_chart(
    px.pie(
        season,
        names="Season",
        values="Total Activity Load",
        title="Seasonal Activity"
    ),
    width="stretch"
)

band = filtered_df.groupby("Time Band")["Total Activity Load"].sum().reset_index()

st.plotly_chart(
    px.bar(
        band,
        x="Time Band",
        y="Total Activity Load",
        title="Activity by Time Band"
    ),
   width="stretch"
)

week = filtered_df.groupby("Weekend")["Total Activity Load"].sum().reset_index()

st.plotly_chart(
    px.bar(
        week,
        x="Weekend",
        y="Total Activity Load",
        title="Weekend vs Weekday"
    ),
    width="stretch"
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
width="stretch")
# -----------------------------------------------------
# Top 10 Busiest Hours
# -----------------------------------------------------

st.markdown("---")
st.subheader("🕒 Top 10 Busiest Hours")

top_hours = (
    filtered_df.groupby("Hour")["Total Activity Load"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_hours,
    x="Hour",
    y="Total Activity Load",
    color="Total Activity Load",
    text="Total Activity Load",
    title="Top 10 Peak Operating Hours"
)

fig.update_traces(textposition="outside")

st.plotly_chart(
    fig,
    width="stretch"
)

st.dataframe(
    top_hours,
    width="stretch"
)
# -----------------------------------------------------
# Top 10 Least Busy Hours
# -----------------------------------------------------

st.markdown("---")
st.subheader("🌙 Top 10 Least Busy Hours")

least_hours = (
    filtered_df.groupby("Hour")["Total Activity Load"]
    .sum()
    .sort_values(ascending=True)
    .head(10)
    .reset_index()
)

fig = px.bar(
    least_hours,
    x="Hour",
    y="Total Activity Load",
    color="Total Activity Load",
    text="Total Activity Load",
    title="Top 10 Least Busy Operating Hours"
)

fig.update_traces(textposition="outside")

st.plotly_chart(
    fig,
    width="stretch"
)

st.dataframe(
    least_hours,
    width="stretch"
)
# -----------------------------------------------------
# Top 10 Busiest Days
# -----------------------------------------------------

st.markdown("---")
st.subheader("📅 Top 10 Busiest Days")

daily_activity = (
    filtered_df.groupby(filtered_df["Timestamp"].dt.date)["Total Activity Load"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

daily_activity.columns = ["Date", "Total Activity Load"]

fig = px.bar(
    daily_activity,
    x="Date",
    y="Total Activity Load",
    color="Total Activity Load",
    text="Total Activity Load",
    title="Top 10 Busiest Days"
)

fig.update_traces(textposition="outside")

st.plotly_chart(
    fig,
    width="stretch"
)

st.dataframe(
    daily_activity,
    width="stretch"
)
# -----------------------------------------------------
# Top 10 Least Busy Days
# -----------------------------------------------------

st.markdown("---")
st.subheader("📅 Top 10 Least Busy Days")

least_days = (
    filtered_df.groupby(filtered_df["Timestamp"].dt.date)["Total Activity Load"]
    .sum()
    .sort_values(ascending=True)
    .head(10)
    .reset_index()
)

least_days.columns = ["Date", "Total Activity Load"]

fig = px.bar(
    least_days,
    x="Date",
    y="Total Activity Load",
    color="Total Activity Load",
    text="Total Activity Load",
    title="Top 10 Least Busy Days"
)

fig.update_traces(textposition="outside")

st.plotly_chart(
    fig,
    width="stretch"
)

st.dataframe(
    least_days,
    width="stretch"
)
# -----------------------------------------------------
# Monthly Performance Ranking
# -----------------------------------------------------

st.markdown("---")
st.subheader("🏆 Monthly Performance Ranking")

monthly_ranking = (
    filtered_df.groupby("Month Name")["Total Activity Load"]
    .sum()
    .reindex(month_order)
    .reset_index()
)

monthly_ranking = monthly_ranking.sort_values(
    by="Total Activity Load",
    ascending=False
).reset_index(drop=True)

monthly_ranking.index = monthly_ranking.index + 1
monthly_ranking.rename_axis("Rank", inplace=True)
monthly_ranking.reset_index(inplace=True)


def performance_label(value):

    if value >= monthly_ranking["Total Activity Load"].quantile(0.75):
        return "Excellent"

    elif value >= monthly_ranking["Total Activity Load"].quantile(0.50):
        return "Good"

    elif value >= monthly_ranking["Total Activity Load"].quantile(0.25):
        return "Average"

    else:
        return "Low"


monthly_ranking["Performance"] = monthly_ranking[
    "Total Activity Load"
].apply(performance_label)

st.dataframe(
    monthly_ranking,
    width="stretch"
)
# -----------------------------------------------------
# Operational Efficiency Score
# -----------------------------------------------------

st.markdown("---")
st.subheader("⚙ Operational Efficiency Score")

efficiency_score = (
    capacity_utilization * 0.5
    + (100 - idle_capacity) * 0.3
    + (average_redemption_ratio * 100) * 0.2
)

efficiency_score = min(efficiency_score, 100)

if efficiency_score >= 85:
    status = "🟢 Excellent"

elif efficiency_score >= 70:
    status = "🟡 Good"

else:
    status = "🔴 Needs Improvement"

col1, col2 = st.columns(2)

col1.metric(
    "Operational Efficiency Score",
    f"{efficiency_score:.2f}/100"
)

col2.metric(
    "Operational Status",
    status
)
# -----------------------------------------------------
# Congestion Analysis
# -----------------------------------------------------

st.markdown("---")
st.subheader("🚦 Congestion Analysis")

congestion = (
    filtered_df.groupby("Hour")["Total Activity Load"]
    .sum()
    .reset_index()
)

high_limit = congestion["Total Activity Load"].quantile(0.75)
low_limit = congestion["Total Activity Load"].quantile(0.25)


def congestion_level(activity):

    if activity >= high_limit:
        return "High"

    elif activity >= low_limit:
        return "Moderate"

    else:
        return "Low"


congestion["Congestion Level"] = congestion[
    "Total Activity Load"
].apply(congestion_level)

fig = px.bar(
    congestion,
    x="Hour",
    y="Total Activity Load",
    color="Congestion Level",
    title="Hourly Congestion Analysis",
    text="Total Activity Load"
)

fig.update_traces(textposition="outside")

st.plotly_chart(
    fig,
    width="stretch"
)

st.dataframe(
    congestion,
    width="stretch"
)
# -----------------------------------------------------
# Peak Demand Summary
# -----------------------------------------------------

st.markdown("---")
st.subheader("📊 Peak Demand Summary")

peak_day = (
    filtered_df.groupby(filtered_df["Timestamp"].dt.date)["Total Activity Load"]
    .sum()
    .idxmax()
)

peak_day_activity = (
    filtered_df.groupby(filtered_df["Timestamp"].dt.date)["Total Activity Load"]
    .sum()
    .max()
)

peak_month = (
    filtered_df.groupby("Month Name")["Total Activity Load"]
    .sum()
    .idxmax()
)

peak_season = (
    filtered_df.groupby("Season")["Total Activity Load"]
    .sum()
    .idxmax()
)

col1, col2 = st.columns(2)

with col1:
    st.info(f"""
### Peak Demand

📅 Peak Day: **{peak_day}**

🕒 Peak Hour: **{peak_hour}:00**

📈 Activity: **{peak_day_activity:,.0f}**
""")

with col2:
    st.success(f"""
### Seasonal Demand

📆 Peak Month: **{peak_month}**

🌞 Peak Season: **{peak_season}**

⚙ Capacity Utilization: **{capacity_utilization:.2f}%**
""")
    # -----------------------------------------------------
# Monthly Growth Analysis
# -----------------------------------------------------

st.markdown("---")
st.subheader("📈 Monthly Growth Analysis")

monthly_growth = (
    filtered_df.groupby(["Year", "Month", "Month Name"])["Total Activity Load"]
    .sum()
    .reset_index()
)

monthly_growth = monthly_growth.sort_values(["Year", "Month"])

monthly_growth["Growth %"] = (
    monthly_growth["Total Activity Load"]
    .pct_change() * 100
)

fig = px.line(
    monthly_growth,
    x="Month Name",
    y="Growth %",
    color="Year",
    markers=True,
    title="Month-over-Month Growth (%)"
)

st.plotly_chart(
    fig,
    width="stretch"
)

st.dataframe(
    monthly_growth,
    width="stretch"
)
# -----------------------------------------------------
# Yearly Performance Ranking
# -----------------------------------------------------

st.markdown("---")
st.subheader("🏅 Yearly Performance Ranking")

yearly_rank = (
    filtered_df.groupby("Year")["Total Activity Load"]
    .sum()
    .reset_index()
)

yearly_rank = yearly_rank.sort_values(
    by="Total Activity Load",
    ascending=False
)

fig = px.bar(
    yearly_rank,
    x="Year",
    y="Total Activity Load",
    color="Total Activity Load",
    text="Total Activity Load",
    title="Yearly Passenger Activity Ranking"
)

fig.update_traces(textposition="outside")

st.plotly_chart(
    fig,
    width="stretch"
)

st.dataframe(
    yearly_rank,
    width="stretch"
)
# -----------------------------------------------------
# Activity Heatmap
# -----------------------------------------------------

st.markdown("---")
st.subheader("🔥 Activity Heatmap (Month vs Hour)")

heatmap_df = (
    filtered_df.groupby(["Month Name", "Hour"])["Total Activity Load"]
    .sum()
    .reset_index()
)

month_order = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]

heatmap_df["Month Name"] = pd.Categorical(
    heatmap_df["Month Name"],
    categories=month_order,
    ordered=True
)

heatmap_df = heatmap_df.sort_values("Month Name")

fig = px.density_heatmap(
    heatmap_df,
    x="Hour",
    y="Month Name",
    z="Total Activity Load",
    color_continuous_scale="Viridis",
    title="Passenger Activity Heatmap"
)

st.plotly_chart(fig, width="stretch")
# -----------------------------------------------------
# Business Insights
# -----------------------------------------------------

st.markdown("---")
st.subheader("📈 Business Insights & Recommendations")

# Peak Hour
peak_hour = (
    filtered_df.groupby("Hour")["Total Activity Load"]
    .sum()
    .idxmax()
)

# Least Busy Hour
least_busy_hour = (
    filtered_df.groupby("Hour")["Total Activity Load"]
    .sum()
    .idxmin()
)

# Busiest Month
busiest_month = (
    filtered_df.groupby("Month Name")["Total Activity Load"]
    .sum()
    .idxmax()
)

# Least Busy Month
least_busy_month = (
    filtered_df.groupby("Month Name")["Total Activity Load"]
    .sum()
    .idxmin()
)

# Capacity Status
if capacity_utilization >= 90:
    capacity_status = "High Utilization"
elif capacity_utilization >= 70:
    capacity_status = "Optimal Utilization"
else:
    capacity_status = "Under Utilized"

st.success(f"""
### Executive Insights

• Peak operating hour: **{peak_hour}:00**

• Least busy hour: **{least_busy_hour}:00**

• Highest passenger demand month: **{busiest_month}**

• Lowest passenger demand month: **{least_busy_month}**

• Overall Capacity Status: **{capacity_status}**
""")

st.info("""
### Operational Recommendations

✅ Increase ferry frequency during peak hours.

✅ Optimize staffing during weekends and summer months.

✅ Reduce idle ferry deployment during low-demand periods.

✅ Monitor operational load continuously to improve passenger experience.

✅ Use historical trends for seasonal planning and resource allocation.
""")

# -----------------------------------------------------
# Download Button
# -----------------------------------------------------

st.download_button(
    label="📥 Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_ferry_data.csv",
    mime="text/csv"
)