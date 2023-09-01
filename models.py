from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    app.app_context().push()
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet."""
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(25),
        nullable=False
    )

    species = db.Column(
        db.String(40),
        nullable=False
    )

    photo_url = db.Column(
        db.Text,
        default='',
        nullable=False
    )

    age = db.Column(
        db.String(5),
        db.CheckConstraint('age in ["baby", "young", "adult", "senior"]'),
        nullable=False
    )

    notes = db.Column(
        db.Text,
        nullable=True
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )
