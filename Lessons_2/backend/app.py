from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:i2245699@localhost/postgres"

db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return render_template('index.html', title='Main page', age=16, users=[{'name': 'Ilya'}, {'name': 'Vania'}])


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32))
    age = db.Column(db.Integer)
    email = db.Column(db.String(255))

    def __init__(self, form):
        self.firstname = form['firstname']
        self.lastname = form['lastname']
        self.age = form['age']
        self.email = form['email']


db.create_all()


@app.route('/user/create', methods=['POST'])
def form():
    try:
        user = User(request.form)
        db.session.add(user)
        db.session.commit()

        return redirect('/users')
    except Exception as e:
        return render_template('error.html', msg=e)


@app.route('/users')
def users():
    users = User.query.all()

    return render_template('list.html', users=users)


if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run(port=8000)








#
# @app.route('/')
# def hello_world():
#     return f'{datetime.datetime.now()}'
#
#
# @app.route('/user/<int:id>')
# def user(id):
#     print(type(id))
#     return f'I user with id: {id}'
#

# @app.route('/user/<id>/friends')
# def friends(id):
#     return f'My friends is: {id}'

#
# @app.route('/two_pow/<int:id>') # 2 ** id
# def two(id):
#     return f'{2**id}'

#
# @app.route('/admin')
# def admin():
#     return f'Admin'
#
# @app.route('/user/<name>')
# def user(name):
#     return f'name: {name}'
#
# @app.route('/guest/<guest_name>') #перекинет на admin or user(28 - 41)
# def guest(guest_name):
#     if guest_name == 'admin':
#         return redirect(url_for('admin'))
#
#     return redirect(url_for('user', name=guest_name))

#
# @app.route('/my_word/<word>') #только слово или нечетные буквы выведет
# def word(word):
#     if len(word) % 2 == 0:
#         return word
#
#     return word[::2]