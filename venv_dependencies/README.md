## Dependencies
### Virtual environment (ex0)

```bash
python3 -m venv matrix_env		# create a virtual environment for the project

source matrix_env/bin/activate  # activate it - Unix

which python					# check if venv is activated
								# (it should display path to the venv)
```
### Packages (ex1)
```bash
pip install -r requirements.txt		# install dependencies with pip (into venv)
# OR
poetry install					# load dependencies into poetry
poetry run python loading.py	# run project in poetry venv
```
### Packages (ex2)
```bash
pip install dotenv		# install dependencies with pip (into venv)
```