#!/bin/bash

# Create a Python 3.11 virtual environment named slm-env
python3.12 -m venv random-env

# Activate the virtual environment
source random-env/bin/activate

# Install the requirements from requirements.txt
pip install poetry

# Activate the environment
echo "Virtual environment random-env created and requirements installed."
echo "To activate the environment, run: source random-env/bin/activate"
