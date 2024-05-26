In folder tree we have `poetry.lock`. This lock the versions of packages with respect to the day the project was create. If the the project is cloned 10 months ago the project will have packages with version of 10 months ago.

# From Youtube

1. `poetry --version`
2. `poetry new project_youtube`
3. `cd project_youtube`
4. `poetry run python --version`
5. `poetry add requests`
6. `poetry run python ./project_youtube/main.py`
7. `poetry add pytest`
8. `poetry run pytest`