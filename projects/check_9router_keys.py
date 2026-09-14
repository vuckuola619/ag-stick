import sqlite3
import os
import json

db_path = os.path.expandvars(r'%APPDATA%\9router\db\data.sqlite')
conn = sqlite3.connect(db_path)
cur = conn.cursor()

print("--- API KEYS TABLE ---")
try:
    cur.execute("SELECT * FROM apiKeys")
    cols = [d[0] for d in cur.description]
    rows = cur.fetchall()
    for r in rows:
        print(dict(zip(cols, r)))
except Exception as e:
    print("Error querying apiKeys:", e)

print("\n--- APP SETTINGS OR KEYS ---")
try:
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print("Tables:", cur.fetchall())
except Exception as e:
    print(e)
