from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class UniqueCharacterForm(FlaskForm):
    text = TextAreaField('Введіть текст:')
    submit = SubmitField('Надіслати')
