# -*- encoding:utf-8 -*-
from flask import Blueprint, url_for, redirect, flash, request, render_template

from cyclonejet.forms import RegistrationForm
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
