import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("assistant.db", check_same_thread=False)

# Create a cursor
cursor = conn.cursor()

# Create table for uploaded documents
cursor.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Create table for chat history
cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT,
    chat_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Save changes
conn.commit()


# Function to save uploaded document
def save_document(filename):
    cursor.execute(
        "INSERT INTO documents(filename) VALUES(?)",
        (filename,)
    )
    conn.commit()


# Function to save chat
def save_chat(question, answer):
    cursor.execute(
        "INSERT INTO chat_history(question, answer) VALUES(?, ?)",
        (question, answer)
    )
    conn.commit()


# Function to get chat history
def get_chat_history():
    cursor.execute("SELECT question, answer FROM chat_history")
    return cursor.fetchall()


# Function to get uploaded documents
def get_documents():
    cursor.execute("SELECT filename FROM documents")
    return cursor.fetchall()