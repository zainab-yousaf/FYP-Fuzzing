import subprocess # library used to interact with command line
import os
from graphviz import Source

# slither proxy class for grnrrating the call graph
class SlitherProxy:
    def __init__(self):
        self.current_dir = os.getcwd()
        self.output_folder = self.current_dir

    def genCallGraph(self, contractName):
        try:
            subprocess.run(['slither', contractName, '--print', 'call-graph'])
            call_graph_filename = f'{contractName}.all_contracts.call-graph.dot'
            call_graph_path = os.path.join(self.output_folder, call_graph_filename)

            if os.path.exists(call_graph_path):
                call_graph_png_path = os.path.join(self.output_folder, f'{contractName}.all_contracts.call-graph.dot.png')
                graph_source = Source.from_file(call_graph_path, format="png")
                graph_source.render(view=False)  # Optional: Open the PNG file after rendering
                print(f"Call Graph saved to: {call_graph_path}")
                return call_graph_png_path
            else:
                print("Error: Call graph file not created.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing Slither: {e}")
    #def highlightCallGraph(self, contractName):
    def genListOf_VarFun(self, contractName):
    # command to generate list of state variables and functions
        subprocess.run(['slither', contractName, '--print', 'vars-and-auth'])
    # result = subprocess.run(['slither', contractPath, '--print', 'vars-and-auth']
    #                         , shell=True, capture_output=True)
    # # Access the output
    # output = result.stdout
    # return output




