from flask import Flask, request, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
app.secret_key = '1111'
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:i2245699@localhost/postgres"
manager = LoginManager(app)
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    price = db.Column(db.Float)
    comments = db.Column(db.VARCHAR)


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.VARCHAR, nullable=False, unique=True)
    password = db.Column(db.VARCHAR(255), nullable=False)


@manager.user_loader
def load_user(user_id):
    return User.guery.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = User.query.filter_by(login=login).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            next_page = request.args.get('next')

            return redirect(next_page)

        else:
            flash('Login or password is not correct')
    else:
        flash('Please fill login and password fields')

    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('products'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (login or password or password2):
            flash('Please, fill all fields!')
        elif password != password2:
            flash('Passwords are not equal!')
        else:
            hash_pwd = generate_password_hash(password)
            new_user = User(login=login, password=hash_pwd)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login_page'))

    return render_template('register.html')


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)

    return response


@app.route('/products/add', methods=['POST', 'GET'])
@login_required
def add():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        comments = request.form['comments']

        product = Products(name=name, price=price, comments=comments)

        try:
            db.session.add(product)
            db.session.commit()
            return redirect('/products')
        except:
            return 'Получилась ошибка'
    else:
        return render_template('add.html')


@app.route('/products/<int:id>/update', methods=['POST', 'GET'])
@login_required
def update(id):
    product = Products.query.get(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = request.form['price']
        product.comments = request.form['comments']

        try:
            db.session.commit()
            return redirect('/products')
        except:
            return 'Получилась ошибка'
    else:
        return render_template('update.html', product=product)


@app.route('/products')
def products():
    products = Products.query.order_by(Products.price).all()
    return render_template('products.html', products=products)


@app.route('/products/<int:id>')
def detail(id):
    product = Products.query.get(id)
    return render_template('detail.html', product=product)


@app.route('/products/<int:id>/del')
@login_required
def delete(id):
    product = Products.query.get_or_404(id)

    try:
        db.session.delete(product)
        db.session.commit()
        return redirect('/products')
    except:
        return "При удалении продукта произошла ошибка"


@app.route('/products/daily')
def daily():
    return render_template('daily.html')


if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run(port=8000)



return, redirect