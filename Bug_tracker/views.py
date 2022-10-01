"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Bug_tracker import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/login')
def login():
    """Renders the login page."""
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/tickets')
def tickets():
    """Renders the tickets page."""
    return render_template(
        'tickets.html',
        title='Tickets',
        year=datetime.now().year,
        message='Your application description page.'
    )
    
