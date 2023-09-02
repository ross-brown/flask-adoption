import os
from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from petfinder import get_oauth_token, get_random_pet

from dotenv import load_dotenv
load_dotenv()

PETFINDER_API_KEY = os.environ['PETFINDER_API_KEY']
PETFINDER_SECRET = os.environ['PETFINDER_SECRET']


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///adopt')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

connect_db(app)

auth_token = None

@app.before_request
def refresh_credentials():
    """Just once, get token and store it globally."""
    global auth_token
    auth_token = get_oauth_token()


@app.get("/")
def show_homepage():
    """Render the homepage of pets."""

    pets = Pet.query.all()

    random_pet = get_random_pet(auth_token)



    return render_template("home.html", pets=pets,
                           random_pet = random_pet)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handles adding pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url,
                      age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f'Added {name} to adoption pool')
        return redirect('/')

    else:
        return render_template('add_pet.html', form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Displays Pet Details / edit form; handles editing pet"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash(f'Edited {pet.name}.')
        return redirect(f'/{pet_id}')
    else:
        return render_template("edit_pet.html", form=form, pet=pet)




