# Pollard Rho Prime Factorization

![Prime Factorization Application Screenshot](https://ik.imagekit.io/8mch78q847k/prime-factorization-demo_XuHZZrAL9.png?ik-sdk-version=javascript-1.4.3&updatedAt=1677315114588)

A flask web application for prime factorizing integers. The focus of this project is centered around prime factorization.
Developing it as a web application is a means of sharing the application service with others. A modular approach has been 
followed to ease reuse and separate business logic from presentation logic.

The application uses the Pollard Rho algorithm with a flavor of Floyd's cycle detection algorithm. The implementation 
of the Pollard Rho algorithm is in the file 'prime_factorization.py' and the web application is contained in 
the 'app.py' file.

## Running the application

Preferably, creating a virtual environment before installing the requirements is better.

### Creating a virtual environment

`python3 -m venv flask-sanbox`

`source flask-sanbox/bin/activate`

### Installing required packages

`pip install -r requiremnts.txt`

### Serving application

`flask run`
