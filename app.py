
import streamlit as st

import os

from dotenv import load_dotenv, find_dotenv

# load env vars from .env file
load_dotenv(find_dotenv())

# retrieve access password (opt: add a login)
app_password = os.environ.get("APP_PASSWORD")

# ask for password
password = st.text_input("Enter a password", type="password")
if password == app_password:

    "your're in 🎉"

    # content of the page

else:

    "nope ❌"
