from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UniqueCharacterForm(FlaskForm):
    text = StringField('Введіть текст', validators=[DataRequired()])
    submit = SubmitField()
