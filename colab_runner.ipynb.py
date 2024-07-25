{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github"
      },
      "source": [
        "# Local LLM Wrapper - Google Colab Runner\n",
        "\n",
        "This notebook allows you to run the Local LLM Wrapper project on Google Colab."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "!pip install flask flask-wtf python-dotenv llama-cpp-python"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "%%writefile app/__init__.py\n",
        "# Paste content of app/__init__.py here"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "%%writefile app/config.py\n",
        "# Paste content of app/config.py here"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "%%writefile app/llm_handler.py\n",
        "# Paste content of app/llm_handler.py here"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "%%writefile app/routes.py\n",
        "# Paste content of app/routes.py here"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "%%writefile run.py\n",
        "# Paste content of run.py here"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Set environment variables\n",
        "%env SECRET_KEY=your-secret-key\n",
        "%env LLM_MODEL_PATH=/path/to/your/model.bin\n",
        "%env LLM_MODEL_TYPE=llama"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "!python run.py"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "Local LLM Wrapper - Colab Runner",
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}