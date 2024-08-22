import sqlite3
from sqlite3 import Error

# Function to get user chat history from the SQLite database
def get_user_chat_history(username):
    connection = create_connection()
    if connection is None:
        return []
    
    try:
        create_chat_table(connection)  # Ensure the chat table exists
        cursor = connection.cursor()

        # Use parameterized query with SQLite placeholder `?`
        cursor.execute("SELECT message FROM chat_history WHERE username = ? ORDER BY timestamp ASC", (username,))
        chats = cursor.fetchall()
        return [chat[0] for chat in chats]  # Return a list of messages

    except Error as e:
        print(f"Error while fetching chat history: {e}")
        return []
    finally:
        if connection:
            connection.close()

# Function to add a new chat message to the SQLite database
def add_to_chat_history(username, message):
    connection = create_connection()
    if connection is None:
        return
    
    try:
        create_chat_table(connection)  # Ensure the chat table exists
        cursor = connection.cursor()

        # Use parameterized query with SQLite placeholder `?`
        cursor.execute("INSERT INTO chat_history (username, message) VALUES (?, ?)", (username, message))
        connection.commit()

    except Error as e:
        print(f"Error while inserting chat message: {e}")
    finally:
        if connection:
            connection.close()

# Function to create the chat history table if it does not exist
def create_chat_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                message TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        connection.commit()
    except Error as e:
        print(f"Error while creating chat table: {e}")

# Function to create a connection to the SQLite database
def create_connection():
    try:
        connection = sqlite3.connect('eventdb.sqlite')  # SQLite database file
        return connection
    except Error as e:
        print(f"Error while connecting to SQLite: {e}")
        return None
