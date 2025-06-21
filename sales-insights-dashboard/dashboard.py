import os
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

# Locate the database file
# __file__ is the path to this dashboard.py, so BASE_DIR is your app folder
BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "data", "sales_data.db")

#  Connect to the database
conn = sqlite3.connect(DB_PATH)

# Query & display based on sidebar choice
if metric == "Revenue by Category":
    query = """
    SELECT category,
           SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY category
    ORDER BY revenue DESC;
    """
    df = pd.read_sql_query(query, conn)
    st.subheader("Revenue by Category")
    fig = px.bar(
        df,
        x="category",
        y="revenue",
        labels={"revenue": "Revenue ($)", "category": "Category"},
        title="Revenue by Category"
    )
    st.plotly_chart(fig, use_container_width=True)

else:  
    query = """
    SELECT product,
           SUM(quantity) AS total_units_sold
    FROM sales
    GROUP BY product
    ORDER BY total_units_sold DESC
    LIMIT 5;
    """
    df = pd.read_sql_query(query, conn)
    st.subheader("Top 5 Products by Units Sold")
    fig = px.bar(
        df,
        x="product",
        y="total_units_sold",
        labels={"total_units_sold": "Units Sold", "product": "Product"},
        title="Top 5 Products by Units Sold"
    )
    st.plotly_chart(fig, use_container_width=True)

# Clean up 
conn.close()

