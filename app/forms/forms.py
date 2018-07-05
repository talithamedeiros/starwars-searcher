from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import RadioField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    term = StringField(u'Term', validators=[DataRequired()])
    type_search = RadioField(u'Types',
                    validators=[DataRequired()], 
                    choices = [('planets', 'Planets'),
                    ('spaceships', 'Spaceships'),
                    ('vehicles', 'Vehicles'),
                    ('people', 'People'),
                    ('films', 'Films'),
                    ('species', 'Species')], 
                    default='planets')
     