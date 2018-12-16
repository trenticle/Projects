"""
This script runs the S10L139_Flask_Demo2 application using a development server.
"""

from os import environ
from S10L139_Flask_Demo2 import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
