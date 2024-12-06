"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Vehicle, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_all_user():
    all_user = User.query.all()
    if all_user is None:
        return jsonify("No Records found!!!!"), 404
    all_user = list(map(lambda x: x.serialize(), all_user))
    return jsonify(all_user), 200

@app.route('/people', methods=["GET"])
def get_all_people():
    all_people = Character.query.all()
    if all_people is None:
        return jsonify("No Records found!!!!"), 404
    all_people = list(map(lambda x: x.serialize(), all_people))
    return jsonify(all_people), 200

@app.route('/people/<int:person_id>', methods=["GET"])
def get_person(person_id):
    single_person = Character.query.get(person_id)

    if single_person is None:
        raise APIException(f'Person ID {person_id} is not found', status_code=404)
    
    single_person = single_person.serialize()
    return jsonify(single_person), 200

@app.route('/planets' , methods=["GET"])
def get_all_planets():
    all_planets = Planet.query.all()
    if all_planets is None:
        return jsonify("No Records found!!!!"), 404
    all_planets = list(map(lambda x: x.serialize(), all_planets))
    return jsonify(all_planets), 200

@app.route('/planets/<int:planet_id>', methods=["GET"])
def get_planet(planet_id):
    single_planet = Planet.query.get(planet_id)
    if single_planet is None:
        raise APIException(f'Planet ID {planet_id} is not found', status_code=404)
    single_planet = single_planet.serialize()
    return jsonify(single_planet), 200


@app.route('/favorites/people', methods=["POST"])
def add_favorite_person():
    data = request.get_json()
    new_favorite_person = Favorite(user_id=data["user_id"], person_id=data["person_id"])
    db.session.add(new_favorite_person)
    db.session.commit()

    return jsonify("Your favorite was added!!!"), 200

@app.route('/favorite/planets', methods=["POST"])
def add_favorite_planet():
    data = request.get_json()
    new_favorite_planet = Favorite(user_id=data["user_id"],planet_id=data["planet_id"])
    db.session.add(new_favorite_planet)
    db.session.commit()

@app.route('/favorite/planets<int:planet_id>', methods=["DELETE"])
def remove_favorite_planet(planet_id):
    remove_planet = Planet.query.get(planet_id)
    db.session.delete(remove_planet)
    db.session.commit()

@app.route('/favorite/people<int:person_id>', methods=["DELETE"])
def remove_favorite_person(person_id):
    remove_person = Character.query.get(person_id)
    db.session.delete(remove_person)
    db.session.commit()

@app.route('/user/<int:user_id>/favorite', methods=["GET"])
def current_favorites(user_id):
    user_favorite = Favorite.query.get(user_id)
    if user_favorite is None:
        raise APIException(f'User ID {user_id} is not found', status_code=404)
    user_favorite = list(map(lambda x: x.serialize(), user_favorite))
    return jsonify(user_favorite),200








# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
