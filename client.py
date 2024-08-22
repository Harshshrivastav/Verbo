# # V-1

# import requests
# import streamlit as st
# from gtts import gTTS
# import io
# import base64
# import PyPDF2  # For reading PDF files

# # Set up Streamlit page configuration
# st.set_page_config(
#     page_title="LCEL_APEX",
#     page_icon="🖌️",
#     layout="centered",
# )

# # Styling for the container with hover effect and custom styles
# st.markdown(
#     """
#     <style>
#     .container {
#         background-image: url("https://cdn.pixabay.com/animation/2023/06/26/03/02/03-02-03-917_512.gif");
#         background-size: cover;
#         margin: 0;
#         padding: 50px;
#         border-radius: 5px;
#         border: 1px solid #ddd;
#         position: relative;
#         overflow: hidden;
#         transition: background-color 0.5s ease;
#         background-color: #000; 
#     }

#     .container::before {
#         content: "";
#         position: absolute;
#         top: 0;
#         left: 0;
#         width: 0;
#         height: 100%;
#         background-color: rgb(106, 156, 137, 0.5);
#         transition: width 0.5s ease;
#         z-index: 0;
#     }

#     .container:hover::before {
#         width: 100%;
#     }

#     .container h4,
#     .container p {
#         position: relative;
#         z-index: 1;
#         color: #fff;
#         transition: color 0.5s ease, font-size 0.5s ease;
#     }

#     .container:hover h4,
#     .container:hover p {
#         color: #fff;
#         font-size: 1.1em; /* Slightly larger on hover */
#     }

#     .translated-container,
#     .wiki-container {
#         position: relative;
#         padding: 10px;
#         border-radius: 5px;
#         border: 1px solid #ddd;
#         margin-top: 20px;
#         color: #fff;
#         transition: background-color 0.5s ease, color 0.5s ease, font-size 0.5s ease;
#         overflow: hidden;
#     }

#     .translated-container::before,
#     .wiki-container::before {
#         content: "";
#         position: absolute;
#         top: 0;
#         left: 0;
#         width: 0;
#         height: 100%;
#         background-color: rgba(0, 0, 0, 0.5);
#         transition: width 0.5s ease;
#         z-index: 0;
#     }

#     .translated-container:hover::before,
#     .wiki-container:hover::before {
#         width: 100%;
#     }

#     .translated-container:hover,
#     .wiki-container:hover {
#         background-color: #444b6e; /* Change background color on hover */
#         font-size: 1.1em; /* Slightly larger on hover */
#     }

#     .translated-container h4,
#     .translated-container p,
#     .wiki-container h4,
#     .wiki-container p {
#         position: relative;
#         z-index: 1;
#     }

#     audio {
#         margin-top: 20px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Sidebar toggle for input method
# st.sidebar.title("Settings")
# input_method = st.sidebar.radio(
#     "Select input method",
#     ("Type your input manually", "Upload a PDF or Text file"),
#     index=0  # Default is "Type your input manually"
# )
# # Main UI layout with basic styling and header
# st.markdown(
#     """
#     <div class="container">
#         <h4>🖌️ LCEL_APEX</h4>
#         <p>Confused! Converse your thoughts with APEX</p>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# # Dropdown for language selection
# languages = [
#     "Arabic", "Chinese", "Dutch", "English", "French", "German", "Greek", "Hebrew", "Hindi", "Hungarian",
#     "Italian", "Japanese", "Korean", "Latvian", "Lithuanian", "Norwegian", "Persian", "Polish", "Portuguese",
#     "Romanian", "Russian", "Spanish", "Swedish", "Thai", "Turkish", "Ukrainian", "Vietnamese", "Swahili",
#     "Czech", "Slovak", "Bulgarian", "Catalan", "Danish", "Finnish", "Serbian",
#     "Hindi", "Bengali", "Telugu", "Marathi", "Tamil", "Urdu", "Gujarati", "Malayalam", "Kannada", "Odia",
#     "Punjabi", "Assamese", "Maithili", "Sanskrit", "Nepali", "Manipuri", "Konkani", "Sikkimese", "Bodo"
# ]
# selected_language = st.selectbox("Select the target language", languages)

