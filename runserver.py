"""
This script runs the Bug_tracker application using a development server.
"""

from os import environ
import os
from Bug_tracker import app


app.secret_key = os.urandom(24)

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
