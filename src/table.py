import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database!")

conn.execute('CREATE TABLE tempTable (name TEXT,transcription TEXT, notes TEXT, date DATE )')
print("Table created successfully")

conn.close()

