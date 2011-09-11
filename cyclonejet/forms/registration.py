from flaskext.wtf import Form, TextField, PasswordField, validators

class RegistrationForm(Form):

    username = TextField(u"Username", validators=[validators.Required(), validators.Length(min=2)])
    email = TextField(u"Email", validators=[validators.Required(), validators.Email()])
    password = PasswordField(u"Password", validators=[validators.Required()])
    
