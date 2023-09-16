import sqlite3

conn = sqlite3.connect("db.sqlite3")
conn.row_factory = sqlite3.Row

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS users(
             id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
             name CHAR(128) NOT NULL,
             is_enabled BOOLEAN DEFAULT TRUE
    )
"""
)

conn.execute("INSERT INTO users(name) VALUES('Diego')")
conn.execute("INSERT INTO users(name) VALUES('Catalina')")

conn.commit()

c = conn.cursor()
c.execute("SELECT * FROM users")

for row in c.fetchall():
    print({**row})

conn.close()
