import streamlit as st


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
     st.title("FuzzBee 🐝")
     sideBar()