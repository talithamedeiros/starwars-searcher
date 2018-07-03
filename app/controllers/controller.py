from flask import render_template
from app  import app
from swapi import swapi
import requests
import json
from jinja2 import Template
 
from app.models.forms import SearchForm


@app.route("/index", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        term = form.term.data
        type_search = form.type_search.data

        if(type_search == 'people'):
            response = requests.get('https://swapi.co/api/people/?search='+term)
        elif(type_search == 'spaceships'):
            response = requests.get('https://swapi.co/api/spaceships/?search='+term)    
        elif(type_search == 'vehicles'):
            response = requests.get('https://swapi.co/api/vehicles/?search='+term)    
        elif(type_search == 'planets'):
            response = requests.get('https://swapi.co/api/planets/?search='+term)    
        elif(type_search == 'films'):
            response = requests.get('https://swapi.co/api/films/?search='+term)    
        else:
            response = requests.get('https://swapi.co/api/species/?search='+term)    

        data = response.text
        print(data)

    else:
        print(form.errors)
    return render_template('index.html', form=form)