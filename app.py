# V-1

# import streamlit as st
# from auth import create_connection, create_usertable, login_user, add_userdata, user_exists, make_hashes, check_hashes, validate_password
# from client import client_main

# # set config for streamlit app and set title to Verbo and icon to 🖌️ 
# st.set_page_config(layout="centered", page_title="Verbo", page_icon="🖌")

# # Initialize session state for login
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False
# if 'username' not in st.session_state:
#     st.session_state.username = ''

# def main():
#     st.markdown(
#         """
#         <style>
#         .container {
#             background-image: url("https://cdn.pixabay.com/animation/2023/06/26/03/02/03-02-03-917_512.gif");
#             background-size: cover;
#             margin: 0;
#             padding: 50px;
#             border-radius: 5px;
#             border: 1px solid #ddd;
#             position: relative;
#             overflow: hidden;
#             transition: background-color 0.5s ease;
#             background-color: #000; 
#         }

#         .container::before {
#             content: "";
#             position: absolute;
#             top: 0;
#             left: 0;
#             width: 0;
#             height: 100%;
#             background-color: rgb(106, 156, 137, 0.5);
#             transition: width 0.5s ease;
#             z-index: 0;
#         }

#         .container:hover::before {
#             width: 100%;
#         }

#         .container h4,
#         .container p {
#             position: relative;
#             z-index: 1;
#             color: #fff;
#             transition: color 0.5s ease, font-size 0.5s ease;
#         }

#         .container:hover h4,
#         .container:hover p {
#             color: #fff;
#             font-size: 1.1em; /* Slightly larger on hover */
#         }

#         .translated-container,
#         .wiki-container {
#             position: relative;
#             padding: 10px;
#             border-radius: 5px;
#             border: 1px solid #ddd;
#             margin-top: 20px;
#             color: #fff;
#             transition: background-color 0.5s ease, color 0.5s ease, font-size 0.5s ease;
#             overflow: hidden;
#         }

#         .translated-container::before,
#         .wiki-container::before {
#             content: "";
#             position: absolute;
#             top: 0;
#             left: 0;
#             width: 0;
#             height: 100%;
#             background-color: rgba(0, 0, 0, 0.5);
#             transition: width 0.5s ease;
#             z-index: 0;
#         }

#         .translated-container:hover::before,
#         .wiki-container:hover::before {
#             width: 100%;
#         }

#         .translated-container:hover,
#         .wiki-container:hover {
#             background-color: #444b6e; /* Change background color on hover */
#             font-size: 1.1em; /* Slightly larger on hover */
#         }

#         .translated-container h4,
#         .translated-container p,
#         .wiki-container h4,
#         .wiki-container p {
#             position: relative;
#             z-index: 1;
#         }

#         audio {
#             margin-top: 20px;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     st.markdown(
#         """
#         <div class="container">
#             <h4>Verbo 🖌️</h4>
#             <p>Translate. Converse. Connect.</p>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )
#     if st.session_state.logged_in:
#         st.sidebar.success(f"Logged in as {st.session_state.username}")
        
#         if st.sidebar.button("Logout"):
#             st.session_state.logged_in = False
#             st.session_state.username = ''
#             st.query_params()  # Refresh the app to go back to the login screen

#         client_main()   # Load the client functionalities if the user is logged in
#     else:
#         menu = ["Login", "SignUp"]
#         choice = st.sidebar.selectbox("Menu", menu)

#         connection = create_connection()
#         if connection is None:
#             st.error("Could not connect to the database.")
#             return

#         if choice == "Login":
#             st.sidebar.subheader("Login Section")
#             username = st.sidebar.text_input("User Name")
#             password = st.sidebar.text_input("Password", type='password')

#             if st.sidebar.button("Login"):
#                 create_usertable(connection)
#                 hashed_pswd = make_hashes(password)
#                 result = login_user(connection, username, check_hashes(password, hashed_pswd))
#                 if result:
#                     st.session_state.logged_in = True  # Set the login state
#                     st.session_state.username = username
#                     st.success(f"Logged In as {username}")
#                     client_main()  # Load the client functionalities after successful login
#                 else:
#                     st.warning("Incorrect Username/Password")

