import streamlit as st
from transcribe import TranscribeSpeechToText
from llm import llm
from tools import FilesToMessages

hide_streamlit_style = """
<style>
MainMenu {visibility: hidden;}
</style>
"""

ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
    position: relative;
    min-height: 0vh;
}

footer{
    visibility:hidden;
}

.footer {
position: fixed;
display: flex;
justify-items: center;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/>&nbsp;by <a style='display: inline; text-align: left;' href="https://github.com/andykr1k" target="_blank">Andrew Krikorian</a></p>
</div>

</div>
"""

def header():
    st.set_page_config(page_title="ComposeAI", layout="wide", page_icon='📄')
    st.header("📄 ComposeAI")
    st.caption("Generate a readme in seconds!")
    return

def sidebar():
    return

def footer():
    st.write(ft, unsafe_allow_html=True)
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    return

def body():
    files = st.file_uploader("Upload Project", accept_multiple_files=True)

    if files != None:
        if st.button("Generate Docs"):
            llm(FilesToMessages(files))

    return