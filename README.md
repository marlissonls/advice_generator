
# Advice Generator 👴🏻📝  
Get new advice from an advice API and make your life easier!

## Get Started 🚀  

Install Python

~~~bash  
  sudo apt-get update
  sudo apt-get install python3.10
  python3 --version
~~~

Clone the project

~~~bash  
  git clone https://github.com/marlissonls/advice_generator
~~~

Go to the project directory  

~~~bash  
  cd advice_generator
~~~

Start getting advice

~~~bash  
  python3 main.py
~~~

## Run Tests with Pytest 🔥

Install Pytest

~~~bash  
  sudo apt-get update
  sudo apt-get install pytest
  pytest --version
~~~

Go to the project directory  

~~~bash  
  cd advice_generator
~~~

Run Tests

~~~bash  
  pytest
~~~

## Install Poetry for Virtual Envs ✨

Install Poetry on:

Linux, macOS, Windows (WSL)

~~~bash  
  curl -sSL https://install.python-poetry.org | python3 -
~~~

Windows

~~~bash  
  (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
~~~

Add Poetry to your PATH:

The installer creates a poetry wrapper in a well-known, platform-specific directory:

- $HOME/.local/bin on Unix.
- %APPDATA%\Python\Scripts on Windows.
- $POETRY_HOME/bin if $POETRY_HOME is set.

If this directory is not present in your $PATH, you can add it in order to invoke Poetry as poetry.

Alternatively, the full path to the poetry binary can always be used:

- ~/Library/Application Support/pypoetry/venv/bin/poetry on MacOS.
- ~/.local/share/pypoetry/venv/bin/poetry on Linux/Unix.
- %APPDATA%\pypoetry\venv\Scripts\poetry on Windows.
- $POETRY_HOME/venv/bin/poetry if $POETRY_HOME is set.

Go to the project directory  

~~~bash  
  cd advice_generator
~~~

Install dependencies  

~~~bash  
  poetry install
~~~

Activate the virtual env

~~~bash  
  poetry shell
~~~