from Flask_WTF import FlaskForm
from WTForms import StringField, RadioField


class SearchForm(FlaskForm):
    term = StringField("term")
    type_search = RadioField('type_search', 
                    choices = [('planets', 'Planets'),
                    ('spaceships', 'Spaceships'),
                    ('vehicles', 'Vehicles'),
                    ('people', 'People'),
                    ('films', 'films'),
                    ('species', 'Species')] )
     