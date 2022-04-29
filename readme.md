# Project Setup

[![Production Workflow](https://github.com/rod608/flask_auth2/actions/workflows/prod.yml/badge.svg)](https://github.com/rod608/flask_auth2/actions/workflows/prod.yml)

* [Production Deployment](https://ren9-p2-prod.herokuapp.com/)


[![Development Workflow](https://github.com/rod608/flask_auth2/actions/workflows/dev.yml/badge.svg)](https://github.com/rod608/flask_auth2/actions/workflows/dev.yml)

* [Developmental Deployment](https://ren9-p2-dev.herokuapp.com/)

# Project 3 Notes: 
Requirement #1: "Your project must have a log file with an entry for each time a user uploads a CSV playlist."
   - COMPLETED | Embedded within songs_upload() function within the songs/dunderinit. The log file is myApp.log.

Requirement #2: "There must be a test to verify that the CSV file is uploaded and processed."
   - A portion of the test_csv_verification() test method in tests/csv_verification_test accomplishes this.

Requirement #3: "You must create a database record that is related to the user record for each song in the playlist.  You only need to store the song's title, artist, year, and genre."
   - COMPLETED | Found in the Song class within db/models/dunderinit. All four requested properties for the Song-related datatable are included.

Requirement #4: "You must have a test for login, a test for registration, a test for accessing the dashboard as a logged-in user, and a test for denying access to the dashboard, and denying access to uploading the CSV file"
   - All can be found within tests/user_test in their associated functions and are in order following the test_adding_user() method.

Requirement #5: "Write a log message for each request and response that records the method, route, time, request address."
   - COMPLETED | Done by making use of RequestFormatter within logging_config's dunderinit. Check out the request logger.


## Running Locally

1. To Build with docker compose:
   docker compose up --build
2. To run tests, Lint, and Coverage report use this command: pytest --pylint --cov

.pylintrc is the config for pylint, .coveragerc is the config for coverage and setup.py is a config file for pytest


### Future Notes and Resources
* https://flask-user.readthedocs.io/en/latest/basic_app.html
* https://hackersandslackers.com/flask-application-factory/
* https://suryasankar.medium.com/a-basic-app-factory-pattern-for-production-ready-websites-using-flask-and-sqlalchemy-dbb891cdf69f
* https://develie.hashnode.dev/exploring-flask-sqlalchemy-queries
* https://wtforms.readthedocs.io/en/3.0.x/
* https://bootstrap-flask.readthedocs.io/en/stable/
* https://flask-sqlalchemy.palletsprojects.com/en/2.x/