import plotly.express as px
import streamlit as st


def yearly_activity_chart(df):

    yearly = (
        df.groupby("Year")["Total Activity Load"]
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


def monthly_activity_chart(df):

    month_order = [
        "January","February","March","April",
        "May","June","July","August",
        "September","October","November","December"
    ]

    monthly = (
        df.groupby("Month Name")["Total Activity Load"]
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


def seasonal_chart(df):

    season = (
        df.groupby("Season")["Total Activity Load"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        season,
        names="Season",
        values="Total Activity Load",
        title="Seasonal Activity Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)


def hourly_chart(df):

    hourly = (
        df.groupby("Hour")["Total Activity Load"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        hourly,
        x="Hour",
        y="Total Activity Load",
        markers=True,
        title="Hourly Activity Trend"
    )

    st.plotly_chart(fig, use_container_width=True)


def weekend_chart(df):

    week = (
        df.groupby("Weekend")["Total Activity Load"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        week,
        x="Weekend",
        y="Total Activity Load",
        title="Weekend vs Weekday Activity"
    )

    st.plotly_chart(fig, use_container_width=True)


def timeband_chart(df):

    band = (
        df.groupby("Time Band")["Total Activity Load"]
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


def operational_load_chart(df):

    fig = px.histogram(
        df,
        x="Operational Load Index",
        nbins=40,
        title="Operational Load Index Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)


def redemption_ratio_chart(df):

    fig = px.histogram(
        df,
        x="Redemption Pressure Ratio",
        nbins=40,
        title="Redemption Pressure Ratio Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)