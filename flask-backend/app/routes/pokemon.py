from flask import Blueprint, jsonify, request, redirect
import json
from ..models import Pokemon, db
from ..forms import PokemonForm
bp = Blueprint('pokemon', __name__, url_prefix="/api/pokemon")


@bp.route('/')
def all_pokemon():
    all_pokemon = Pokemon.query.all()
    json_data = json.dumps([pokemon.to_dict() for pokemon in all_pokemon])
    return json_data



@bp.route('/', methods=["POST"])
def add_pokemon():
    form = PokemonForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    print(form.data)

    if form.validate_on_submit():
        params = {
            "name": form.data['name'],
            "number": form.data['number'],
            "attack": form.data['attack'],
            "defense": form.data['defense'],
            "imageUrl" : form.data['imageUrl'],
            "type": form.data['type'],
            "moves": json.dumps(form.data['moves'])
        }
        new_pokemon = Pokemon(*params)

        db.session.add(new_pokemon)
        db.session.commit()
        return new_pokemon.to_dict()
    return '{"errors": "Bad Data"}'


# @bp.route('/', methods=['POST'])
