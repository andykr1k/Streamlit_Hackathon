from io import StringIO
import streamlit as st

def FilesToMessages(files):
    messages = []
    for file in files:
        name = "File Name: " + file.name + "\n"
        data = str(file.read()).replace('\\n','\n')
        content = "File Content: \n" + data
        messages.append(name + content)
    return messages