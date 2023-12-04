import subprocess
import os
import shutil

class FoundryProxy:

    def flatten(self,contractPath):
        print("Flattening Started")
        # Command to execute
        command = "forge flatten " + contractPath
        # Execute the command using subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        # Access the output
        output = result.stdout
        print("Flattening Ended")
        return output

    def check_directory_existence(self,directory_path):
        if os.path.isdir(directory_path):
            return True
        else:
            return False

    def runSubProcess(self,cmd, base_directory):
        try:
            # Run the command
            subprocess.run(cmd, shell=True, check=True, cwd=base_directory)
            print(f"Command '{cmd}' executed successfully in {base_directory}.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    """ For Creating Foundry Project"""
    def createFoundry(self):
        current_dir = os.getcwd()
        self.runSubProcess("forge init FoundryProject --force", current_dir)


