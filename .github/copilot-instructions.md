# Study-Buddy AI Copilot Instructions

This document provides guidance for AI coding agents to effectively contribute to the `study-buddy-ai` project.

## Project Overview & Architecture

This project is a Streamlit-based application that acts as an AI study buddy. It leverages Large Language Models (LLMs) via the `langchain` and `langchain-groq` libraries to generate educational content.

The core application logic is organized within the `src/` directory, following a modular structure:

- `main.py`: The main entry point for the application.
- `src/`: Contains all the core source code.
  - `src/llm`: Houses the logic for interacting with the Groq LLM. This is where the `langchain` components are likely configured and used.
  - `src/prompts`: Stores prompt templates used to query the LLM.
  - `src/generator`: Contains the primary logic for generating content based on LLM responses.
  - `src/config`: For application configuration, such as API keys and settings.
  - `src/common`: Shared utilities, like the custom logger in `src/common/logger.py`.
  - `src/models`: Likely for data models (e.g., Pydantic models) to structure data passed between components.
  - `src/utils`: For general-purpose utility functions.

## Developer Workflow

### Setup & Installation

This project uses `uv` for fast package management. The project is packaged using `setuptools`. To install the project and its dependencies for development, run the following command in the root directory:

```bash
uv pip install -e .
```

This installs the package in "editable" mode, so changes to the source code are immediately reflected.

Dependencies are listed in `requirements.txt`. To add a new dependency, run `uv pip install <package-name>` and then add it to `requirements.txt`.

### Running the Application

The application is a Streamlit app. To run it, use:

```bash
streamlit run main.py
```

### Logging

A custom logger is configured in `src/common/logger.py`. It creates daily log files in the `logs/` directory. To use it in any module:

```python
from src.common.logger import get_logger

logger = get_logger(__name__)
logger.info("This is a log message.")
```

## Key Conventions

- **Modular Design**: All core logic should be placed in the appropriate module under `src/`. Avoid adding business logic directly into `main.py`.
- **Dependency Management**: All Python dependencies should be added to `requirements.txt`.
- **Configuration**: Use environment variables for sensitive information like API keys, loaded via `python-dotenv`. Configuration files should reside in `src/config`.
