from flask import Flask, request, jsonify, render_template, url_for
from models import db, User, Product, Order, Review

app = Flask(__name__)

@app.route('/home')
def home():
 return render_template('home.html')
# Routes for Users
# @app.route('/users', methods=['POST'])
# def create_user():
#     data = request.json
#     new_user = User(Name=data['name'], Email=data['email'], Password=data['password'])
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({'message': 'User created successfully'}), 201

# @app.route('/users', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     output = [{'User_id': user.User_id, 'Name': user.Name, 'Email': user.Email} for user in users]
#     return jsonify(output), 200

# # Routes for Products
# @app.route('/products', methods=['POST'])
# def create_product():
#     data = request.json
#     new_product = Product(Name=data['name'], Description=data['description'], Price=data['price'])
#     db.session.add(new_product)
#     db.session.commit()
#     return jsonify({'message': 'Product created successfully'}), 201

# @app.route('/products', methods=['GET'])
# def get_products():
#     products = Product.query.all()
#     output = [{'Product_id': product.Product_id, 'Name': product.Name, 'Description': product.Description, 'Price': product.Price} for product in products]
#     return jsonify(output), 200

# # Routes for Orders
# @app.route('/orders', methods=['POST'])
# def create_order():
#     data = request.json
#     new_order = Order(User_id=data['user_id'], Status=data.get('status', 'Pending'), Total_amount=data['total_amount'])
#     db.session.add(new_order)
#     db.session.commit()
#     return jsonify({'message': 'Order placed successfully'}), 201

# @app.route('/orders', methods=['GET'])
# def get_orders():
#     orders = Order.query.all()
#     output = [{'Order_id': order.Order_id, 'User_id': order.User_id, 'Status': order.Status, 'Total_amount': order.Total_amount, 'Order_date': order.Order_date} for order in orders]
#     return jsonify(output), 200

# # Routes for Reviews
# @app.route('/reviews', methods=['POST'])
# def create_review():
#     data = request.json
#     new_review = Review(User_id=data['user_id'], Product_id=data['product_id'], Rating=data['rating'], Comment=data['comment'])
#     db.session.add(new_review)
#     db.session.commit()
#     return jsonify({'message': 'Review submitted successfully'}), 201

# @app.route('/reviews', methods=['GET'])
# def get_reviews():
#     reviews = Review.query.all()
#     output = [{'Reviews_id': review.Reviews_id, 'User_id': review.User_id, 'Product_id': review.Product_id, 'Rating': review.Rating, 'Comment': review.Comment, 'Review_date': review.Review_date} for review in reviews]
#     return jsonify(output), 200

# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for("home"))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
#             "utf-8"
#         )
#         user = User(
#             fname=form.fname.data,
#             lname=form.lname.data,
#             username=form.username.data,
#             email=form.email.data,
#             password=hashed_password,
#         )
#         db.session.add(user)
#         db.session.commit()
#         flash(f"Account created successfully for {form.username.data}", "success")
#         return redirect(url_for("login"))
#     return render_template("register.html", title="Register", form=form)


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for("home"))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#             login_user(user, remember=form.remember.data)
#             next_page = request.args.get("next")
#             flash("You have been logged in!", "success")
#             return redirect(next_page) if next_page else redirect(url_for("home"))
#         else:
#             flash("Login Unsuccessful. Please check credentials", "danger")
#     return render_template("login.html", title="Login", form=form)


# @app.route("/logout")
# def logout():
#     logout_user()
#     return redirect(url_for("home"))


# @app.route("/dashboard", methods=["GET", "POST"])
# @login_required
# def dashboard():
#     profile_form = UpdateProfileForm()
#     if profile_form.validate_on_submit():
#         if profile_form.picture.data:
#             picture_file = save_picture(profile_form.picture.data)
#             current_user.image_file = picture_file
#         current_user.username = profile_form.username.data
#         current_user.email = profile_form.email.data
#         current_user.bio = profile_form.bio.data
#         db.session.commit()
#         flash("Your profile has been updated", "success")
#         return redirect(url_for("dashboard"))
#     elif request.method == "GET":
#         profile_form.username.data = current_user.username
#         profile_form.email.data = current_user.email
#         profile_form.bio.data = current_user.bio
#     image_file = url_for("static", filename=f"user_pics/{current_user.image_file}")
#     return render_template(
#         "dashboard.html",
#         title="Dashboard",
#         profile_form=profile_form,
#         image_file=image_file,
#     )