# # Function to read content from uploaded file
# def read_uploaded_file(uploaded_file):
#     if uploaded_file is not None:
#         if uploaded_file.type == "application/pdf":
#             pdf_reader = PyPDF2.PdfReader(uploaded_file)
#             text = ""
#             for page_num in range(len(pdf_reader.pages)):
#                 page = pdf_reader.pages[page_num]
#                 text += page.extract_text()
#             return text
#         elif uploaded_file.type == "text/plain":
#             return uploaded_file.read().decode("utf-8")
#     return ""

# # Handling user input based on selected method
# if input_method == "Type your input manually":
#     input_text = st.text_input("Enter the text you want to convert")
# else:
#     uploaded_file = st.sidebar.file_uploader("Upload a PDF or Text file", type=["pdf", "txt"])
#     input_text = read_uploaded_file(uploaded_file)
#     if input_text:
#         st.text_area("Content from uploaded file", input_text, height=200)

# # Function to get response from Groq
# def get_groq_response(input_text, language):
#     json_body = {
#         "input": {
#             "language": language,
#             "text": f"{input_text}"
#         },
#         "config": {},
#         "kwargs": {}
#     }
#     response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)

#     try:
#         response_data = response.json()
#         output_message = response_data.get("output", "No result field in response")
#         return output_message
#     except ValueError:
#         return "Error: Invalid JSON response"

# # Function to fetch Wikipedia context
# def get_wikipedia_context(query):
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles={query}&exintro=1&explaintext=1"
#     headers = {'User-Agent': user_agent}
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         data = response.json()
#         pages = data.get('query', {}).get('pages', {})
#         if pages:
#             page = next(iter(pages.values()))
#             return page.get('extract', 'No content found')
#         else:
#             return 'No content found'
#     else:
#         return 'Failed to retrieve content'

# # Function to convert text to speech
# def text_to_speech(text):
#     tts = gTTS(text=text, lang='en', slow=False)
#     audio_bytes = io.BytesIO()
#     tts.write_to_fp(audio_bytes)
#     audio_bytes.seek(0)
#     return audio_bytes

# # Function to display audio
# def display_audio(audio_bytes):
#     audio_base64 = base64.b64encode(audio_bytes.read()).decode()
#     st.markdown(f'<audio controls src="data:audio/mp3;base64,{audio_base64}"></audio>', unsafe_allow_html=True)


# # Main logic for processing input
# if input_text:
#     with st.spinner('Translation in progress...'):
#         output_message = get_groq_response(input_text, selected_language)
        
#         st.markdown(
#             f"""
#             <div class="translated-container">
#                 <h4>Translated Text:</h4>
#                 <p>{output_message}</p>
#             </div>
#             """, unsafe_allow_html=True
#         )
        
#     with st.spinner('Fetching response from Wikipedia...'):
#         context = get_wikipedia_context(input_text)
#         st.markdown(
#             f"""
#             <div class="wiki-container">
#                 <h4>Wikipedia Context:</h4>
#                 <p>{context}</p>
#             </div>
#             """, unsafe_allow_html=True
#         )
    
#     if st.button("🔊 Speak Translated Text"):
#         with st.spinner('Converting text to audio...'):
#             audio_bytes = text_to_speech(output_message)
#             display_audio(audio_bytes)


# V-2

# import streamlit as st
# import requests
# import PyPDF2
# from gtts import gTTS
# import io
# import base64

# # Function to read content from uploaded file
# def read_uploaded_file(uploaded_file):
#     if uploaded_file is not None:
#         if uploaded_file.type == "application/pdf":
#             pdf_reader = PyPDF2.PdfReader(uploaded_file)
#             text = ""
#             for page_num in range(len(pdf_reader.pages)):
#                 page = pdf_reader.pages[page_num]
#                 text += page.extract_text()
#             return text
#         elif uploaded_file.type == "text/plain":
#             return uploaded_file.read().decode("utf-8")
#     return ""

