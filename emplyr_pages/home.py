import requests
import streamlit as st


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def display_home(name):
    st.header(f"Welcome {name} 😊😊")
    st.header("Need staff? ")
    st.header("Get local applicants fast.")
    