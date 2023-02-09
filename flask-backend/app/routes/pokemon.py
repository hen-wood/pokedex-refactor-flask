from flask import Flask, Blueprint, render_template, jsonify
import app
import json
from ..models import Pokemon, db

bp = Blueprint('pokemon', __name__, url_prefix="/api/pokemon")


@bp.route('/')
def all_pokemon():
    all_pokemon = Pokemon.query.all()
    json_data = json.dumps([pokemon.to_dict() for pokemon in all_pokemon])
    # return jsonify(json_data)
    return json_data


# @bp.route('/', methods=['POST'])