#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb')
def display_hbnb():
    """Display 'HBNB'"""
    return 'HBNB'

@app.route('/c/<text>')
def display_c(text):
    """Display 'C' followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/')
@app.route('/python/<text>')
def display_python(text='is cool'):
    """Display 'Python' followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>')
def is_number(n):
    """Display 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
    """Display an HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Display an HTML page with 'Number: n is even|odd'"""
    return render_template('6-number_odd_or_even.html', number=n, parity=('even' if n % 2 == 0 else 'odd'))
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)