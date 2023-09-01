from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import AnyOf, URL, Optional, InputRequired


class AddPetForm(FlaskForm):
    """Form for adding pet"""

    name = StringField("Pet Name",
                       validators=[InputRequired()])

    species = StringField("Pet Species",
                          validators=[AnyOf(['cat', 'dog', 'porcupine']),
                                      InputRequired()])
    photo_url = StringField("Photo URL",
                            validators=[URL(), Optional()])
    age = SelectField("Pet Age",
                      choices=[('baby', 'Baby'), ('young', 'Young'),
                               ('adult', 'Adult'), ('senior', 'Senior')],
                      validators=[AnyOf(['baby', 'young', 'adult', 'senior']),
                                  InputRequired()])
    notes = StringField("Notes",
                            validators=[Optional()])
    # instead of stringfield use textareafield, displays more space in the input form ^


class EditPetForm(FlaskForm):
    """Form for editing a pet."""

    photo_url = StringField("Photo URL",
                            validators=[URL(), Optional()])
    notes = StringField("Notes")
    available = BooleanField("Available")
