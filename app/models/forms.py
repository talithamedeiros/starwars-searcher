from flask_wtf import FlaskForm
from wtforms import StringField, RadioField


class SearchForm(FlaskForm):
    term = StringField("term")
    type_search = RadioField('type_search', 
                    choices = [('planets', 'Planets'),
                    ('spaceships', 'Spaceships'),
                    ('vehicles', 'Vehicles'),
                    ('people', 'People'),
                    ('films', 'films'),
                    ('species', 'Species')])
     