"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, session, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from Bug_tracker import app
import sqlite3

#Classes for the database

db = SQLAlchemy(app)


class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.Text, nullable = False)

    tracks = db.relationship("UserTrackingCompany", lazy="subquery", back_populates = "user")

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password


#Template functions for view pages
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""

    if "user" in session:
        user = session["name"]
        return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
    else:
        flash("Please log in to access your information")
        return redirect(url_for("login"))
    

@app.route('/login')
def login():
    """Renders the login page."""
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route("/register", methods=["POST", "GET"])
def register():
    if "user" in session:
        flash("You're currently already logged in")
        return redirect(url_for("user"))

    if request.method == "POST":
        session.permanent = True
        new_user = ["name", "email", "username", "password", "confirm password"]

        name = request.form["name"]
        session["name"] = name

        email = request.form["email"]
        session["email"] = email

        username = request.form["username"]
        session["username"] = username

        preencrypted_password = request.form["password"]
        password = sha256_crypt.hash(preencrypted_password)
        session ["password"] = password

        confirmed_password = request.form["confirm"]
        
        if confirmed_password != preencrypted_password:
            flash("The password fields do not match, please type again.")
            return redirect(url_for("register"))
        
        if not username:
            flash("Please enter a username")
        if not email:
            flash("Please enter an email")
        if not password:
            flash("Please enter a password")

        new_user = User(name = name, username = username, email = email, password= password)
        db.session.add(new_user)
        db.session.commit()
       
        flash("Welcome, {}".format(new_user.username))
        return redirect(url_for("user"))
      
    return render_template("register.html")


@app.route("/empty_ticket")
def empty_ticket():
    "Renders a ticket page when nobody is logged in."

    return render_template(
        'empty_ticket.html',
        title='Tickets',
        year=datetime.now().year,
        message='Your application description page.'
        )
    

@app.route('/tickets')
def tickets():
    """Renders the tickets page."""
    if "user" in session:
        
        return render_template(
            'tickets.html',
            title='Tickets',
            year=datetime.now().year,
            message='Your application description page.'
        )
    
    return redirect(url_for("empty_ticket"))
