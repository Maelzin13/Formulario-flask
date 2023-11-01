# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin

from apps import db, login_manager

from apps.authentication.util import hash_pass

from datetime import date

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.LargeBinary)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)


@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Users.query.filter_by(username=username).first()
    return user if user else None

class Musicos(db.Model):
    __tablename__ = 'Musicos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    city = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(64), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    baptism_date = db.Column(db.Date, nullable=False)
    officialization_date = db.Column(db.Date, nullable=False)
    in_charge = db.Column(db.String(64), nullable=False)
    instructor = db.Column(db.String(64), nullable=False)
    baptism = db.Column(db.String(64), nullable=False)

    def __init__(self, name, email, city, address, birth_date, baptism_date, officialization_date, in_charge, instructor, baptism):
        self.name = name
        self.email = email
        self.city = city
        self.address = address
        self.birth_date = birth_date
        self.baptism_date = baptism_date
        self.officialization_date = officialization_date
        self.in_charge = in_charge
        self.instructor = instructor
        self.baptism = baptism

    def __repr__(self):
        return self.name