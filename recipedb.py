import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()

#Create a table to store recipe details
cursor.execute('''CREATE TABLE IF NOT EXISTS recipes (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    ingredients TEXT NOT NULL,
                    procedure TEXT NOT NULL,
                    youtube_link TEXT,
                    image_path TEXT
                 )''')



# Commit changes and close connection
conn.commit()
conn.close()

print("Database 'recipes.db' and table 'recipes' created successfully!")
