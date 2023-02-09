
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask import Flask
from app.config import Config
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
from .models import db, Pokemon, Item
from .routes import pokemon
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_object(Config)
app.register_blueprint(pokemon.bp)
db.init_app(app)
Migrate(app,db)

@app.cli.command()
def seed():
    from app.seeds import seed_data
    seed_data()

@app.route('/')
def home():
    return '<h1> home </h1>'





# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response