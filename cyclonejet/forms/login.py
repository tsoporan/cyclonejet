from flaskext.wtf import Form, TextField, PasswordField, validators

class LoginForm(Form):
    username = TextField(u"Username", validators=[validators.Required()])
    password = PasswordField(u"Password", validators=[validators.Required()]) 
