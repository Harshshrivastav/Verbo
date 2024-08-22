import mysql.connector
from mysql.connector import Error

# Function to get user chat history from the MySQL database
def get_user_chat_history(username):
    connection = create_connection()
    if connection is None:
        return []
    
    try:
        create_chat_table(connection)  # Ensure the chat table exists
        cursor = connection.cursor()

        # Use parameterized query to prevent SQL injection
        cursor.execute("SELECT message FROM chat_history WHERE username = %s ORDER BY timestamp ASC", (username,))
        chats = cursor.fetchall()
        return [chat[0] for chat in chats]  # Return a list of messages

    except Error as e:
        print(f"Error while fetching chat history: {e}")
        return []
    finally:
        if connection.is_connected():
            connection.close()

# Function to add a new chat message to the MySQL database
def add_to_chat_history(username, message):
    connection = create_connection()
    if connection is None:
        return
    
    try:
        create_chat_table(connection)  # Ensure the chat table exists
        cursor = connection.cursor()

        # Use parameterized query to prevent SQL injection
        cursor.execute("INSERT INTO chat_history (username, message) VALUES (%s, %s)", (username, message))
        connection.commit()

    except Error as e:
        print(f"Error while inserting chat message: {e}")
    finally:
        if connection.is_connected():
            connection.close()

# Function to create the chat history table if it does not exist
def create_chat_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_history (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                message TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        connection.commit()
    except Error as e:
        print(f"Error while creating chat table: {e}")

# Function to create a connection to the MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Shriv@st@v@096',
            database='eventdb'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
