import os
from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///adopt')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"

connect_db(app)


@app.get("/")
def show_homepage():
    """Render the homepage of pets."""

    pets = Pet.query.all()

    return render_template("home.html", pets=pets)


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
