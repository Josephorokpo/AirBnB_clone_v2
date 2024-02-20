#!/usr/bin/python3
"""
Starts a Flask web application.
Listening on 0.0.0.0, port 5000

Routes:
    * /hbnb_filters: display a HTML page
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(excpt=None):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display the hbnb filters HTML page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
