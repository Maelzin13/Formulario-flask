# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired

# login and registration


class LoginForm(FlaskForm):
    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])
    
class MusicForm(FlaskForm):
    name = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    email = StringField('Password',
                             id='',
                             validators=[DataRequired()])
    city = StringField('Password',
                             id='',
                             validators=[DataRequired()])
    address = StringField('Password',
                             id='',
                             validators=[DataRequired()])
    birth_date = StringField('Password',
                             id='',
                             validators=[DataRequired()])
    baptism_date = StringField('Password',
                             id='',
                             validators=[DataRequired()])
    officialization_date = StringField('Password',
                             id='',
                             validators=[DataRequired()])
    in_charge = StringField('Password',
                             id='',
                             validators=[DataRequired()])
    instructor = StringField('Password',
                             id='',
                             validators=[DataRequired()])
    baptism = StringField('Password',
                             id='',
                             validators=[DataRequired()])
                             


class CreateAccountForm(FlaskForm):
    username = StringField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])
