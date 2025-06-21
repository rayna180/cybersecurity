import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Connect to the SQLite database
conn = sqlite3.connect("data/sales_data.db")
cursor = conn.cursor()

# 2️⃣ Query 1: Total sales revenue
query_total = """
SELECT
    SUM(quantity * price) AS total_revenue
FROM sales;
"""
cursor.execute(query_total)
total_revenue = cursor.fetchone()[0]
print(f"Total Revenue: ${total_revenue:,.2f}")

# 3️⃣ Query 2: Revenue by category
query_by_cat = """
SELECT
    category,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC;
"""
df_cat = pd.read_sql_query(query_by_cat, conn)
print("\nRevenue by Category:")
print(df_cat)

# 4️⃣ Visualize: Bar chart of revenue by category
plt.figure(figsize=(8, 5))
plt.bar(df_cat['category'], df_cat['revenue'])
plt.title('Revenue by Category')
plt.xlabel('Category')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5️⃣ Query 3: Top 5 products by units sold
query_top_products = """
SELECT
    product,
    SUM(quantity) AS total_units_sold
FROM sales
GROUP BY product
ORDER BY total_units_sold DESC
LIMIT 5;
"""
df_top = pd.read_sql_query(query_top_products, conn)
print("\nTop 5 Products by Units Sold:")
print(df_top)

# 6️⃣ Visualize: Bar chart of top 5 products by units sold
plt.figure(figsize=(8, 5))
plt.bar(df_top['product'], df_top['total_units_sold'])
plt.title('Top 5 Products by Units Sold')
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7️⃣ Clean up
conn.close()

