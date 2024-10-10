from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Farel275&@localhost/FoodAI'  # Mettez à jour avec vos identifiants DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Modèle User
class User(db.Model):
    __tablename__ = 'user'
    User_id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(45))
    Email = db.Column(db.String(45), unique=True, nullable=False)
    Password = db.Column(db.String(128), nullable=False)  # Hashed password
    Goal = db.Column(db.Text)
    Diet_preference = db.Column(db.Integer)
    Created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Users(db.Model):
    __tablename__ = 'users'
    User_id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(45))
    Email = db.Column(db.String(45), unique=True, nullable=False)
    Password = db.Column(db.String(128), nullable=False)  # Hashed password
    Goal = db.Column(db.Text)
    Diet_preference = db.Column(db.Integer)
    Created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Route pour la page d'inscription
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        goal = request.form.get('goal')
        diet_preference = request.form.get('diet_preference')

        # Validation des champs requis
        if not name or not email or not password:
            return render_template('signup.html', error="Tous les champs obligatoires doivent être remplis.")

        # Vérification si l'email existe déjà
        if User.query.filter_by(Email=email).first():
            return render_template('signup.html', error="L'email existe déjà.")

        # Hashage du mot de passe
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Création d'un nouvel utilisateur
        new_user = User(Name=name, Email=email, Password=hashed_password, Goal=goal, Diet_preference=diet_preference)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))  # Rediriger vers la page de connexion après succès
        except Exception as e:
            db.session.rollback()
            return render_template('signup.html', error=f"Erreur de base de données : {str(e)}")

    # Si c'est une requête GET, afficher la page d'inscription
    return render_template('signup.html')

# Route pour la page de connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Validation des champs requis
        if not email or not password:
            return render_template('login.html', error="L'email et le mot de passe sont requis.")

        # Rechercher l'utilisateur par email
        user = User.query.filter_by(Email=email).first()
        if not user or not bcrypt.check_password_hash(user.Password, password):
            return render_template('login.html', error="Email ou mot de passe invalide.")

        # Si les informations sont correctes, rediriger vers la page de succès (ou une autre page)
        return redirect(url_for('dashboard'))  # Exemple : redirection après connexion réussie

    # Si c'est une requête GET, afficher la page de connexion
    return render_template('login.html')

# Route pour le tableau de bord (exemple après connexion)
@app.route('/dashboard')
def dashboard():
    return "<h1>Bienvenue dans votre tableau de bord !</h1>"

if __name__ == '__main__':
    with app.app_context():  # Créer un contexte d'application
        db.create_all()  # Créer les tables de la base de données
    app.run(debug=True)
