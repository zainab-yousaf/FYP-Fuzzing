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


###########################################################################################
def change_to_foundry_src():
    current_dir = os.getcwd()
    base_directory = f'{current_dir}/FoundryProject/src'
    print("CWD: ", base_directory)
    # Change the current working directory
    os.chdir(base_directory)

if __name__ == "__main__":
    foundryobj=foundry.FoundryProxy()
    auditorobj=Auditor.Auditor()

    st.title("FuzzBee 🐝")
    session_state = st.session_state
    session_state.file_status = getattr(session_state,"file_status",False)
    

    os.chdir("/home/khansa/Desktop/FuzzBee")
    print("current directory: ", os.getcwd())

    sideBar()
    # creating foundry project
    if not session_state.file_status:
        foundryobj.createFoundry()
    # Input files
    auditorobj.input_files(session_state)

    # When files are uploaded 
    if session_state.file_status:
        contractName = st.text_input("Enter contract name", value="UnstoppableLender.sol")
        contractPath = f'FoundryProject/src/{contractName}'
        
        #change path to foundry source folder
        change_to_foundry_src()

    # Flatten module
    if st.button("Flatten Smart Contract"):
        # Flatten the smart contract
        outputFlatten = foundryobj.flatten(contractName)
        st.text_area("Flattened Smart contract:", outputFlatten, height=600)
            


     