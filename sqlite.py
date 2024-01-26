import sqlite3

# Connect to SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('tasks.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define a table schema and create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
    duration TEXT
    start_time TEXT
    end_time TEXT
    is_tracking INTEGER
    )
''')

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
