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


@app.route('/states')
def states():
    """
    Displays a HTML page with a list of states
    """
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def state_cities(id):
    """
    Displays a HTML page with cities of a state
    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
