# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired
from wtforms.fields import RadioField

# login and registration


class LoginForm(FlaskForm):
    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])
    
class MusicForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    city = StringField('Cidade', validators=[DataRequired()])
    address = StringField('Endereço', validators=[DataRequired()])
    birth_date = StringField('Data de Nascimento', validators=[DataRequired()])
    baptism_date = StringField('Data de Batismo', validators=[DataRequired()])
    officialization_date = StringField('Data de Oficialização', validators=[DataRequired()])
    in_charge = RadioField('Encarregado', choices=[('sim', 'Sim'), ('nao', 'Não')], validators=[DataRequired()])
    instructor = RadioField('Instrutor(a)', choices=[('sim', 'Sim'), ('nao', 'Não')], validators=[DataRequired()])
    baptism = RadioField('Batizado', choices=[('sim', 'Sim'), ('nao', 'Não')], validators=[DataRequired()])

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
