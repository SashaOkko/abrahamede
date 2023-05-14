from flask_wtf import FlaskForm
from wtforms import StringField, PaswordField, BoolField, SumbitField
from wtforms.validators import Datarequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Datarequired()])
    username = StringField('Password', validators=[Datarequired()])
    remember_me = BooleanField('Remember Me')
    sumbit = SumbitField('Sign in')

