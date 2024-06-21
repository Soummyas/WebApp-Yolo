import streamlit as st
import base64
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app

#Layout and Configurations
st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home_icon.png')
st.title('YOLOv5 Fish Detection App')
st.caption('Please uses side bar to navigate')
# - with space will give html like ul of circle
#link in the existing page syntax :  [click able text](/page name where we want to direct/)
st.markdown("""
### App detects  fishes
- Automatically detect fishes      
- [Click here to detect from image](/Image/)\n\n
- Currently we are detecting :
 """)

st.markdown(
    '1. <a href="https://en.wikipedia.org/wiki/Goldfish" target="_self"> Gold Fish</a>\n'
     '1. <a href="#" target="_self"> Silver Carp</a> (Comming soon)\n'
     '1. <a href="#" target="_self"> Catfish</a> (Comming soon)\n'
     , unsafe_allow_html=True
    )


