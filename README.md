# Pollard Rho Prime Factorization

A flask web application for prime factorizing integers. The essence of this project is the problem the web application 
is addressing which is prime factorization. A modular approach has been followed to separate the presentation logic
from the business logic

The application uses the Pollard Rho algorithm with a flavor of Floyd's cycle detection algorithm. The implementation 
of the Pollard Rho algorithm is in the file 'prime_factorization.py' and the web application is contained in 
the 'app.py' file.

## Running the application

Preferably, creating a virtual environment before installing the requirements would be better.

### Creating a virtual environment

`python3 -m venv flask-sanbox`
`source flask-sanbox/bin/activate`

### Installing required packages

`pip install -r requiremnts.txt`

### Serving application

`flask run`
