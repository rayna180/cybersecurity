import sqlite3

# Create the database file
connection = sqlite3.connect("data/sales_data.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# cREATE THE 'SALES' TABLE IF IT DOESN'T ALREADY EXIST
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    order_id    INTEGER PRIMARY KEY,
    product     TEXT,
    category    TEXT,
    quantity    INTEGER,
    price       REAL,
    order_date  TEXT
)
               """)

# Define sample sales data as a list tuples
sample_data = [
    (1, "Laptop",     "Electronics", 1, 1200.00, "2024-01-01"),
    (2, "Headphones", "Electronics", 2, 150.00,  "2024-01-03"),
    (3, "Keyboard",   "Electronics", 1, 100.00,  "2024-01-05"),
    (4, "Monitor",    "Electronics", 1, 300.00,  "2024-02-10"),
    (5, "Mouse",      "Electronics", 3, 25.00,   "2024-02-12"),
    (6, "Webcam",     "Electronics", 1, 75.00,   "2024-02-15"),
]

# Insert all sample rows into the sales table
cursor.executemany(
    "INSERT INTO sales (order_id, product, category, quantity, price, order_date) VALUES (?, ?, ?, ?, ?, ?)",
    sample_data
)

# Save the changes and close the coonnection
connection.commit()
connection.close()

print("✅ Created sales_data.db and inserted sample data!")