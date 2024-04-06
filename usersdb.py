import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

# Create a table to store user credentials
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE,
                    email TEXT UNIQUE,
                    age INTEGER,
                    gender TEXT,
                    password TEXT
                 )''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Database created successfully!")
