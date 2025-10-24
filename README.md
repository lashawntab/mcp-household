
## Running and Testing the MCP Server

Follow these steps to run and test the MCP server:

### 1.  Install uv (if you have not already)

- **On Linux or macOS:**
  ```sh
  brew install uv
  ```

### 2.  Create a virtual environment using `uv`:

```sh
uv venv .
```

### 3.  Activate the environment:

- **On Linux or macOS:**

  ```sh
  source .venv/bin/activate
  ```

- **On Windows:**

  ```sh
  .venv\Scripts\activate
  ```

### 4.  Install Python 3.12+ (if you have not already)

### 5. Install Dependencies

```sh
uv pip install -r pyproject.toml
```

### 6. Start the MCP Server (Python)
```sh
python mcp_server.py
```
OR 

### 7. Test the MCP Server using MCP Inspector

   ```sh
   npx @modelcontextprotocol/inspector uv --directory . run mcp_server.py
   ```