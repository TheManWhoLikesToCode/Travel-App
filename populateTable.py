import sqlite3
from datetime import datetime, timedelta

# Connect to the SQLite database
conn = sqlite3.connect('db/travel.db')
c = conn.cursor()

# Define some example data
data = [
    (1, "New York", "London", "2023-08-01", "2023-08-15"),
    (2, "Paris", "Tokyo", "2023-09-01", "2023-09-20"),
    (3, "Sydney", "Los Angeles", "2023-10-01", "2023-10-15"),
]

# Insert the data into the "destinations" table
for row in data:
    c.execute("""
        INSERT INTO destinations (id, Departure_Location, Arrival_Location, Departure_Date, Arrival_Date)
        VALUES (?, ?, ?, ?, ?)
    """, row)

# Commit the changes and close the connection
conn.commit()
conn.close()
