# Virtual environments in Python (venv)
# A virtual environment loads your entire installation
# from Python to a folder in the chosen path.
# When activating a virtual environment, installing the
# virtual environment will be used.
# venv is the module we will use to
# create virtual environments.
# You can give whatever name you prefer to a
# virtual environment, but the most common are:
# venv env .venv .env
#
# How to create virtual environments
# Open your project folder in the terminal
# and type:
# python -m venv venv
#
# Activating and deactivating my virtual environment
# Windows: .\venv\Scripts\activate
# Linux and Mac: source venv/bin/activate
# Deactivate: deactivate
#
# pip - installing packages and libraries
# Install latest version:
# pip install package_name
# Install accurate version
# (there are other forms also not mentioned)
# pip install package_name==0.0.0
# Uninstall package
# pip uninstall package_name
# Freeze (see packages)
# pip freeze
#
# Creating and using a requirements.txt
# pip freeze > requirements.txt
# Installing everything from requirements.txt
# pip install -r requirements.txt