# # Function to get response from Groq
# def get_groq_response(input_text, language):
#     json_body = {
#         "input": {
#             "language": language,
#             "text": f"{input_text}"
#         },
#         "config": {},
#         "kwargs": {}
#     }
#     response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)
#     try:
#         response_data = response.json()
#         output_message = response_data.get("output", "No result field in response")
#         return output_message
#     except ValueError:
#         return "Error: Invalid JSON response"

# # Function to fetch Wikipedia context
# def get_wikipedia_context(query):
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles={query}&exintro=1&explaintext=1"
#     headers = {'User-Agent': user_agent}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         data = response.json()
#         pages = data.get('query', {}).get('pages', {})
#         if pages:
#             page = next(iter(pages.values()))
#             return page.get('extract', 'No content found')
#         else:
#             return 'No content found'
#     else:
#         return 'Failed to retrieve content'

# # Function to convert text to speech
# def text_to_speech(text):
#     tts = gTTS(text=text, lang='en', slow=False)
#     audio_bytes = io.BytesIO()
#     tts.write_to_fp(audio_bytes)
#     audio_bytes.seek(0)
#     return audio_bytes

# # Function to display audio
# def display_audio(audio_bytes):
#     audio_base64 = base64.b64encode(audio_bytes.read()).decode()
#     st.markdown(f'<audio controls src="data:audio/mp3;base64,{audio_base64}"></audio>', unsafe_allow_html=True)

# # Main Client Logic
# def client_main():
#     st.title("LCEL_APEX")
#     st.sidebar.title("Settings")
#     input_method = st.sidebar.radio(
#         "Select input method",
#         ("Type your input manually", "Upload a PDF or Text file"),
#         index=0  # Default is "Type your input manually"
#     )

#     languages = [
#         "Arabic", "Chinese", "Dutch", "English", "French", "German", "Greek", "Hebrew", "Hindi", "Hungarian",
#         "Italian", "Japanese", "Korean", "Latvian", "Lithuanian", "Norwegian", "Persian", "Polish", "Portuguese",
#         "Romanian", "Russian", "Spanish", "Swedish", "Thai", "Turkish", "Ukrainian", "Vietnamese", "Swahili",
#         "Czech", "Slovak", "Bulgarian", "Catalan", "Danish", "Finnish", "Serbian",
#         "Hindi", "Bengali", "Telugu", "Marathi", "Tamil", "Urdu", "Gujarati", "Malayalam", "Kannada", "Odia",
#         "Punjabi", "Assamese", "Maithili", "Sanskrit", "Nepali", "Manipuri", "Konkani", "Sikkimese", "Bodo"
#     ]
#     selected_language = st.selectbox("Select the target language", languages)

#     if input_method == "Type your input manually":
#         input_text = st.text_input("Enter the text you want to convert")
#     else:
#         uploaded_file = st.sidebar.file_uploader("Upload a PDF or Text file", type=["pdf", "txt"])
#         input_text = read_uploaded_file(uploaded_file)
#         if input_text:
#             st.text_area("Content from uploaded file", input_text, height=200)

#     if input_text:
#         with st.spinner('Translation in progress...'):
#             output_message = get_groq_response(input_text, selected_language)
#             st.markdown(f"<div><h4>Translated Text:</h4><p>{output_message}</p></div>", unsafe_allow_html=True)
        
#         with st.spinner('Fetching response from Wikipedia...'):
#             context = get_wikipedia_context(input_text)
#             st.markdown(f"<div><h4>Wikipedia Context:</h4><p>{context}</p></div>", unsafe_allow_html=True)
        
#         if st.button("🔊 Speak Translated Text"):
#             with st.spinner('Converting text to audio...'):
#                 audio_bytes = text_to_speech(output_message)
#                 display_audio(audio_bytes)

# V-3
# import streamlit as st
# import requests
# import PyPDF2
# from gtts import gTTS
# import io
# import base64

# # Main Client Logic
# def client_main():
#     # Apply old app's CSS

#     st.sidebar.title("Settings")
#     input_method = st.sidebar.radio(
#         "Select input method",
#         ("Type your input manually", "Upload a PDF or Text file"),
#         index=0  # Default is "Type your input manually"
#     )

