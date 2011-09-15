# -*- encoding:utf-8 -*-
from flask import Blueprint, url_for, redirect, flash, session, request, render_template

from cyclonejet.forms import RegistrationForm, LoginForm
from cyclonejet.models.users import User
from cyclonejet.extensions import db

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index():
    return render_template('index.html')

@frontend.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        User.query_class.create_user(form.username.data, form.email.data, form.password.data)
        flash('Workiez')
        return redirect(url_for('.index'))
    
    return render_template('register.html', form=form)

@frontend.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first()

        if not user:
            flash('This user is not registered')
        elif not user.check_password(form.password.data):
            flash('Incorrect password')
        else:
            flash("You've been logged in")
            session['uid'] = user.id
            session['logged_in'] = True
            return redirect(url_for('.index'))

    return render_template('login.html', form=form)
