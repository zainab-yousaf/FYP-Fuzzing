import subprocess

class Foundry:
    def flatten(contractPath):
        print("Flattening Started")
        # Command to execute
        command = "forge flatten "+ contractPath
        # Execute the command using subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        # Access the output
        output = result.stdout
        print("Flattening Ended")
        return output