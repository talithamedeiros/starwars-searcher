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

    return response

def jsonResult(data):
    json_data = data.json()    
    return json_data