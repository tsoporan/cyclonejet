from flask import Blueprint, url_for, redirect, flash, request, render_template
from cyclonejet.forms import RegistrationForm, LoginForm
from cyclonejet.models.users import User

from cyclonejet.views.utils import login_required, login_user, logout_user

accounts = Blueprint('accounts', __name__)

@accounts.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User.query_class.create_user(
                username = form.username.data,
                email= form.email.data,
                password = form.password.data
        )
        # send verification email
        user.send_mail(
            subject = "[cyclonejet] You've just signed up!",
            message = """Thank you for registering to cyclonejet [verification link here]"""
        )

        #log user in automatically
        login_user(user)

        flash("%s registered successfully!" % user.username)
        return redirect(url_for('accounts.profile'))
    
    return render_template('register.html', form=form)

@accounts.route('/login/', methods=['GET', 'POST'])
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
            login_user(user)
            return redirect(url_for('accounts.profile'))

    return render_template('login.html', form=form)

@accounts.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("You've been logged out, see ya")
    return redirect(url_for('frontend.index'))


@accounts.route('/profile')
@login_required
def profile():
    return 'Got to restricted page!'
