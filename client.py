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
# from bs4 import BeautifulSoup

# # Main Client Logic
# def client_main():
#     # Apply old app's CSS

#     st.sidebar.title("Settings")
#     input_method = st.sidebar.radio(
#         "Select input method",
#         ("Type your input manually", "Upload a PDF or Text file", "Add URL"),
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
#     elif input_method == "Upload a PDF or Text file":
#         uploaded_file = st.sidebar.file_uploader("Upload a PDF or Text file", type=["pdf", "txt"])
#         input_text = read_uploaded_file(uploaded_file)
#         if input_text:
#             st.text_area("Content from uploaded file", input_text, height=200)
#     elif input_method=="Add URL":
#         input_text = st.text_input("Enter the URL to fetch and translate")
#         if input_text:
#             input_text = fetch_url_data(input_text)
#             if input_text:
#                 st.text_area("Content from the URL", input_text, height=200)

#     if st.button("Translate"):
#         if input_text:
#             with st.spinner('Translation in progress...'):
#                 output_message = get_groq_response(input_text, selected_language)
#                 st.markdown(f"<div class='translated-container'><h4>Translated Text:</h4><p>{output_message}</p></div>", unsafe_allow_html=True)
            
#             col1, col2, col3, col4, col5, col6,col7,col8,col9,col10 = st.columns(10)
            
#             with col1:   
#                 if st.button("🔊"):
#                     with st.spinner('Converting text to audio...'):
#                         audio_bytes = text_to_speech(output_message)
#                         display_audio(audio_bytes)
                        
#             with col2:
#                 if st.button("Wiki"):
#                     with st.spinner('Fetching response from Wikipedia...'):
#                         context = get_wikipedia_context(input_text)
#                         st.markdown(f"<div class='wiki-container'><h4>Wikipedia Context:</h4><p>{context}</p></div>", unsafe_allow_html=True)
            
            

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


# def fetch_url_data(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.content, 'html.parser')
#             text_content = soup.get_text(separator='\n')  # Extract text content
#             return text_content.strip()  # Remove leading/trailing whitespace
#         else:
#             return "Failed to retrieve content from the URL."
#     except requests.exceptions.RequestException as e:
#         return f"An error occurred: {e}"

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
#     response = requests.post("https://verbo-if1h.onrender.com/chain/invoke", json=json_body)
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

# V-4
import streamlit as st
import requests
import PyPDF2
import fitz  # PyMuPDF
from gtts import gTTS
import io
import base64
from bs4 import BeautifulSoup
from streamlit_quill import st_quill

# Function to display PDF as images
def render_pdf_to_html(uploaded_file):
    import fitz  # PyMuPDF

    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    html_content = ""
    list_open = False  # Track if a list is currently open (ul or ol)

    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        # Go through each block to build the HTML structure
        for block in blocks:
            if "lines" in block:
                # Determine alignment based on the block position
                block_bbox = block['bbox']
                block_x0 = block_bbox[0]  # Left coordinate
                block_x1 = block_bbox[2]  # Right coordinate
                page_width = page.rect.width

                # Infer alignment from the block's x-coordinates
                alignment = "left"
                if block_x0 < 50 and block_x1 > (page_width - 50):
                    alignment = "justify"
                elif block_x0 > (page_width / 2):
                    alignment = "right"
                elif abs(block_x0 - (page_width / 2)) < 50:
                    alignment = "center"

                # Add the div with alignment styling
                html_content += f"<div style='text-align: {alignment}; margin-bottom:10px;'>"

                current_list_type = None  # Track if it's an ordered or unordered list

                for line in block["lines"]:
                    line_text = "".join([span["text"] for span in line["spans"]]).strip()

                    # Detect if the line is part of a list
                    if line_text.startswith("- ") or line_text.startswith("• "):  # Unordered list
                        if not list_open:  # Open the list if it's not already open
                            current_list_type = "ul"
                            html_content += "<ul>"
                            list_open = True
                        html_content += "<li>"
                    elif len(line_text) > 1 and line_text[0].isdigit() and line_text[1] in ('.', ')'):  # Ordered list
                        if not list_open:
                            current_list_type = "ol"
                            html_content += "<ol>"
                            list_open = True
                        html_content += "<li>"
                    else:
                        if list_open:  # Close any open list if the current line is not part of a list
                            html_content += f"</{current_list_type}>"
                            list_open = False
                        html_content += "<br>"

                    # Process each span for formatting (bold, italic, underline)
                    for span in line["spans"]:
                        span_content = span["text"]
                        font_name = span["font"]  # Get the font name

                        # Apply formatting tags: <b>, <i>, <u>
                        if "Bold" in font_name:  # Check if the font indicates bold
                            span_content = f"<b>{span_content}</b>"

                        if "Italic" in font_name or "Oblique" in font_name:  # Check if the font indicates italic
                            span_content = f"<i>{span_content}</i>"

                        if span["flags"] & 4:  # Check if the underline flag is set
                            span_content = f"<u>{span_content}</u>"

                        # Add the formatted span to the HTML content
                        html_content += span_content

                    if list_open:
                        html_content += "</li>"  # Close the list item

                html_content += "</div>"  # Close block div

        # Ensure any open list is closed at the end of the page
        if list_open:
            html_content += f"</{current_list_type}>"
            list_open = False

    return html_content

# def render_pdf_to_html(uploaded_file):
#     import fitz  # PyMuPDF

