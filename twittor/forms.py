from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length

from twittor.models import User


class LoginForm(FlaskForm):
    class Meta:
        csrf = False
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sigin In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email Address',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password Repeat', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('please use other username')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('please use other email')


class EditProfileForm(FlaskForm):
    about_me = TextAreaField('About me', validators=[Length(min=0, max=120)])
    submit = SubmitField('Save')

class TweetForm(FlaskForm):
    tweet = TextAreaField('Tweet', validators=[DataRequired(), Length(min=0, max=140)])
    submit = SubmitField('Tweet')
    
