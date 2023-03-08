import requests
import streamlit as st
from streamlit_lottie import st_lottie


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def display_home(name):
    lottie_url_hello = "https://assets8.lottiefiles.com/packages/lf20_EOzPAenKJ6.json"
    lottie_hello = load_lottieurl(lottie_url_hello)
    st.header(f"Welcome {name} 😊😊")
    st_lottie(lottie_hello, key="hello",speed=1.2,height=300,width=700)

