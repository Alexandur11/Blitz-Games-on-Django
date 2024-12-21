import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('db.sqlite3')  # Ensure 'db.sqlite3' exists in your project directory

# Create a cursor object
cursor = connection.cursor()

# Execute a query
cursor.execute("SELECT * FROM blitz_games_app_series")
# Fetch and print the results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
connection.close()
