import sqlite3
import hashlib

# Connect to database
conn = sqlite3.connect("students.db", check_same_thread=False)
cursor = conn.cursor()

# ---------------- CREATE TABLE ----------------
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

# ---------------- PASSWORD HASHING ----------------
def hash_password(password):
    """Hashes the password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

# ---------------- REGISTER USER ----------------
def register_user(username, password, email, fullname, age, qualification):
    """Registers a new user in the database."""
    try:
        hashed_password = hash_password(password)
        cursor.execute(
            "INSERT INTO users (username, fullname, email, password, age, qualification) VALUES (?, ?, ?, ?, ?, ?)",
            (username, fullname, email, hashed_password, age, qualification)
        )
        conn.commit()
        return "✅ Account created successfully!"
    except sqlite3.IntegrityError:
        return "❌ Username already exists. Try a different one."

# ---------------- LOGIN USER ----------------
def login_user(username, password):
    """Verifies username and password. Returns user data if valid."""
    hashed_password = hash_password(password)
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, hashed_password)
    )
    user = cursor.fetchone()  # Returns a tuple: (username, fullname, email, password, age, qualification)
    return user
