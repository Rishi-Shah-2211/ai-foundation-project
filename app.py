import streamlit as st

st.title("AI Engineer Foundation 🚀")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome to your AI journey, {name}!")