#         elif choice == "SignUp":
#             st.sidebar.subheader("Create New Account")
#             new_user = st.sidebar.text_input("Username")
#             new_password = st.sidebar.text_input("Password", type='password')
#             confirm_password = st.sidebar.text_input("Confirm Password", type='password')

#             if st.sidebar.button("Signup"):
#                 create_usertable(connection)

#                 if user_exists(connection, new_user):
#                     st.warning("User already exists. Please choose a different username.")
#                 elif new_password != confirm_password:
#                     st.warning("Passwords do not match.")
#                 else:
#                     is_valid, message = validate_password(new_password)
#                     if not is_valid:
#                         st.warning(message)
#                     else:
#                         add_userdata(connection, new_user, make_hashes(new_password))
#                         st.success("You have successfully created an account")
#                         st.info("Go to the Login Menu to log in")

# if __name__ == '__main__':
#     main()


# V-2
# import streamlit as st
# from auth import create_connection, create_usertable, login_user, add_userdata, user_exists, make_hashes, check_hashes, validate_password
# from client import client_main
 
# st.set_page_config(layout="centered", page_title="Verbo", page_icon="🖌")

# # Initialize session state for login, username, and chat history
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False
# if 'username' not in st.session_state:
#     st.session_state.username = ''
# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = []

# def main():
#     # Home page styling and structure
#     st.markdown("""
#         <style>
#         .container {
#             background-image: url("https://cdn.pixabay.com/animation/2023/06/26/03/02/03-02-03-917_512.gif");
#             background-size: cover;
#             margin: 0;
#             padding: 50px;
#             border-radius: 5px;
#             border: 1px solid #ddd;
#             position: relative;
#             overflow: hidden;
#             transition: background-color 0.5s ease;
#             background-color: #000; 
#         }

#         .container::before {
#             content: "";
#             position: absolute;
#             top: 0;
#             left: 0;
#             width: 0;
#             height: 100%;
#             background-color: rgb(106, 156, 137, 0.5);
#             transition: width 0.5s ease;
#             z-index: 0;
#         }

#         .container:hover::before {
#             width: 100%;
#         }

#         .container h4,
#         .container p {
#             position: relative;
#             z-index: 1;
#             color: #fff;
#             transition: color 0.5s ease, font-size 0.5s ease;
#         }

#         .container:hover h4,
#         .container:hover p {
#             color: #fff;
#             font-size: 1.1em; /* Slightly larger on hover */
#         }

#         .translated-container,
#         .wiki-container {
#             position: relative;
#             padding: 10px;
#             border-radius: 5px;
#             border: 1px solid #ddd;
#             margin-top: 20px;
#             color: #fff;
#             transition: background-color 0.5s ease, color 0.5s ease, font-size 0.5s ease;
#             overflow: hidden;
#         }

#         .translated-container::before,
#         .wiki-container::before {
#             content: "";
#             position: absolute;
#             top: 0;
#             left: 0;
#             width: 0;
#             height: 100%;
#             background-color: rgba(0, 0, 0, 0.5);
#             transition: width 0.5s ease;
#             z-index: 0;
#         }

#         .translated-container:hover::before,
#         .wiki-container:hover::before {
#             width: 100%;
#         }

#         .translated-container:hover,
#         .wiki-container:hover {
#             background-color: #444b6e; /* Change background color on hover */
#             font-size: 1.1em; /* Slightly larger on hover */
#         }

#         .translated-container h4,
#         .translated-container p,
#         .wiki-container h4,
#         .wiki-container p {
#             position: relative;
#             z-index: 1;
#         }

#         audio {
#             margin-top: 20px;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )
#     st.markdown(
#             """
#             <div class="container">
#                 <h4>Welcome to Verbo 🖌️</h4>
#                 <p>Translate. Converse. Connect.</p>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )
#     if st.session_state.logged_in:
#         st.sidebar.success(f"Logged in as {st.session_state.username}")
        
#         if st.sidebar.button("Logout"):
#             st.session_state.logged_in = False
#             st.session_state.username = ''
#             st.session_state.chat_history.clear()  # Clear chat history on logout
#             st.experimental_set_query_params()   # Refresh the app to go back to the login screen

