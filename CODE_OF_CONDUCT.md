### Using Python `venv` 🐍

- Go to location using `cmd` or `terminal`

  ```bash
  python -m venv myvenv
  ```

  ```sh
  # On Windows
  .\myvenv\Scripts\activate --OR-- source myvenv/bin/activate # On Linux or Mac
  ```

  ```sh
  pip install -r requirements.txt
  ```

### Using Docker 🐳

- Go to location using `cmd` or `terminal`

  ```sh
  cd env_docker
  ```

  ```sh
  docker compose -f docker-compose.yml up
  ```

  - Press `Ctrl+C` to stop and then run the following

  ```sh
  docker-compose -f docker-compose.yml down --volumes --rmi all 
  ```

- Put the desired notebook in the `notebook` directory along with the data in the `data` folder.

### Using Conda 🧶

- Open your favourite `terminal` or `cmd` to download the dependencies listed in `envALL.yml`

  ```sh
  conda env create -f envALL.yml
  ```

### Using `uv`

- For Linux and macOS

  ```sh
  curl -LsSf <https://astral.sh/uv/install.sh> | sh
  ```

- For Windows, use PowerShell:

  ```sh
  powershell -ExecutionPolicy ByPass -c "irm <https://astral.sh/uv/install.ps1> | iex"
  ```

- If `curl` is not installed, use `wget` instead:

  ```sh
  wget -qO- <https://astral.sh/uv/install.sh> | sh
  ```

- install it globally using

  ```sh
  pip install uv
  ```

- Initialize a new Python project by running:

  ```sh
  uv init llms
  ```

- To add a new package to `pyproject.toml`  

  ```sh
  uv add numpy
  ```

- To remove a new package

  ```sh
  uv remove numpy
  ```

- Add all dependencies from `requirements.txt`

    ```sh
    uv add -r requirements.txt
    ```

- Sync Dependencies

    ```sh
    uv pip compile .pyproject.toml -o requirements.in
    ```

- Run main.py

    ```sh
    uv run main.py
    ```

## References

1. <https://realpython.com/python-uv/>
2. <https://docs.astral.sh/uv/guides/projects/>
