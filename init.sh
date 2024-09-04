#!/bin/bash

# Create a Python 3.12 virtual environment named random-env
python3.12 -m venv random-env

brew install python-tk
# Activate the virtual environment
source ./random-env/bin/activate

# Install the requirements from requirements.txt
pip install poetry
pip install -r requirements.txt

poetry init --no-interaction
poetry add $(cat requirements.txt | xargs)
# activate the poetry plugin
poetry shell

# Activate the environment
echo "Virtual environment random-env created and requirements installed."
echo "To activate the environment, run: source random-env/bin/activate"

poetry run python src/app.py