import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Sales Insights Dashboard", layout="wide")
st.title("📊 Sales Insights Dashboard")

# Sidebar filter 
metric = st.sidebar.radio(
    "Choose metric to view:",
    ("Revenue by Category", "Top Products by Units Sold")
)

# Connect to DB and execute query
conn = sqlite3.connect("data/sales_data.db")

if metric == "Revenue by Category":
    query = """
    SELECT category, SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY category
    ORDER BY revenue DESC;
    """
    df = pd.read_sql_query(query, conn)
    st.subheader("Revenue by Category")
    fig = px.bar(df, x="category", y="revenue",
                 labels={"revenue":"Revenue ($)","category":"Category"},
                 title="Revenue by Category")
    st.plotly_chart(fig, use_container_width=True)

else:  # Top Products
    query = """
    SELECT product, SUM(quantity) AS total_units_sold
    FROM sales
    GROUP BY product
    ORDER BY total_units_sold DESC
    LIMIT 5;
    """
    df = pd.read_sql_query(query, conn)
    st.subheader("Top 5 Products by Units Sold")
    fig = px.bar(df, x="product", y="total_units_sold",
                 labels={"total_units_sold":"Units Sold","product":"Product"},
                 title="Top 5 Products by Units Sold")
    st.plotly_chart(fig, use_container_width=True)

conn.close()
