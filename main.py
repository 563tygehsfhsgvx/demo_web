import streamlit as st



st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

with st.container():
 st.subheader("Hi, I am Sahil :wave:")
 st.title("Build a Website")
 st.write("Follow these are the Steps.")


with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("How To Do!")
    st.write("##")
    st.write("Step 1: Get a domain name and URL. It's important to choose a good domain name.")
    st.write("Step 2: Set up an email address to match your domain name.")
    st.write("Step 3: Find a web hosting company.")
    st.write("Step 4: Design your website.")
    st.write("Step 5: Build your website.")
    st.write("Step 6: Add and manage your website content.")
    st.write("Step 7: Publish your website.")

("Also Visit Sister Channel Click in below")
st.write("[Youtube Channel >](https://www.youtube.com/@BestGirlVlog)")






