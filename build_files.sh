#!/bin/bash

echo "Upgrading pip"

python3 -m pip install --upgrade pip

echo "Installing requirements"

python3 -m pip install -r requirements.txt

echo "Creating static files"

python3 manage.py collectstatic --noinput