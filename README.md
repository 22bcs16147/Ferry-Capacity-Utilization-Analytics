# ⛴️ Ferry Capacity Utilization & Operational Efficiency Analytics System

## 📌 Project Overview

The **Ferry Capacity Utilization & Operational Efficiency Analytics System** is an end-to-end Data Analytics project developed to analyze Toronto Island Ferry ticket activity and evaluate operational performance. The project transforms raw ticket transaction data into actionable business insights through data preprocessing, exploratory data analysis, interactive dashboards, KPI monitoring, and passenger demand forecasting.

An interactive **Streamlit dashboard** enables users to analyze historical ferry operations using multiple filters, visualize passenger demand trends, monitor operational efficiency, and support data-driven decision-making for resource planning.

---

# 🎯 Business Problem

Ferry transportation experiences significant fluctuations in passenger demand depending on season, weekdays, weekends, holidays, and time of day. Without proper analysis, ferry operators may face:

- Underutilized ferry capacity
- Passenger congestion during peak hours
- Inefficient staff allocation
- Increased operational costs
- Poor passenger experience

This project helps identify operational bottlenecks and provides analytical insights for optimizing ferry services.

---

# 🎯 Project Objectives

- Analyze historical ferry ticket activity.
- Measure operational efficiency using business KPIs.
- Identify passenger demand trends.
- Detect idle operational periods.
- Measure ferry capacity utilization.
- Perform seasonal and time-based analysis.
- Forecast future passenger demand using Facebook Prophet.
- Support operational planning through data-driven insights.

---

# 📂 Dataset Information

| Attribute | Details |
|-----------|----------|
| Dataset | Toronto Island Ferry Ticket Activity |
| Time Period | 2015 – 2025 |
| Granularity | 15-minute intervals |
| Records | 261,538+ |
| Source | Toronto Open Data |

---

# 🛠️ Technology Stack

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Prophet (Facebook Prophet)
- Git
- GitHub
- VS Code

---

# 📁 Project Structure

```text
Ferry-Capacity-Utilization-Analytics
│
├── assets
│   ├── charts
│   ├── forecast
│   └── screenshots
│
├── dashboard
│   └── app.py
│
├── data
│   ├── raw
│   └── processed
│
├── src
│   ├── data_understanding.py
│   ├── feature_engineering.py
│   ├── exploratory_analysis.py
│   ├── forecasting.py
│   └── kpi_analysis.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🔄 Project Workflow

```
Raw Dataset
      │
      ▼
Data Understanding
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Exploratory Data Analysis
      │
      ▼
KPI Analysis
      │
      ▼
Interactive Streamlit Dashboard
      │
      ▼
Passenger Demand Forecasting
      │
      ▼
Business Insights & Recommendations
```

---

# 📊 Dashboard Features

The interactive Streamlit dashboard includes:

- Interactive Date Range Filter
- Year Filter
- Month Filter
- Season Filter
- Time Band Filter
- Weekday vs Weekend Filter
- Executive Summary
- Business Insights
- Download Filtered Dataset
- Interactive Plotly Visualizations

---

# 📈 Key Performance Indicators (KPIs)

The dashboard monitors the following operational KPIs:

| KPI | Value |
|------|--------|
| 🎫 Total Sales | **12,972,051** |
| 🚢 Total Redemption | **12,785,293** |
| 📊 Total Activity Load | **25,757,344** |
| ⚙️ Capacity Utilization | **98.56%** |
| 💤 Idle Capacity | **44.86%** |
| 📈 Average Operational Load Index | **0.007** |
| 🔥 Peak Activity | **14,445** |
| 🎟️ Redemption Pressure Ratio | **1.29** |

---

# 📉 Exploratory Data Analysis

The project performs comprehensive exploratory analysis including:

- Yearly Passenger Activity
- Monthly Trends
- Seasonal Analysis
- Hourly Passenger Demand
- Weekend vs Weekday Comparison
- Time Band Analysis
- Passenger Activity Distribution
- Operational Load Analysis

---

# 🔮 Passenger Demand Forecasting

The project uses the **Facebook Prophet** forecasting model to predict passenger demand for the next **30 days**.

### Forecast Outputs

- Forecast Visualization
- Forecast Results CSV
- Interactive HTML Forecast Dashboard

The forecasting model helps ferry operators anticipate future passenger demand and improve operational planning.

---

# 💡 Business Insights

The dashboard automatically identifies:

- Peak operating hours
- Least busy operating hours
- Highest demand months
- Lowest demand months
- Capacity utilization status
- Seasonal demand patterns
- Passenger activity trends

---

# ✅ Operational Recommendations

Based on the analysis, the following recommendations are provided:

- Increase ferry frequency during peak demand periods.
- Optimize staffing during weekends and summer seasons.
- Reduce idle ferry deployment during low-demand hours.
- Monitor operational load continuously.
- Utilize historical trends for seasonal planning.
- Improve ferry scheduling based on passenger demand forecasts.

---

# 📷 Dashboard Screenshots

## Dashboard Home

![Dashboard](assets/screenshots/dashboard_home.png)

---

## KPI Dashboard

![KPIs](assets/screenshots/kpi_cards.png)

---

## Dashboard Filters

![Filters](assets/screenshots/filters.png)

---

## Interactive Charts

![Charts](assets/screenshots/charts.png)

---

## Business Insights

![Insights](assets/screenshots/business_insights.png)

---

## Passenger Demand Forecast

![Forecast](assets/screenshots/forecast.png)

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/22bcs16147/Ferry-Capacity-Utilization-Analytics.git
```

Navigate to the project directory:

```bash
cd Ferry-Capacity-Utilization-Analytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the Streamlit Dashboard:

```bash
streamlit run dashboard/app.py
```

Run Passenger Forecasting:

```bash
python src/forecasting.py
```

---

# 📌 Project Outcomes

- Built a complete end-to-end analytics solution.
- Designed an interactive business dashboard using Streamlit.
- Developed multiple operational KPIs.
- Automated passenger demand forecasting.
- Generated business recommendations using data analytics.
- Improved operational decision support through visualization and forecasting.

---

# 🔮 Future Enhancements

- Live API Integration
- Real-time Passenger Monitoring
- Weather Data Integration
- Machine Learning Forecasting Models
- Route Optimization Algorithms
- Automated Operational Alerts
- Mobile Dashboard Support

---

# 👤 Author

**Nidhi**

Data Analyst | Python | SQL | Power BI | Streamlit | Machine Learning

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is licensed under the MIT License.