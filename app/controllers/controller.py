from flask import render_template
from app  import app
from swapi import swapi
import requests
 
from app.models.forms import SearchForm


@app.route("/index", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        term = form.term.data
        type_search = form.type_search.data
        
        if(type_search == 'people'):
            r = requests.get('https://swapi.co/api/people/?search='+term)
        elif(type_search == 'spaceships'):
            r = requests.get('https://swapi.co/api/spaceships/?search='+term)    
        elif(type_search == 'vehicles'):
            r = requests.get('https://swapi.co/api/vehicles/?search='+term)    
        elif(type_search == 'planets'):
            r = requests.get('https://swapi.co/api/planets/?search='+term)    
        elif(type_search == 'films'):
            r = requests.get('https://swapi.co/api/films/?search='+term)    
        else:
            r = requests.get('https://swapi.co/api/species/?search='+term)    

        print(r.text)
    else:
        print(form.errors)
    return render_template('index.html', form=form)