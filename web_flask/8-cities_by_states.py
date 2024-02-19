#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """
    Closes the current SQLAlchemy session
    """
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    """
    Displays a HTML page with a list of states and cities
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
