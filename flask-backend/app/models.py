from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

types = [
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
]

class Pokemon(db.Model):
    __tablename__ = 'pokemons'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    type = db.Column(db.Enum(*types), nullable=False)
    moves = db.Column(db.String(2000), nullable=False)
    encounter_rate = db.Column(db.Float(asdecimal=False))
    catch_rate = db.Column(db.Float(precision=3,asdecimal=True))
    captured = db.Column(db.Boolean)


# class PokemonType(db.Model):
#     __tablename__ = 'pokemon_types'
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.Enum(types), nullable=False)


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    happiness = db.Column(db.Integer)
    image_url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemon_id = db.Column(db.Integer, nullable=False)