#     pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
#     html_content = ""

#     for page_num in range(len(pdf_document)):
#         page = pdf_document.load_page(page_num)
#         blocks = page.get_text("dict")["blocks"]

#         for block in blocks:
#             if "lines" in block:
#                 html_content += "<div style='margin-bottom:10px;'>"

#                 for line in block["lines"]:
#                     for span in line["spans"]:
#                         span_content = span["text"]
#                         font_name = span["font"]  # Get the font name

#                         # Check if the font is bold by inspecting the font name
#                         if "Bold" in font_name:
#                             span_content = f"<b>{span_content}</b>"

#                         # Check if the font is italic by inspecting the font name
#                         if "Italic" in font_name or "Oblique" in font_name:
#                             span_content = f"<i>{span_content}</i>"

#                         # Check if the text is underlined using flags (underline is usually handled by flags)
#                         if span["flags"] & 4:
#                             span_content = f"<u>{span_content}</u>"

#                         # Add the formatted span content
#                         html_content += span_content

#                 html_content += "</div>"

#     return html_content


# Function to generate a Markdown file content
def generate_markdown_content(translated_text):
    markdown_content = f"# Translated Content\n\n{translated_text}"
    return markdown_content

# Function to create a downloadable Markdown file
def create_download_button(translated_text):
    markdown_content = generate_markdown_content(translated_text)
    markdown_bytes = markdown_content.encode('utf-8')
    st.download_button(
        label="Download Translated Content as Markdown",
        data=markdown_bytes,
        file_name="translated_content.md",
        mime="text/markdown"
    )
    
def display_pdf_as_images(uploaded_file):
    if uploaded_file is not None:
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        images = []
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap()
            img_data = pix.tobytes("png")
            images.append(img_data)
        
        for img in images:
            st.image(img)
            
# Main Client Logic
def client_main():
    st.sidebar.title("Settings")
    input_method = st.sidebar.radio(
        "Select input method",
        ("Type your input manually", "Upload a PDF or Text file", "Add URL"),
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

    # Initialize session state variables
    if "input_text" not in st.session_state:
        st.session_state.input_text = ""
    if "output_message" not in st.session_state:
        st.session_state.output_message = ""

    if input_method == "Type your input manually":
        st.session_state.input_text = st.text_input("Enter the text you want to convert", st.session_state.input_text)
    elif input_method == "Upload a PDF or Text file":
        uploaded_file = st.sidebar.file_uploader("Upload a PDF or Text file", type=["pdf", "txt"])

        if uploaded_file is not None:
            view_method = st.sidebar.radio(
                "View Content",
                ("View PDF as Images", "View PDF in Non-Editable Editor", "Edit PDF Content in Editor"),
                index=0  # Default is "Type your input manually"
            )

            if view_method == "View PDF as Images" and uploaded_file.type == "application/pdf":
                display_pdf_as_images(uploaded_file)  # Display the PDF as images

            if view_method == "View PDF in Non-Editable Editor" and uploaded_file.type == "application/pdf":
                html_content = render_pdf_to_html(uploaded_file)
                # Display the content in a read-only Quill editor
                st_quill(value=html_content, readonly=True)

            if view_method == "Edit PDF Content in Editor" and uploaded_file.type == "application/pdf":
                html_content = render_pdf_to_html(uploaded_file)
                # Display the text in Quill editor for editing
                edited_text = st_quill(value=html_content)
                create_html_download_button(html_content)
                st.session_state.input_text = edited_text
                # quill_editor(initial_content=html_content)

            if st.session_state.input_text:
                st.text_area("Content from uploaded file", st.session_state.input_text, height=200)
    elif input_method == "Add URL":
        url_input = st.text_input("Enter the URL to fetch and translate")
        if url_input:
            st.session_state.input_text = fetch_url_data(url_input)
        if st.session_state.input_text:
            st.text_area("Content from the URL", st.session_state.input_text, height=200)

    if st.button("Translate"):
        if st.session_state.input_text:
            with st.spinner('Translation in progress...'):
                st.session_state.output_message = get_groq_response(st.session_state.input_text, selected_language)

    # Display the translated text
    if st.session_state.output_message:
        st.markdown(f"<div class='translated-container'><h4>Translated Text:</h4><p>{st.session_state.output_message}</p></div>", unsafe_allow_html=True)
        
        # Provide download button for the translated content
        create_download_button(st.session_state.output_message)

    col1, col2 = st.columns(2)
    
    with col1:   
        if st.button("🔊"):
            if st.session_state.output_message:
                with st.spinner('Converting text to audio...'):
                    audio_bytes = text_to_speech(st.session_state.output_message)
                    display_audio(audio_bytes)
                
    with col2:
        if st.button("Wiki"):
            if st.session_state.input_text:
                with st.spinner('Fetching response from Wikipedia...'):
                    context = get_wikipedia_context(st.session_state.input_text)
                    st.markdown(f"<div class='wiki-container'><h4>Wikipedia Context:</h4><p>{context}</p></div>", unsafe_allow_html=True)
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
    response = requests.post("https://verbo-if1h.onrender.com/chain/invoke", json=json_body)
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


def create_html_download_button(html_content):
    html_bytes = html_content.encode('utf-8')
    st.download_button(
        label="Download as HTML",
        data=html_bytes,
        file_name="content.html",
        mime="text/html"
    )
