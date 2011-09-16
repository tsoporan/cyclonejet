from flaskext.wtf import Form, TextField, PasswordField, validators, ValidationError
from cyclonejet.models import User

class RegistrationForm(Form):

    username = TextField(u"Username", validators=[validators.Required(), validators.Length(min=2)])
    email = TextField(u"Email", validators=[validators.Required(), validators.Email()])
    password = PasswordField(u"Password", validators=[validators.Required()])

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError("This username already exists.")

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError("This email already exists for a user.")

