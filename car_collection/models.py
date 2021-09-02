from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid 
from datetime import datetime

# Adding Flask Security for Passwords
from werkzeug.security import generate_password_hash, check_password_hash

# Import Secrets module (Given by Python)
import secrets

# Imports for Login Manager
from flask_login import UserMixin, login_manager

# Imports for Flask Login
from flask_login import LoginManager

# Imports for Flask Marshmallow
from flask_marshmallow import Marshmallow



db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String(150), primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(150), nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    car = db.relationship('Car', backref = 'owner', lazy = True)

    def __init__(self, email, first_name = '', last_name = '', id = '', password = '', token = '', g_auth_verify = False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self,length):
        return secrets.token_hex(length) 

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database.'

class Car(db.Model):
    id = db.Column(db.String, primary_key = True)
    year = db.Column(db.String(4))
    car_make = db.Column(db.String)
    car_model = db.Column(db.String(100))
    color = db.Column(db.String(100))
    name = db.Column(db.String, nullable = True)
    horsepower = db.Column(db.Integer, nullable = True)
    top_speed = db.Column(db.Integer, nullable = True)
    modifications = db.Column(db.String, nullable = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, year, car_make, car_model, color, name, horsepower, top_speed, modifications, user_token, id = ''):
        self.id = self.set_id()
        self.year = year
        self.car_make = car_make
        self.car_model = car_model
        self.color = color
        self.name = name
        self.horsepower = horsepower
        self.top_speed = top_speed
        self.modifications = modifications
        self.user_token = user_token

    def __repr__(self):
        return f'The following car has been added: {self.car_model}'

    def set_id(self):
        return secrets.token_urlsafe()

# Creation of the API Schema via the Marshmallow Object
class CarSchema(ma.Schema):
    class Meta:
        fields = ['id', 'year', 'car_make', 'car_model', 'color', 'name', 
        'horsepower', 'top_speed', 'modifications']


car_schema = CarSchema()

cars_schema = CarSchema(many = True)
    
    