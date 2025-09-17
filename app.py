# Importing Required Packages
import streamlit as st
import time
from utils import get_text_chunks, get_vector_store
from rag_backend import get_answer

# Set the Streamlit Page Configuration
st.set_page_config(page_title = "RAG ChatBot", layout = "wide")

# The UI Web Interface Elements
st.title("RAG ChatBot from Documents")
st.write("Ask a question from the data and get answer")

# Use cache to cache the expensive data loading and vector store creation
@st.cache_resource(show_spinner = False)
def setup_rag():
    with st.spinner("Loading documents and building knowldge base...."):
        text_chunks = get_text_chunks(r"C:\Users\Webbies\Jupyter_Notebooks\RAG_ChatBot\textdata")
        vector_store = get_vector_store(text_chunks)
    return vector_store

# Initialize the RAG components
vector_store = setup_rag()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input and Chat Logic
if prompt := st.chat_input("Ask a question..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response with delayed log messages
    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        # Simulating the delayed log messages
        message_placeholder.markdown("Thinking....")
        time.sleep(2)

        message_placeholder.markdown("Processing Documents...")
        time.sleep(2)

        message_placeholder.markdown("Retrieving context....")
        time.sleep(2)

        # Get the answer from backend
        full_response = get_answer(prompt, vector_store)

        # Display the Final Answer
        message_placeholder.markdown(full_response)
    
    # Adding assistant response to chat histoty
    st.session_state.messages.append({"role": "assistant", "content": full_response})