#     languages = [
#         "Arabic", "Chinese", "Dutch", "English", "French", "German", "Greek", "Hebrew", "Hindi", "Hungarian",
#         "Italian", "Japanese", "Korean", "Latvian", "Lithuanian", "Norwegian", "Persian", "Polish", "Portuguese",
#         "Romanian", "Russian", "Spanish", "Swedish", "Thai", "Turkish", "Ukrainian", "Vietnamese", "Swahili",
#         "Czech", "Slovak", "Bulgarian", "Catalan", "Danish", "Finnish", "Serbian",
#         "Hindi", "Bengali", "Telugu", "Marathi", "Tamil", "Urdu", "Gujarati", "Malayalam", "Kannada", "Odia",
#         "Punjabi", "Assamese", "Maithili", "Sanskrit", "Nepali", "Manipuri", "Konkani", "Sikkimese", "Bodo"
#     ]
#     selected_language = st.selectbox("Select the target language", languages)
    
#     if input_method == "Type your input manually":
#         input_text = st.text_input("Enter the text you want to convert")
#     else:
#         uploaded_file = st.sidebar.file_uploader("Upload a PDF or Text file", type=["pdf", "txt"])
#         input_text = read_uploaded_file(uploaded_file)
#         if input_text:
#             st.text_area("Content from uploaded file", input_text, height=200)

#     if input_text:
#         with st.spinner('Translation in progress...'):
#             output_message = get_groq_response(input_text, selected_language)
#             st.markdown(f"<div class='translated-container'><h4>Translated Text:</h4><p>{output_message}</p></div>", unsafe_allow_html=True)
        
#         with st.spinner('Fetching response from Wikipedia...'):
#             context = get_wikipedia_context(input_text)
#             st.markdown(f"<div class='wiki-container'><h4>Wikipedia Context:</h4><p>{context}</p></div>", unsafe_allow_html=True)
        
#         if st.button("🔊 Speak Translated Text"):
#             with st.spinner('Converting text to audio...'):
#                 audio_bytes = text_to_speech(output_message)
#                 display_audio(audio_bytes)

# # Function to read content from uploaded file
# def read_uploaded_file(uploaded_file):
#     if uploaded_file is not None:
#         if uploaded_file.type == "application/pdf":
#             pdf_reader = PyPDF2.PdfReader(uploaded_file)
#             text = ""
#             for page_num in range(len(pdf_reader.pages)):
#                 page = pdf_reader.pages[page_num]
#                 text += page.extract_text()
#             return text
#         elif uploaded_file.type == "text/plain":
#             return uploaded_file.read().decode("utf-8")
#     return ""

# # Function to get response from Groq
# def get_groq_response(input_text, language):
#     json_body = {
#         "input": {
#             "language": language,
#             "text": f"{input_text}"
#         },
#         "config": {},
#         "kwargs": {}
#     }
#     response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)
#     try:
#         response_data = response.json()
#         output_message = response_data.get("output", "No result field in response")
#         return output_message
#     except ValueError:
#         return "Error: Invalid JSON response"

# # Function to fetch Wikipedia context
# def get_wikipedia_context(query):
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles={query}&exintro=1&explaintext=1"
#     headers = {'User-Agent': user_agent}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         data = response.json()
#         pages = data.get('query', {}).get('pages', {})
#         if pages:
#             page = next(iter(pages.values()))
#             return page.get('extract', 'No content found')
#         else:
#             return 'No content found'
#     else:
#         return 'Failed to retrieve content'

# # Function to convert text to speech
# def text_to_speech(text):
#     tts = gTTS(text=text, lang='en', slow=False)
#     audio_bytes = io.BytesIO()
#     tts.write_to_fp(audio_bytes)
#     audio_bytes.seek(0)
#     return audio_bytes

# # Function to display audio
# def display_audio(audio_bytes):
#     audio_base64 = base64.b64encode(audio_bytes.read()).decode()
#     st.markdown(f'<audio controls src="data:audio/mp3;base64,{audio_base64}"></audio>', unsafe_allow_html=True)


