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

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.split_map(
            left_layer='ESA WorldCover 2020', right_layer='ESA WorldCover 2021'
        )
        m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')

m.to_streamlit(height=700)
