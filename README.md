# Model Context Protocol (MCP)

### Prerequisites

You will need the local LLM ollama
```
brew install ollama
ollama pull llama3.2:1b
ollama pull llama3.2:3b
```

You can also use other LLMs for this repository, like the ones from Groq
> [Groq API Key](https://console.groq.com/playground) can be generated and used free of charge

## Environment

### **`macOS`** type the following commands :


- Install the virtual environment and the required packages by following commands:

    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
### **`WindowsOS`** type the following commands :

- Install the virtual environment and the required packages by following commands.

   For `PowerShell` CLI :

    ```PowerShell
    pyenv local 3.11.3
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-Bash` CLI :
    ```
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/Scripts/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

---