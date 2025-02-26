import streamlit as st
import pandas as pd
import os
import openpyxl
from io import BytesIO
print(openpyxl.__version__)
st.set_page_config(page_title="Growth Mindset",page_icon="🌼")

# custom css

st.markdown(
    """
    <style>
    .stApp{
       background-color:#CCCCFF;
       color:white;
          }
          </style>
          """,
          unsafe_allow_html=True
)

# tittle and description
st.title("Growth mindset challenge with Streamlit 😊💛")
st.write("Belief that abilities and intelligence can be developed through **hard work, perseverance, and learning from mistakes.**")

st.header("Today's qoutes🧠")
st.write("You don't have to be great to start, but you have to start to be great.🕊️")


# Changllenge
st.header("💭What is your Chanllenge today ?")
user_input=st.text_input("Enter Your chanllenge")

if user_input:
    st.success(f" Focus on developing **{user_input}** and understanding concepts, not just grades.")
else:
    st.warning("Tell us about your chanllenge🤔?")    


# goals
st.header("Tell about your goals🎓")
goals=st.text_input("Enter your goals") 

if goals:
    st.success(f"Amazing! **{goals}**😇")
else:
    st.warning("Keep working untill you archive it....")


# Acheivements
st.header('Tell about Your wins🏆')
acheivement=  st.text_input('Enter your wins ')

if acheivement:
    st.success(f"Great! Your are achieved **{acheivement}**")
else:
    st.info('Share your achievement now 🤩')


# footer
st.write('--------------------------------------------------------------')
st.write("Embrace your potential and never stop striving to grow and succeed.✨🎓")

     
