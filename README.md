> [!WARNING]
> Do not try to use this in a production environment.
>
> It does not have all the security and safety features that a production AI agent would have. It is for learning purposes only.

### Prerequisites

* **Python 3.x**: Ensure you have a compatible version of Python installed (e.g., Python 3.9+).
* **`uv` (or `pip`)**: The project uses `uv` for dependency management and running, which is a fast Python package installer and resolver. You can install it via `pip`:
    ```bash
    pip install uv
    ```
    Alternatively, you can use `pip` directly if you prefer, but `uv` is recommended by the project's structure.

### Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/MN-nagy/AIagent.git
    cd AIagent
    ```

2. **Create a Virtual Environment (Recommended with `uv`)**:
    ```bash
    uv venv
    uv pip install -r requirements.txt
    ```
    If using `pip` directly:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Obtain a Google Gemini API Key**:
    * Go to the [Google AI Studio](https://aistudio.google.com/app/apikey) or [Google Cloud Console](https://console.cloud.google.com/apis/credentials).
    * Create a new API key.

4. **Configure Environment Variables**:
    * Create a file named `.env` in the root directory of the project (where `main.py` is located).
    * Add your Gemini API key to this file:
        ```
        GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
        ```
        Replace `"YOUR_GEMINI_API_KEY_HERE"` with the actual API key you obtained.

### Running the Agent

After completing the setup, you can run the agent using `uv`:

```bash
uv run python3 main.py "Your prompt here"
```

For verbose output to debug or see the agent's internal thought process (function calls and tool outputs):

```bash
uv run python3 main.py "Your prompt here" -v
```

---

### Project Structure (for context)

```
AIagent/
├── .env
├── main.py
├── config.py
├── requirements.txt
├── pyproject.toml
├── functions/
│   ├── __init__.py
│   ├── call_func.py
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
└── calculator/
    ├── __init__.py
    ├── main.py
    └── pkg/
        ├── __init__.py
        ├── calculator.py
        └── render.py
```

> **Note**: Made this while following [boot.dev](https://www.boot.dev/tracks/backend-python-golang) course.
