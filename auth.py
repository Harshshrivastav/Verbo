# import streamlit as st
# import hashlib
# import mysql.connector
# from mysql.connector import Error
# import re


# def validate_password(password):
#     """
#     Validates that the password meets certain criteria:
#     - At least 8 characters long
#     - Contains at least one number
#     - Contains at least one uppercase letter
#     - Contains at least one lowercase letter
#     - Contains at least one special character
#     """
#     if len(password) < 8:
#         return False, "Password must be at least 8 characters."
#     if not re.search(r"\d", password):
#         return False, "Password must contain at least one number."
#     if not re.search(r"[A-Z]", password):
#         return False, "Password must contain at least one uppercase letter."
#     if not re.search(r"[a-z]", password):
#         return False, "Password must contain at least one lowercase letter."
#     if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
#         return False, "Password must contain at least one special character."
#     return True, ""


# # Function to hash passwords
# def make_hashes(password):
#     return hashlib.sha256(str.encode(password)).hexdigest()

# # Function to check hashed passwords
# def check_hashes(password, hashed_text):
#     if make_hashes(password) == hashed_text:
#         return hashed_text
#     return False

# # MySQL connection setup
# def create_connection():
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='Shriv@st@v@096',
#             database='eventdb'
#         )
#         if connection.is_connected():
#             return connection
#     except Error as e:
#         st.error(f"Error connecting to MySQL: {e}")
#         return None

# # Create the userstable if it doesn't exist
# def create_usertable(connection):
#     try:
#         cursor = connection.cursor()
#         cursor.execute('CREATE TABLE IF NOT EXISTS userstable (username VARCHAR(255), password VARCHAR(255))')
#         connection.commit()
#     except Error as e:
#         st.error(f"Error creating table: {e}")

# # Function to add a new user
# def add_userdata(connection, username, password):
#     try:
#         cursor = connection.cursor()
#         cursor.execute('INSERT INTO userstable (username, password) VALUES (%s, %s)', (username, password))
#         connection.commit()
#     except Error as e:
#         st.error(f"Error inserting data: {e}")

# # Function to check if a user already exists
# def user_exists(connection, username):
#     try:
#         cursor = connection.cursor()
#         cursor.execute('SELECT * FROM userstable WHERE username = %s', (username,))
#         data = cursor.fetchall()
#         return len(data) > 0
#     except Error as e:
#         st.error(f"Error checking user existence: {e}")
#         return False

# # Function to login user
# def login_user(connection, username, password):
#     try:
#         cursor = connection.cursor()
#         cursor.execute('SELECT * FROM userstable WHERE username = %s AND password = %s', (username, password))
#         data = cursor.fetchall()
#         return data
#     except Error as e:
#         st.error(f"Error fetching data: {e}")
#         return None
    
    
# # Function to delete a user account
# def delete_user_account(connection, username, password):
#     try:
#         cursor = connection.cursor()
#         cursor.execute('SELECT password FROM userstable WHERE username = %s', (username,))
#         stored_password = cursor.fetchone()
        
#         if stored_password and check_hashes(password, stored_password[0]):
#             cursor.execute('DELETE FROM userstable WHERE username = %s', (username,))
#             connection.commit()
#             return True
#         else:
#             return False
#     except Error as e:
#         connection.rollback()  # Rollback in case of error
#         st.error(f"Error deleting user: {e}")
#         return False

import streamlit as st
import hashlib
import sqlite3  # SQLite instead of MySQL
import re

# Function to validate passwords
def validate_password(password):
    """
    Validates that the password meets certain criteria:
    - At least 8 characters long
    - Contains at least one number
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one special character
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one number."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, ""


# Function to hash passwords
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Function to check hashed passwords
def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

# SQLite connection setup
def create_connection():
    try:
        connection = sqlite3.connect('eventdb.db')
        return connection
    except sqlite3.Error as e:
        st.error(f"Error connecting to SQLite: {e}")
        return None

# Create the userstable if it doesn't exist
def create_usertable(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS userstable (username TEXT, password TEXT)')
        connection.commit()
    except sqlite3.Error as e:
        st.error(f"Error creating table: {e}")

# Function to add a new user
def add_userdata(connection, username, password):
    try:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO userstable (username, password) VALUES (?, ?)', (username, password))
        connection.commit()
    except sqlite3.Error as e:
        st.error(f"Error inserting data: {e}")

# Function to check if a user already exists
def user_exists(connection, username):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM userstable WHERE username = ?', (username,))
        data = cursor.fetchall()
        return len(data) > 0
    except sqlite3.Error as e:
        st.error(f"Error checking user existence: {e}")
        return False

# Function to login user
def login_user(connection, username, password):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
        data = cursor.fetchall()
        return data
    except sqlite3.Error as e:
        st.error(f"Error fetching data: {e}")
        return None

# Function to delete a user account
def delete_user_account(connection, username, password):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT password FROM userstable WHERE username = ?', (username,))
        stored_password = cursor.fetchone()
        
        if stored_password and check_hashes(password, stored_password[0]):
            cursor.execute('DELETE FROM userstable WHERE username = ?', (username,))
            connection.commit()
            return True
        else:
            return False
    except sqlite3.Error as e:
        connection.rollback()  # Rollback in case of error
        st.error(f"Error deleting user: {e}")
        return False

