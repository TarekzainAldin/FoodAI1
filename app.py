from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home ():
    return render_template(('home.html'))
if __name__ == '__main__':
    with app.app_context():  # Créer un contexte d'application
        db.create_all()  # Créer les tables de la base de données
    app.run(debug=True)
