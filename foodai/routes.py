from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")
