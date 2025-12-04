import os  

import streamlit as st  
from dotenv import load_dotenv 
import google.generativeai as gen_ai 

# load environment variable 

load_dotenv() 

# configuration streamlit page settings 

st.set_page_config(
    page_title ="My Chat Bot" ,
    page_icon =":brain:", 
    layout ="centered"
)

GOOGLE_API_KEY =os.getenv("GOOGLE_API_KEY") 

# set up google Gemini_pro AI Model 