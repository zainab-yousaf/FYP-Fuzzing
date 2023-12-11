import streamlit as st
import os
import foundry
import Auditor
import slither
from PIL import Image

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
    slitherobj=slither.SlitherProxy()

    st.title("FuzzBee 🐝")
    session_state = st.session_state
    session_state.file_status = getattr(session_state,"file_status",False)
    

    os.chdir("/Users/muaazzz/Desktop/Fuzzing Github/FYP-Fuzzing")
    print("current directory: ", os.getcwd())

    sideBar()
    # creating foundry project
    if not session_state.file_status:
        foundryobj.createFoundry()
    # Input files
    auditorobj.input_files(session_state)

    # When files are uploaded 
    if session_state.file_status:
        contractName = st.text_input("Enter contract name", value=".sol")
        contractPath = f'FoundryProject/src/{contractName}'
        
        #change path to foundry source folder
        change_to_foundry_src()

    # Flatten module
    if st.button("Flatten Smart Contract"):
        # Flatten the smart contract
        outputFlatten = foundryobj.flatten(contractName)
        st.text_area("Flattened Smart contract:", outputFlatten, height=600)
    
    #Generate Call Graph
    if st.button("Generate Call graphs"):
            # Generating Call graphs of smart contract
            call_graph_png_path=slitherobj.genCallGraph(contractName)
            print("png file path",call_graph_png_path)
            if os.path.exists(call_graph_png_path):
                #display callgraph image on the screen
                st.title("Call Graph Visualization")
                
                # Display the image
                image = Image.open(call_graph_png_path)
                st.image(image, caption='Call Graph', use_column_width=True)
                
            else:
                #display error in case file not found
                st.error("Error: Call graph PNG file not found.")
 
    if st.button("Generate list of state vars and functions"):
            # command to generate list of state variables and functions
            outputVarFun = slitherobj.genListOf_VarFun(contractName)    
            output_file_path = '/Users/muaazzz/Desktop/Fuzzing Github/FYP-Fuzzing/FoundryProject/src/output.txt'
            with open(output_file_path, 'r') as file:
                output_content = file.read()
            st.text_area("List of State Variables:", output_content, height=600)
            # st.text_area("List of Variables and Functions in smart contract:", outputVarFun, height=600)

    '''if st.button("View List of State Variables"):
            # command to generate list of state variables and functions
            output_file_path = '/Users/muaazzz/Desktop/Fuzzing Github/FYP-Fuzzing/FoundryProject/src/output.txt'
            outputList = slitherobj.get_state_variables(output_file_path)    
            with open(output_file_path, 'r') as file:
                output_content = file.read()
            st.text_area("List of State Variables:", output_content, height=600)'''
    #if st.button("View List of State Variables"):
    # command to generate list of state variables and functions
    output_file_path = '/Users/muaazzz/Desktop/Fuzzing Github/FYP-Fuzzing/FoundryProject/src/output.txt'
    state_variables_list = slitherobj.get_state_variables(output_file_path)

        # Display dropdown list
    selected_variable = st.selectbox("Select State Variable:", state_variables_list)
    st.session_state.selected_variable = selected_variable
    st.text_area("Selected Variable:", st.session_state.selected_variable)

    
        # Display information for the selected state variable
        


     