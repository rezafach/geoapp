import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Reza Fachrizal: rfachrizal@hotmail.com
    [GitHub](https://github.com/rezafach) | [Linkedin](https://www.linkedin.com/in/rfachrizal/) | [Website](https://rezaf.notion.site/Reza-Fachrizal-s-Portfolio-624494e94d79428492954fd32f08e3cc)
    """
)

st.title("Fairatmos Assesment 🌳")

st.markdown(
    """
    Hello, I'm Reza, and I'd like to share my assessment on crafting a front-end web application. In this evaluation, I explore the crucial elements of creating 
    an engaging and user-friendly interface. From responsive design to seamless navigation, I delve into the nuances that make a web application stand out.
    This multi-page web app demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and open-source mapping libraries [leafmap](https://leafmap.org)    .
    """
)

st.info("Click on the left sidebar menu to navigate to the apps.")


