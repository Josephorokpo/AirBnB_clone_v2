#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Display 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    """ Display 'HBNB """
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
