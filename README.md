# ⛴️ Ferry Capacity Utilization & Operational Efficiency Analytics System

An end-to-end Data Analytics project that analyzes Toronto Island Ferry ticket activity to evaluate operational efficiency, passenger demand, capacity utilization, and forecasting. The project combines data preprocessing, exploratory data analysis, interactive dashboarding, and time-series forecasting to generate actionable business insights.

---

## 🌐 Live Demo

**🚀 Streamlit Dashboard:**  
https://ferry-capacity-utilization-analytics-nidhi.streamlit.app/

**💻 GitHub Repository:**  
https://github.com/22bcs16147/Ferry-Capacity-Utilization-Analytics

---

## 📌 Project Overview

This project analyzes over **261,000 ferry ticket records** to understand passenger traffic, identify operational bottlenecks, measure capacity utilization, and forecast future demand.

The dashboard enables stakeholders to monitor ferry operations, improve resource allocation, optimize schedules, and support data-driven decision-making.

---

## 🎯 Project Objectives

- Analyze ferry passenger activity across multiple years.
- Measure operational efficiency using key performance indicators.
- Identify peak demand periods and idle capacity.
- Monitor seasonal and hourly passenger trends.
- Forecast passenger demand for the next 30 days.
- Support operational planning through interactive visualizations.

---

## 📊 Dashboard Features

### Key Performance Indicators (KPIs)

- 🎫 Total Sales
- 🚢 Total Redemption
- 📊 Total Activity Load
- ⚙️ Capacity Utilization
- 💤 Idle Capacity
- 📈 Average Operational Load Index
- 🔥 Peak Activity
- 🎟️ Redemption Pressure Ratio

### Interactive Filters

- Date Range
- Year
- Month
- Season
- Time Band
- Weekday / Weekend

### Visualizations

- Yearly Activity Trend
- Monthly Passenger Activity
- Seasonal Activity Distribution
- Activity by Time Band
- Weekend vs Weekday Analysis
- Hourly Activity Trend

### Business Insights

- Peak Operating Hour
- Least Busy Hour
- Busiest Month
- Least Busy Month
- Capacity Utilization Status
- Operational Recommendations

---

## 🔮 Forecasting

Passenger demand forecasting is implemented using **Facebook Prophet**.

The forecasting module predicts the next **30 days** of passenger demand, helping operators improve staffing, scheduling, and resource allocation.

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Prophet
- Matplotlib
- Scikit-learn
- OpenPyXL
- Git
- GitHub

---

## 📂 Project Structure

```
Ferry-Capacity-Utilization-Analytics
│
├── dashboard/
│   └── app.py
│
├── src/
│   ├── data_understanding.py
│   ├── feature_engineering.py
│   ├── exploratory_analysis.py
│   ├── kpi_analysis.py
│   └── forecasting.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── assets/
│   ├── charts/
│   └── forecast/
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## 📷 Dashboard Screenshots

### Main Dashboard

(Add your dashboard screenshot here)

### Forecasting

(Add your forecasting chart screenshot here)

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/22bcs16147/Ferry-Capacity-Utilization-Analytics.git
```

Move into the project

```bash
cd Ferry-Capacity-Utilization-Analytics
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run dashboard/app.py
```

---

## 📈 Key Business Insights

- Capacity utilization exceeds 98%, indicating highly efficient ferry operations.
- Passenger demand peaks during summer and weekends.
- Idle capacity is concentrated during off-peak periods.
- Peak-hour analysis supports optimized ferry scheduling.
- Demand forecasting enables proactive operational planning.

---

## 👩‍💻 Author

**Nidhi**

GitHub:
https://github.com/22bcs16147

---

## ⭐ If you found this project useful, consider giving it a star!