import streamlit as st
import requests

st.title("FastAPI + Streamlit Demo")

# Button to call API
if st.button("Get Message from Backend"):
    try:
        response = requests.get("http://127.0.0.1:8000/")
        data = response.json()
        st.success(data["message"])
    except Exception as e:
        st.error(f"Error: {e}")