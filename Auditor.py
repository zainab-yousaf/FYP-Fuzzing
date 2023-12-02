import streamlit as st
import os

class Auditor:
    def input_files(self,session_state):
        # Solidity Files Input
        uploaded_files = st.file_uploader('Choose your .sol files', type="sol", accept_multiple_files=True)

        # Add files to src
        upload_folder = "FoundryProject/src/"

        # Check if files are uploaded
        if uploaded_files:
            for file in uploaded_files:
                # Save the files to the upload folder
                file_path = os.path.join(upload_folder, file.name)
                with open(file_path, 'wb') as f:
                    f.write(file.read())

            print(f"Files successfully uploaded to {upload_folder}")
            session_state['file_status'] = True
            return True
        else:
            st.warning("No files uploaded.")