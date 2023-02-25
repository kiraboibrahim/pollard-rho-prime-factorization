from flask import Flask
from flask import render_template

from .prime_factorization import prime_factorize

app = Flask(__name__)


@app.route("/factorize")
def index():
    return render_template("index.html")


@app.route("/factorize/<int:number>")
def prime_factorize_(number):
    prime_factors = prime_factorize(number)
    return render_template("index.html", **{'number': number, "result": prime_factors})


if __name__ == "__main__":
    app.run(debug=True)
