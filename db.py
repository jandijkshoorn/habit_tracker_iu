import sqlite3
from datetime import date


def get_db(name="main.db"):
    db = sqlite3.connect('main.db')
    create_tables(db)
    return db


def create_tables(db):
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS tracker (
        name TEXT PRIMARY KEY,
        description TEXT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS counter (
        date TEXT,
        trackerName TEXT,
        FOREIGN KEY (trackerName) REFERENCES tracker(name))""")

    db.commit()


def add_tracker(db, name, description):
    cur = db.cursor()
    cur.execute("INSERT INTO tracker VALUES (?, ?)", (name, description))
    db.commit()


def increment_tracker(db, name, event_date=None):
    cur = db.cursor()
    if not event_date:
        event_date = str(date.today())
    cur.execute("INSERT INTO counter VALUES (?,?)", (event_date, name))
    db.commit()


def get_tracker_data(db, name):
    cur = db.cursor()
    cur.execute("SELECT * FROM counter WHERE trackerName=?", (name,))
    return cur.fetchall()