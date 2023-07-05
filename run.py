from flask import Flask, render_template
from forms import UniqueCharacterForm
from module import unique_character

app = Flask(__name__)
app.config['SECRET_KEY'] = 'BecomeADeveloper2023'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UniqueCharacterForm()
    if form.validate_on_submit():
        text = form.text.data
        value = unique_character(text)
    else:
        value = None
    return render_template('index.html', form=form, answer=value)
