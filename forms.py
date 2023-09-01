from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import AnyOf, URL, Optional


class AddPetForm(FlaskForm):
    """Form for adding pet"""

    name = StringField("Pet Name")
    species = StringField("Pet Species",
                          validators=[AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = StringField("Photo URL",
                            validators=[URL(), Optional()])
    age = SelectField("Pet Age",
                      choices=[('baby', 'Baby'), ('young', 'Young'),
                               ('adult', 'Adult'), ('senior', 'Senior')],
                      validators=[AnyOf(['baby', 'young', 'adult', 'senior'])])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing a pet."""

    photo_url = StringField("Photo URL",
                            validators=[URL(), Optional()])
    notes = StringField("Notes")
    available = BooleanField("Available")
