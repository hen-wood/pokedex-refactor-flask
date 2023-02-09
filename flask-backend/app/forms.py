from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, IntegerField, BooleanField, SelectField
from wtforms.validators import DataRequired, NumberRange, URL


class PokemonForm(FlaskForm):
    name = StringField('name',  [DataRequired()])
    number = IntegerField('number',  [DataRequired(message='cannot be empty'), NumberRange(min=0, message='must be over 0')])
    attack = IntegerField('attack', [DataRequired(message='cannot be empty'), NumberRange(min=0, max=100, message='must be between 0 and 100')])
    defense = IntegerField('defense', [DataRequired(message='cannot be empty'), NumberRange(min=0, max=100, message='must be between 0 and 100')])
    imageUrl = StringField('imageUrl', [DataRequired(message='cannot be empty'), URL(require_tld=False, message='must be url')])
    type = SelectField('type', [DataRequired(message='cannot be empty')], choices=[
        "fire",
        "electric",
        "normal",
        "ghost",
        "psychic",
        "water",
        "bug",
        "dragon",
        "grass",
        "fighting",
        "ice",
        "flying",
        "poison",
        "ground",
        "rock",
        "steel",
    ])
    moves = StringField('moves', [DataRequired(message='cannot be empty')])
