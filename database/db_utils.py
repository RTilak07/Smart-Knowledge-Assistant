import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("database/history.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        question TEXT,
        answer TEXT,
        time TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_history(url, question, answer):
    conn = sqlite3.connect("database/history.db")
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO history (url, question, answer, time)
    VALUES (?, ?, ?, ?)
    """, (url, question, answer, datetime.now()))
    conn.commit()
    conn.close()
