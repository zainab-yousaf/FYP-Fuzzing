import streamlit as st
import os
import foundry
import Auditor


def sideBar():
    with st.sidebar:
        st.title("FuzzBee 🐝")
        st.markdown("---")
        st.markdown(
            "## How to use\n"
            "1. Upload Smart contract files 📄\n"
            "2. Provide Foundry Properties for the provided contract 📝\n"
        )


if __name__ == "__main__":
    foundryobj=foundry.FoundryProxy()
    auditorobj=Auditor.Auditor()

    st.title("FuzzBee 🐝")
    session_state = st.session_state
    session_state.file_status = getattr(session_state,"file_status",False)
    
    print("current directory: ", os.getcwd())

    sideBar()
    # creating foundry project
    if not session_state.file_status:
        foundryobj.createFoundry()
    # Input files
    auditorobj.input_files(session_state)


     