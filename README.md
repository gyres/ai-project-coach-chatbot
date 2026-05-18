# AI Project Coach Chatbot

AI Project Coach Chatbot is a FastAPI web chatbot that helps beginner developers understand, debug, refactor, and improve coding projects step by step.

The project was built to demonstrate backend application structure, OpenAI API integration, session-based chat handling, frontend rendering, environment configuration, and basic automated testing.

## Screenshot

![AI Project Coach Chatbot Screenshot](assets/screenshot.png)

## Features

- FastAPI backend with a clean controller, service, model, schema, and dependency structure
- OpenAI Responses API integration for AI-generated coaching replies
- Custom system prompt that guides the assistant to act as an AI Project Coach
- Session-based chat handling using signed browser sessions
- In-memory chat storage for learning and demonstration purposes
- Simple web interface built with HTML, CSS, and JavaScript
- Markdown-like response formatting for headings, bullet points, numbered lists, inline code, and code blocks
- Environment variable management using `.env`
- Safe public configuration using `.env.example`
- Basic pytest configuration for backend tests

## Demo Use Cases

The chatbot can help users:

- Understand a Python or FastAPI project structure
- Debug common Python, FastAPI, OpenAI API, Conda, VS Code, and dotenv issues
- Refactor code step by step
- Improve a coding project for GitHub portfolio presentation
- Generate beginner-friendly explanations of backend code
- Suggest next features for an AI engineering project

## Tech Stack

- Python
- FastAPI
- OpenAI API
- Jinja2
- HTML
- CSS
- JavaScript
- python-dotenv
- itsdangerous
- pytest
- Conda

## Project Structure

```text
.
├── README.md
├── requirements.txt
├── environment.yml
├── pytest.ini
├── .env.example
├── .gitignore
├── assets/
│   └── screenshot.png
├── tests/
│   └── test_chat_manager.py
└── app/
    ├── __init__.py
    ├── main.py
    ├── core/
    │   ├── __init__.py
    │   ├── config.py
    │   └── dependencies.py
    ├── controllers/
    │   ├── __init__.py
    │   └── chat_controller.py
    ├── models/
    │   ├── __init__.py
    │   ├── chat.py
    │   └── schemas.py
    ├── services/
    │   ├── __init__.py
    │   └── chat_service.py
    ├── data/
    │   └── system_prompt.txt
    ├── static/
    │   └── style.css
    └── templates/
        └── chat.html
```

## How It Works

The application follows a simple layered architecture.

1. `main.py` creates and configures the FastAPI application.
2. `chat_controller.py` defines the web routes and API endpoints.
3. `chat_service.py` handles the main business logic and OpenAI API call.
4. `chat.py` stores chat messages in memory.
5. `schemas.py` defines request and response models using Pydantic.
6. `system_prompt.txt` defines how the assistant should behave.
7. `chat.html` and `style.css` provide the browser-based chat interface.

## Setup Instructions

### 1. Clone the repository

```powershell
git clone https://github.com/your-username/ai-project-coach-chatbot.git
cd ai-project-coach-chatbot
```

### 2. Create or activate your Conda environment

```powershell
conda activate ai-project-coach-chatbot
```

If you are creating a new environment, you can use:

```powershell
conda create -n ai-project-coach-chatbot python
conda activate ai-project-coach-chatbot
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Create your `.env` file

Create a `.env` file in the project root.

Use `.env.example` as a guide:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-5.4-nano
SESSION_SECRET_KEY=replace_with_a_random_secret_key
APP_HOST=0.0.0.0
APP_PORT=3000
```

Do not commit your real `.env` file to GitHub.

## Running the App

Run the FastAPI app with Uvicorn:

```powershell
python -m uvicorn app.main:app --reload --port 3000
```

Then open your browser and go to:

```text
http://127.0.0.1:3000
```

You can also run the app through Python:

```powershell
python -m app.main
```

When running through `python -m app.main`, the app will use `APP_HOST` and `APP_PORT` from your `.env` file or the default values in `config.py`.

## Running Tests

Run:

```powershell
python -m pytest
```

The `pytest.ini` file adds the project root to the Python path and tells pytest to look inside the `tests` folder.

## Environment Variables

| Variable | Required | Description |
|---|---:|---|
| `OPENAI_API_KEY` | Yes | Your OpenAI API key |
| `OPENAI_MODEL` | No | The OpenAI model used by the chatbot |
| `SESSION_SECRET_KEY` | Yes | Secret key used for signed browser sessions |
| `APP_HOST` | No | Host used when running the app through `python -m app.main` |
| `APP_PORT` | No | Port used when running the app through `python -m app.main` |

## Example Prompts

Try asking the chatbot:

```text
Explain my FastAPI project structure like I am a beginner.
```

```text
Suggest how I can refactor this project step by step.
```

```text
Help me turn this project into a stronger AI engineering portfolio project.
```

```text
Why do we separate controllers, services, models, and schemas?
```

## What I Learned

This project helped me practise:

- Building a FastAPI web application
- Structuring backend code into maintainable layers
- Using environment variables safely
- Connecting a backend service to the OpenAI API
- Managing simple browser sessions
- Creating a custom AI assistant with a system prompt
- Rendering chatbot responses in a frontend interface
- Writing basic tests for backend logic
- Preparing a project for GitHub portfolio presentation

## Current Limitations

This is a learning and portfolio project, not a production system.

Limitations:

- Chat history is stored in memory and resets when the server restarts.
- There is no user login or account system.
- There is no database yet.
- The frontend uses plain JavaScript instead of a modern frontend framework.
- The app does not currently support file uploads.
- The app does not currently stream responses token by token.

## Security Notes

The real `.env` file should never be committed to GitHub.

Only `.env.example` should be included in the public repository. The example file shows the required environment variable names without exposing real secrets.

## License

This project is licensed under the MIT License.

## Contact

- Name: Ou Yang Yu
- GitHub: https://github.com/gyres
