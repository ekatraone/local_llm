# Local LLM Wrapper

## Description
This project provides a web-based interface and API for interacting with a local Large Language Model (LLM). It allows users to send prompts to the LLM and receive generated responses, either through a user-friendly web interface or via API calls.

## Features
- Web interface for easy interaction with the LLM
- RESTful API for programmatic access
- Support for various LLM backends (currently supports LLaMA)
- Easy configuration using environment variables
- Cross-platform compatibility (Windows, Mac, Linux)
- Google Colab support for cloud-based execution

## Project Structure
llm_wrapper/
│
├── app/
│   ├── init.py
│   ├── routes.py
│   ├── llm_handler.py
│   └── config.py
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── requirements.txt
├── run.py
├── .env.example
├── README.md
└── colab_runner.ipynb
Copy
## Setup and Running Instructions
See the separate instruction files for Mac, Windows, and Google Colab setup guides.

## API Documentation
POST /api/generate
Request body: JSON object with a "prompt" key
Response: JSON object with a "response" key containing the LLM's generated text

## License
This project is licensed under the MIT License.