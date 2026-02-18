import sys
import subprocess
import os
from io import StringIO
from mcp.server.fastmcp import FastMCP
from duckduckgo_search import DDGS


mcp: FastMCP = FastMCP("SuperServer")

@mcp.tool()
def search_web(query: str) -> str:
    """Searches the web for current information using DuckDuckGo."""
    print(f"DEBUG: Searching web for {query}") # FastMCP redirects prints safely
    with DDGS() as ddgs:
        results = [r['body'] for r in ddgs.text(query, max_results=3)]
        return "\n---\n".join(results) if results else "No results found."

@mcp.tool()
def read_local_file(file_path: str) -> str:
    """Reads the content of a local text file. Provide the full path."""
    if not os.path.exists(file_path):
        return f"Error: File at {file_path} not found."
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"


# @mcp.tool()
# def execute_python_code(code: str) -> str:
#     """
#     Executes Python code. 
#     If 'code' is a filename (e.g. 'fibonacci.py'), it runs that file.
#     Otherwise, it executes the string as Python code.
#     """
#     scripts_dir = os.path.abspath("scripts")
    
#     # 1. Check if the LLM passed a filename that exists in our scripts folder
#     potential_file_path = os.path.join(scripts_dir, code.strip())
    
#     # Setup environment
#     env = os.environ.copy()
#     env["PYTHONPATH"] = scripts_dir

#     try:
#         if code.strip().endswith(".py") and os.path.exists(potential_file_path):
#             # CASE A: Run the actual file
#             print(f"🚀 Running script file: {potential_file_path}")
#             command = [sys.executable, potential_file_path]
#         else:
#             # CASE B: Execute as code string (using -c)
#             print(f"💻 Executing code string...")
#             command = [sys.executable, "-c", code]

#         result = subprocess.run(
#             command,
#             capture_output=True,
#             text=True,
#             timeout=10,
#             cwd=scripts_dir,
#             env=env 
#         )
        
#         if result.stderr:
#             return f"Execution Error:\n{result.stderr}"
#         return f"Output:\n{result.stdout}" if result.stdout else "Success (No output)."
        
#     except Exception as e:
#         return f"Error: {str(e)}"    
    
if __name__ == "__main__":
    mcp.run()