import sqlite3

conn = sqlite3.connect("leaderboard.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS leaders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    wins INTEGER DEFAULT 0,
    losses INTEGER DEFAULT 0,
    ties INTEGER DEFAULT 0,
    total INTEGER DEFAULT 0
)
""")

conn.commit()
conn.close()

print("Leaderboard database created!")
