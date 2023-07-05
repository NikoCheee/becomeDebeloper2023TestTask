from flask import Flask, render_template
from forms import UniqueCharacterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'BecomeADeveloper2023'


@app.route('/')
def index():
    form = UniqueCharacterForm()
    if form.validate_on_submit():
        text = form.text.data
    return render_template('index.html', form=form)
