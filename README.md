# OCMovies-API: Test API providing movie information

The OCMovies-API project is a REST API application to be executed locally in the context
of educational projects. It provides movies information from GET http endpoints.
The API provides endpoints to get detailed infomation about movies filtered by
various criteria such as genre, IMDB score or year. Endpoints allow to retrieve
info for individual movies or lists of movies.

## Installation

This locally-executable API can be installed and executed from [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/) using the following steps. A requirement is to have pipenv already installed on your python installation. If pipenv is not already installed on your computer, refer to [this page](docs/pipenv/installation.md). If you don't have
pipenv installed and do not want to install it, see the corresponding
installation procedure below.

### Installation and execution with pipenv

1. Clone this repository using `$ git clone https://github.com/pythonmentor/ocmovies-api.git`
2. Move to the ocmovies-api root folder with `$ cd ocmovies-api`
3. Install project dependencies with `pipenv install` 
4. Create and populate project database with `pipenv run python manage.py create_db`
5. Run the server with `pipenv run python manage.py runserver`

When the server is running after step 5 of the procedure, the OCMovies API can
be requested from endpoints starting with the following base URL: [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/).

Steps 1-4 are only to be done for initial installation. For subsequent launches
of the API, you only have to execute steps 5 from the root folder of the project.

### Installation and execution without pipenv (using venv and pip)

1. Clone this repository using `$ git clone https://github.com/pythonmentor/ocmovies-api.git`
2. Move to the ocmovies-api root folder with `$ cd ocmovies-api`
3. Create a virtual environment for the project with `$ python -m venv env` on windows or 
   `$ python3 -m venv env` on macos or linux.
4. Active the virtual environment with `$ env\Scripts\activate` on windows or
   `$ source env/bin/activate` on macos or linux.
5. Install project dependencies with `pip install -r requirements.txt` 
6. Create and populate project database with `python manage.py create_db`
7. Run the server with `python manage.py runserver`

When the server is running after step 7 of the procedure, the OCMovies API can
be requested from endpoints starting with the following base URL: [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/).

Steps 1-6 are only to be done for initial installation. For subsequent launches
of the API, you only have to execute steps 4 and 7 from the root folder of the project.