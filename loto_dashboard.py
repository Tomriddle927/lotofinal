
import streamlit as st
import pandas as pd
import numpy as np
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

st.set_page_config(page_title="Lebanese Loto Dashboard", layout="wide")

# Load config.yaml
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    credentials=config['credentials'],
    cookie_name=config['cookie']['name'],
    key=config['cookie']['key'],
    expiry_days=config['cookie']['expiry_days'],
    preauthorized=config['preauthorized']
)

name, authentication_status, username = authenticator.login("Login", location="main")

if authentication_status:
    st.sidebar.success(f"Welcome {name}")
    st.title("Lebanese Loto Prediction Dashboard")
    st.write("Upload historical draw data and generate predictions here.")
elif authentication_status is False:
    st.error("Username or password is incorrect")
elif authentication_status is None:
    st.warning("Please enter your username and password")
