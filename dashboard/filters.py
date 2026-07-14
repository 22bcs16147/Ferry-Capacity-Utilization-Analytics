import streamlit as st
import pandas as pd


def apply_filters(df):
    """
    Apply sidebar filters and return filtered dataframe.
    """

    st.sidebar.header("📌 Dashboard Filters")

    # -------------------------------
    # Date Filter
    # -------------------------------

    min_date = df["Timestamp"].min().date()
    max_date = df["Timestamp"].max().date()

    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    # -------------------------------
    # Year Filter
    # -------------------------------

    years = sorted(df["Year"].unique())

    selected_year = st.sidebar.multiselect(
        "Select Year",
        years,
        default=years
    )

    # -------------------------------
    # Month Filter
    # -------------------------------

    month_order = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    selected_month = st.sidebar.multiselect(
        "Select Month",
        month_order,
        default=month_order
    )

    # -------------------------------
    # Season Filter
    # -------------------------------

    season_order = ["Winter", "Spring", "Summer", "Autumn"]

    selected_season = st.sidebar.multiselect(
        "Select Season",
        season_order,
        default=season_order
    )

    # -------------------------------
    # Time Band Filter
    # -------------------------------

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

    # -------------------------------
    # Week Type
    # -------------------------------

    selected_week = st.sidebar.multiselect(
        "Week Type",
        ["Weekday", "Weekend"],
        default=["Weekday", "Weekend"]
    )

    # -------------------------------
    # Apply Filters
    # -------------------------------

    filtered_df = df.copy()

    if len(date_range) == 2:

        start_date = date_range[0]
        end_date = date_range[1]

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

    return filtered_df