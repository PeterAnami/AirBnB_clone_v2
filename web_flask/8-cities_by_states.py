#!/usr/bin/python3
""" This module starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """ The "cities_by_states" route.
        Sends a corresponding template.
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_appcontext(self):
    """ Hook that runs before app would be closed
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
