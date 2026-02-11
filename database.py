import sqlite3
import hashlib

conn = sqlite3.connect("students.db", check_same_thread=False)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    fullname TEXT,
    email TEXT,
    password TEXT,
    age INTEGER,
    qualification TEXT
)
""")
conn.commit()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password, email, fullname, age, qualification):
    hashed = hash_password(password)
    try:
        cursor.execute(
            "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)",
            (username, fullname, email, hashed, age, qualification)
        )
        conn.commit()
        return "Registration successful"
    except:
        return "Username already exists"

def login_user(username, password):
    hashed = hash_password(password)
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hashed)
    )
    return cursor.fetchone()
