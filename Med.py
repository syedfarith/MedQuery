import streamlit as st
from medical_keywords import medical_keywords  # Ensure you have this module
import google.generativeai as genai

# Configure the Gemini API with your API key
genai.configure(api_key="AIzaSyAYkNollmdlQoIQeUoNVeYUcJ6rIwDDsow")

# Define the generation configuration and safety settings
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

# Function to validate if a query is medical-related
def is_medical_query(query):
    return any(keyword in query.lower() for keyword in medical_keywords)

# Streamlit app layout
st.set_page_config(page_title="MedQuery", layout="centered")
st.title('MedQuery')

query = st.text_input("Ask a medical-related query:")

if is_medical_query(query):
    with st.spinner('Generating response...'):
        # Create a new chat session and send the query
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(query)
        
        st.write(response.text)
else:
    st.warning("Please enter a medical-related query.")

# Center-align the input text
st.write("""
<style>
.stTextInput > div > input {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)