# v-4
import streamlit as st
import requests
import PyPDF2
from gtts import gTTS
import io
import base64
from bs4 import BeautifulSoup
# Main Client Logic
def client_main():
    # Apply old app's CSS

    st.sidebar.title("Settings")
    input_method = st.sidebar.radio(
        "Select input method",
        ("Type your input manually", "Upload a PDF or Text file", "Fetch URL's data"),
        index=0  # Default is "Type your input manually"
    )

    languages = [
        "Arabic", "Chinese", "Dutch", "English", "French", "German", "Greek", "Hebrew", "Hindi", "Hungarian",
        "Italian", "Japanese", "Korean", "Latvian", "Lithuanian", "Norwegian", "Persian", "Polish", "Portuguese",
        "Romanian", "Russian", "Spanish", "Swedish", "Thai", "Turkish", "Ukrainian", "Vietnamese", "Swahili",
        "Czech", "Slovak", "Bulgarian", "Catalan", "Danish", "Finnish", "Serbian",
        "Hindi", "Bengali", "Telugu", "Marathi", "Tamil", "Urdu", "Gujarati", "Malayalam", "Kannada", "Odia",
        "Punjabi", "Assamese", "Maithili", "Sanskrit", "Nepali", "Manipuri", "Konkani", "Sikkimese", "Bodo"
    ]
    selected_language = st.selectbox("Select the target language", languages)

    input_text = None  # Initialize input_text to None
    
    if input_method == "Type your input manually":
        input_text = st.text_input("Enter the text you want to convert")
    elif input_method == "Upload a PDF or Text file":
        uploaded_file = st.sidebar.file_uploader("Upload a PDF or Text file", type=["pdf", "txt"])
        input_text = read_uploaded_file(uploaded_file)
        if input_text:
            st.text_area("Content from uploaded file", input_text, height=200)
    elif input_method == "Fetch URL's data":
        url = st.text_input("Enter the URL to fetch and translate")
        if url:
            input_text = fetch_url_data(url)
            if input_text:
                st.text_area("Content from the URL", input_text, height=200)
    if st.button("Translate"):
        if input_text:
            with st.spinner('Translation in progress...'):
                output_message = get_groq_response(input_text, selected_language)
                st.markdown(f"<div class='translated-container'><h4>Translated Text:</h4><p>{output_message}</p></div>", unsafe_allow_html=True)
            
            with st.spinner('Fetching response from Wikipedia...'):
                context = get_wikipedia_context(input_text)
                st.markdown(f"<div class='wiki-container'><h4>Wikipedia Context:</h4><p>{context}</p></div>", unsafe_allow_html=True)
            
            if st.button("🔊 Speak Translated Text"):
                with st.spinner('Converting text to audio...'):
                    audio_bytes = text_to_speech(output_message)
                    display_audio(audio_bytes)

# Function to read content from uploaded file
def read_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
            return text
        elif uploaded_file.type == "text/plain":
            return uploaded_file.read().decode("utf-8")
    return ""

# Function to fetch data from a URL
def fetch_url_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            text_content = soup.get_text(separator='\n')  # Extract text content
            return text_content.strip()  # Remove leading/trailing whitespace
        else:
            return "Failed to retrieve content from the URL."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    
    
    
# Function to get response from Groq
def get_groq_response(input_text, language):
    json_body = {
        "input": {
            "language": language,
            "text": f"{input_text}"
        },
        "config": {},
        "kwargs": {}
    }
    response = requests.post("https://verbo-if1h.onrender.com:8000/chain/invoke", json=json_body)
    try:
        response_data = response.json()
        output_message = response_data.get("output", "No result field in response")
        return output_message
    except ValueError:
        return "Error: Invalid JSON response"

# Function to fetch Wikipedia context
def get_wikipedia_context(query):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles={query}&exintro=1&explaintext=1"
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        pages = data.get('query', {}).get('pages', {})
        if pages:
            page = next(iter(pages.values()))
            return page.get('extract', 'No content found')
        else:
            return 'No content found'
    else:
        return 'Failed to retrieve content'

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text=text, lang='en', slow=False)
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes

# Function to display audio
def display_audio(audio_bytes):
    audio_base64 = base64.b64encode(audio_bytes.read()).decode()
    st.markdown(f'<audio controls src="data:audio/mp3;base64,{audio_base64}"></audio>', unsafe_allow_html=True)

