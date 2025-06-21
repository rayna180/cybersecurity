import os
import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st
from datetime import datetime

#  Page config 
st.set_page_config(page_title="Sales Insights Dashboard", layout="wide")
st.title("📊 Sales Insights Dashboard")

# Locate database
BASE_DIR = os.path.dirname(__file__)
DB_PATH  = os.path.join(BASE_DIR, "data", "sales_data.db")

#  Caching helper
@st.cache_data(show_spinner=False)
def load_data(query: str):
    """Run a SQL query and return a DataFrame."""
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql_query(query, conn)

#  Sidebar
st.sidebar.header("Filters & Options")

# 1) Date range picker (min/max from the data)
min_date, max_date = load_data("SELECT MIN(order_date) AS d FROM sales;").iloc[0,0], \
                     load_data("SELECT MAX(order_date) AS d FROM sales;").iloc[0,0]
start_date, end_date = st.sidebar.date_input(
    "Select date range:",
    value=(pd.to_datetime(min_date), pd.to_datetime(max_date)),
    min_value=pd.to_datetime(min_date),
    max_value=pd.to_datetime(max_date)
)

# 2) Metric selector
metric = st.sidebar.selectbox(
    "Choose metric to view:",
    [
        "Revenue by Category",
        "Top Products by Units Sold",
        "Sales Over Time",
        "Average Order Value"
    ]
)

#  Build date‐filtered SQL WHERE clause 
where_clause = (
    f"WHERE order_date BETWEEN '{start_date:%Y-%m-%d}' "
    f"AND '{end_date:%Y-%m-%d}'"
)

# Queries & Charts 
if metric == "Revenue by Category":
    st.subheader("💰 Revenue by Category")
    st.markdown(
        "Total revenue per product category in your selected date range."
    )
    query = f"""
        SELECT
            category,
            SUM(quantity * price) AS revenue
        FROM sales
        {where_clause}
        GROUP BY category
        ORDER BY revenue DESC;
    """
    df = load_data(query)
    fig = px.bar(
        df, x="category", y="revenue",
        title="Revenue by Category",
        labels={"revenue": "Revenue ($)", "category": "Category"},
        color="category",
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    st.plotly_chart(fig, use_container_width=True)

elif metric == "Top Products by Units Sold":
    st.subheader("🏆 Top 5 Products by Units Sold")
    st.markdown(
        "The five best‐selling products (by units sold) in your date range."
    )
    query = f"""
        SELECT
            product,
            SUM(quantity) AS total_units_sold
        FROM sales
        {where_clause}
        GROUP BY product
        ORDER BY total_units_sold DESC
        LIMIT 5;
    """
    df = load_data(query)
    fig = px.bar(
        df, x="product", y="total_units_sold",
        title="Top 5 Products by Units Sold",
        labels={"total_units_sold": "Units Sold", "product": "Product"},
        color="product",
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    st.plotly_chart(fig, use_container_width=True)

elif metric == "Sales Over Time":
    st.subheader("📈 Sales Over Time")
    st.markdown(
        "Daily total revenue trend over your selected date range."
    )
    query = f"""
        SELECT
            order_date AS date,
            SUM(quantity * price) AS daily_revenue
        FROM sales
        {where_clause}
        GROUP BY order_date
        ORDER BY order_date;
    """
    df = load_data(query)
    df["date"] = pd.to_datetime(df["date"])
    fig = px.line(
        df, x="date", y="daily_revenue", markers=True,
        title="Daily Revenue Over Time",
        labels={"daily_revenue": "Daily Revenue ($)", "date": "Date"}
    )
    st.plotly_chart(fig, use_container_width=True)

else:  # Average Order Value
    st.subheader("📊 Average Order Value (AOV)")
    st.markdown(
        "Average revenue per order in your selected date range."
    )
    query = f"""
        SELECT
            ROUND(AVG(quantity * price), 2) AS avg_order_value
        FROM sales
        {where_clause};
    """
    df = load_data(query)
    aov = df.iloc[0, 0]
    st.metric("Average Order Value", f"${aov:,.2f}")

# Footer
st.markdown("---")
st.markdown("Built with Python, SQLite, Pandas, Plotly & Streamlit")

