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


@app.route('/states_list')
def states_list():
    """
    Displays a HTML page with a list of states
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
