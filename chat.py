import streamlit as st
from duckduckgo_search import DDGS
from medical_keywords import medical_keywords 

# Function to search queries
def search_query(query, max_results=5):
    results = DDGS().text(query, max_results=max_results)
    out = []
    for i in range(0, max_results):
        out.append(results[i]['body'])
    return ". ".join(out)

# Function to validate if a query is medical-related
def is_medical_query(query):
    return any(keyword in query.lower() for keyword in medical_keywords)

# Set up the Streamlit app layout
st.set_page_config(page_title="MedQuery", layout="centered")
st.title('MedQuery')


query = st.text_input("Ask a medical related query:")

if is_medical_query(query):
    with st.spinner('Generating...'):
        output = search_query(query)
        st.write(output)
else:
    st.warning("Please enter a medical-related query.")

st.write("""
<style>
.stTextInput > div > input {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)
