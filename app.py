import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
from pages.post_add import post_add, post_submit
from pages.view_jobs import display_view_posts
from pages.home import display_home
from yaml.loader import SafeLoader
import yaml
import json

with open('./creds.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def load_from_json(fname):
    f = open(fname)
    a = json.load(f)
    f.close()
    return a


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


st.write(
    '<style>div.block-container{padding-top:1px;}</style>', unsafe_allow_html=True)

st.header("22dollars.com.au")

local_css("design.css")

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    MENU = option_menu(None, ["Home", "New Job", "View Jobs", 'Settings'],
                       icons=['house', 'cloud-upload', "list-task", 'gear'],
                       menu_icon="cast", default_index=0, orientation="horizontal")
    # -------------------------------------------------------------------------------------------------------------------------------
    if MENU == "New Job":
        post_job_object = post_add()
        if post_job_object[1]:
            post_submit(post_job_object[0])

    if MENU == "View Jobs":
        a = load_from_json("posts.json")
        display_view_posts(a)
        st.balloons()

    if MENU == "Home":
        display_home(name)

    if MENU == "Settings":
        authenticator.logout('Logout', 'main')

#--------------------------------------------------------------------------------------------------------------------------------#
elif authentication_status is False:
    st.error('Username or password is incorrect')

elif authentication_status is None:
    st.warning('Please enter your username and password')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
