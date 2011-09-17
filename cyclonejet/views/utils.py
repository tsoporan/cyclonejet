from flask import session, redirect, url_for
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session or session['logged_in'] is None:
            return redirect(url_for('accounts.login'))
        return f(*args, **kwargs)
    return decorated_function

def login_user(user):
    session['uid'] = user.id
    session['username'] = user.username
    session['logged_in'] = True

def logout_user():
    session.pop('logged_in', None)
