from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField

class AddPetForm(FlaskForm):
    """Form for adding pet"""

    name = StringField("Pet Name")
    species = StringField("Pet Species")
    photo_url = StringField("Photo URL")
    age = SelectField("Pet Age",
                     choices= [('baby','Baby'),('young','Young'),
                       ('adult', 'Adult'),('senior', 'Senior')])
    notes = StringField("Notes")