#         # Display profile and chat history
#         st.sidebar.header(f"Welcome, {st.session_state.username}!")
#         st.sidebar.subheader("Your Chat History:")

#         if st.session_state.chat_history:
#             for chat in st.session_state.chat_history:
#                 st.sidebar.write(chat)
#         else:
#             st.sidebar.write("No chat history yet.")

#         # Load client functionalities (assumed chat interface)
#         client_main()

#     else:
#         # Home Page for non-logged-in users
        

#         # Sidebar for login and signup
#         menu = ["Login", "SignUp"]
#         choice = st.sidebar.selectbox("Menu", menu)

#         connection = create_connection()
#         if connection is None:
#             st.error("Could not connect to the database.")
#             return

#         if choice == "Login":
#             st.sidebar.subheader("Login Section")
#             username = st.sidebar.text_input("User Name")
#             password = st.sidebar.text_input("Password", type='password')

#             if st.sidebar.button("Login"):
#                 if username and password:
#                     create_usertable(connection)
#                     hashed_pswd = make_hashes(password)
#                     result = login_user(connection, username, check_hashes(password, hashed_pswd))
#                     if result:
#                         st.session_state.logged_in = True  # Set the login state
#                         st.session_state.username = username
#                         st.success(f"Logged In as {username}")
#                         client_main()
#                     else:
#                         st.warning("Incorrect Username/Password")
#                 else:
#                     st.warning("Please fill all the mandatory fields")
                    
                    
#         elif choice == "SignUp":
#             st.sidebar.subheader("Create New Account")
#             new_user = st.sidebar.text_input("Username")
#             new_password = st.sidebar.text_input("Password", type='password')
#             confirm_password = st.sidebar.text_input("Confirm Password", type='password')

#             if st.sidebar.button("Signup"):
#                 if  new_user and new_password and confirm_password:
#                     create_usertable(connection)
#                     if user_exists(connection, new_user):
#                         st.warning("User already exists. Please choose a different username.")
#                     elif new_password != confirm_password:
#                         st.warning("Passwords do not match.")
#                     else:
#                         is_valid, message = validate_password(new_password)
#                         if not is_valid:
#                             st.warning(message)
#                         else:
#                             add_userdata(connection, new_user, make_hashes(new_password))
#                             st.success("You have successfully created an account")
#                             st.info("Go to the Login Menu to log in")
#                 else:
#                     st.warning("Please fill all the mandatory fields")
                    
# if __name__ == '__main__':
#     main()




# V-3
import streamlit as st
from auth import (
    create_connection, create_usertable, delete_user_account, login_user, add_userdata, user_exists, 
    make_hashes, check_hashes, validate_password
)
from client import client_main

st.set_page_config(layout="centered", page_title="Verbo", page_icon="🖌")

# Initialize session state for login, username, and chat history
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Function to load chat history from the database
def load_chat_history():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        cursor.execute("SELECT message FROM chat_history WHERE username = %s ORDER BY timestamp ASC", (st.session_state.username,))
        st.session_state.chat_history = [chat[0] for chat in cursor.fetchall()]
        connection.close()

