# -*- encoding:utf-8 -*-
from flask import Module, url_for, redirect, flash, request, render_template

from cyclonejet.forms import RegistrationForm

frontend = Module(__name__)

@frontend.route('/')
def index():
    return "Hello,world"

@frontend.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        flash('Workiez')
        return redirect(url_for('index'))
    
    return render_template('register.html', form=form)
