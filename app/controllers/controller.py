from flask import render_template
from app  import app

from app.models.forms import SearchForm


@app.route("/index")
@app.route("/")
def index():
    form = SearchForm()
    return render_template('index.html', form=form)