import streamlit as st

st.set_page_config(page_title="Abou us Page",
                   layout='wide',
                   page_icon='./images/about_icon.png')
st.title('About Us')
st.subheader("Names : ")
st.markdown(
    ' 1. Sakshi Salve (CS4171) BTech A \n'
     '2. Soummya Panse (CS4217) BTech B\n'
     '3. Aishwarya Ghadmode (CS4228) BTech B\n'
     , unsafe_allow_html=True
    )

