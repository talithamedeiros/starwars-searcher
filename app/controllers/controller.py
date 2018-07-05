from flask import render_template
from app  import app
from swapi import swapi
import requests
import json
 
from app.models.forms import SearchForm


@app.route("/index", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    form = SearchForm()
    json_data = ""
    if form.validate_on_submit():
        data = responseSearch(form.term.data, form.type_search.data)
        json_data = jsonResult(data)

    return render_template('index.html', form=form, json_data=json_data)

def responseSearch(term, type_search):
    uri = f'https://swapi.co/api/{type_search}/?search={term}'
    
    response = requests.get(uri)

    return response

def jsonResult(data):
    json_data = data.json()    
    return json_data