def main():
    # Home page styling and structure
    st.markdown("""
        <style>
        .container {
            background-image: url("https://cdn.pixabay.com/animation/2023/06/26/03/02/03-02-03-917_512.gif");
            background-size: cover;
            margin: 0;
            padding: 50px;
            border-radius: 5px;
            border: 1px solid #ddd;
            position: relative;
            overflow: hidden;
            transition: background-color 0.5s ease;
            background-color: #000; 
        }

        .container::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 0;
            height: 100%;
            background-color: rgb(106, 156, 137, 0.5);
            transition: width 0.5s ease;
            z-index: 0;
        }

        .container:hover::before {
            width: 100%;
        }

        .container h4,
        .container p {
            position: relative;
            z-index: 1;
            color: #fff;
            transition: color 0.5s ease, font-size 0.5s ease;
        }

        .container:hover h4,
        .container:hover p {
            color: #fff;
            font-size: 1.1em; /* Slightly larger on hover */
        }

        .translated-container,
        .wiki-container {
            position: relative;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ddd;
            margin-top: 20px;
            color: #fff;
            transition: background-color 0.5s ease, color 0.5s ease, font-size 0.5s ease;
            overflow: hidden;
        }

        .translated-container::before,
        .wiki-container::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 0;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            transition: width 0.5s ease;
            z-index: 0;
        }

        .translated-container:hover::before,
        .wiki-container:hover::before {
            width: 100%;
        }

        .translated-container:hover,
        .wiki-container:hover {
            background-color: #444b6e; /* Change background color on hover */
            font-size: 1.1em; /* Slightly larger on hover */
        }

        .translated-container h4,
        .translated-container p,
        .wiki-container h4,
        .wiki-container p {
            position: relative;
            z-index: 1;
        }

        audio {
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
            """
            <div class="container">
                <h4>Welcome to Verbo 🖌️</h4>
                <p>Translate. Converse. Connect.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if st.session_state.logged_in:
        st.sidebar.success(f"Logged in as {st.session_state.username}")
        
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ''
            st.session_state.chat_history.clear()  # Clear chat history on logout
            st.experimental_set_query_params()   # Refresh the app to go back to the login screen

        # Display profile and chat history
        st.sidebar.header(f"Welcome, {st.session_state.username}!")


        # if st.sidebar.button("Re-Translate"):
        #     load_chat_history()

        # if st.session_state.chat_history:
        #     for chat in st.session_state.chat_history:
        #         st.sidebar.write(chat)
        # else:
        #     st.sidebar.write("No chat history yet.")
        
        

        # Load client functionalities (assumed chat interface)
        client_main()
        st.sidebar.subheader("Delete Account")
        
        confirm_delete = st.sidebar.button("Delete Account")
        if confirm_delete:
            delete_password = st.sidebar.text_input("Confirm Password for Deletion", type='password')
            if delete_password:
                connection = create_connection()
                if connection:
                    success = delete_user_account(connection, st.session_state.username, delete_password)
                    if success:
                        st.success("Account successfully deleted.")
                        st.session_state.logged_in = False
                        st.session_state.username = ''
                        st.session_state.chat_history.clear()
                        st.experimental_set_query_params()  # Refresh the app to go back to the login screen
                        st.experimental_rerun()  # Trigger a full page reload
                    else:
                        st.warning("Incorrect password or error deleting account.")
                else:
                    st.error("Could not connect to the database.")
            else:
                st.warning("Please enter your password to confirm account deletion.")

    else:
        # Sidebar for login and signup
        menu = ["Login", "SignUp"]
        choice = st.sidebar.selectbox("Menu", menu)

        connection = create_connection()
        if connection is None:
            st.error("Could not connect to the database.")
            return

        if choice == "Login":
            st.sidebar.subheader("Login Section")
            username = st.sidebar.text_input("User Name")
            password = st.sidebar.text_input("Password", type='password')

            if st.sidebar.button("Login"):
                if username and password:
                    create_usertable(connection)
                    hashed_pswd = make_hashes(password)
                    result = login_user(connection, username, check_hashes(password, hashed_pswd))
                    if result:
                        st.session_state.logged_in = True  # Set the login state
                        st.session_state.username = username
                        load_chat_history()  # Load chat history after successful login
                        st.success(f"Logged In as {username}")
                        client_main()
                    else:
                        st.warning("Incorrect Username/Password")
                else:
                    st.warning("Please fill all the mandatory fields")

        elif choice == "SignUp":
            st.sidebar.subheader("Create New Account")
            new_user = st.sidebar.text_input("Username")
            new_password = st.sidebar.text_input("Password", type='password')
            confirm_password = st.sidebar.text_input("Confirm Password", type='password')

            if st.sidebar.button("Signup"):
                if new_user and new_password and confirm_password:
                    create_usertable(connection)
                    if user_exists(connection, new_user):
                        st.warning("User already exists. Please choose a different username.")
                    elif new_password != confirm_password:
                        st.warning("Passwords do not match.")
                    else:
                        is_valid, message = validate_password(new_password)
                        if not is_valid:
                            st.warning(message)
                        else:
                            add_userdata(connection, new_user, make_hashes(new_password))
                            st.success("You have successfully created an account")
                            st.info("Go to the Login Menu to log in")
                else:
                    st.warning("Please fill all the mandatory fields")

if __name__ == '__main__':
    main()
