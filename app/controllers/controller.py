from flask import render_template
from app  import app
from swapi import swapi
 
from app.models.forms import SearchForm


@app.route("/index", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        print(form.term.data)
        print(form.type_search.data)
        print(swapi.get_person(1))
    else:
        print(form.errors)
    return render_template('index.html', form=form)