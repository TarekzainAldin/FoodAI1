from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(125), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.png")
    Diet = db.Column(db.Text, nullable=True)
    password = db.Column(db.String(60), nullable=False)
    lessons = db.relationship("Lesson", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.fname}', '{self.lname}', '{self.username}', '{self.email}', '{self.image_file}')"

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    thumbnail = db.Column(
        db.String(20), nullable=False, default="default_thumbnail.jpg"
    )
    slug = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)

    def __repr__(self):
        return f"Lesson('{self.title}', '{self.date_posted}')"

class Users(db.Model):
    __tablename__ = 'users'
    User_id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(45), nullable=False)
    Email = db.Column(db.String(45), unique=True, nullable=False)
    objectif = db.Column(db.Text, nullable=True)
    preference = db.Column(db.Integer, nullable=True)
    Password = db.Column(db.String(128), nullable=False)
    Created_at = db.Column(db.DateTime, default=datetime.utcnow)

    orders = db.relationship('Order', backref='user', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)

class Products(db.Model):
    __tablename__ = 'products'
    Product_id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(45), nullable=False)
    Description = db.Column(db.String(200), nullable=True)
    Price = db.Column(db.Float, nullable=False)

    reviews = db.relationship('Review', backref='product', lazy=True)


class Orders(db.Model):
    __tablename__ = 'orders'
    Order_id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey('users.User_id'), nullable=False)
    Status = db.Column(db.String(45), default='Pending', nullable=False)
    Total_amount = db.Column(db.Float, nullable=False)
    Order_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    products = db.relationship('Product', secondary='order_products', backref='orders')


class Reviews(db.Model):
    __tablename__ = 'reviews'
    Review_id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey('users.User_id'), nullable=False)
    Product_id = db.Column(db.Integer, db.ForeignKey('products.Product_id'), nullable=False)
    Rating = db.Column(db.Integer, nullable=False)
    Comment = db.Column(db.String(500), nullable=True)
    Review_date = db.Column(db.DateTime, default=datetime.utcnow)

order_products = db.Table('order_products',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.Order_id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.Product_id'), primary_key=True)
)
