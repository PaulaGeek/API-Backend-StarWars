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
from models import db, User, Characters, Planets, Vehicles, Favs
#_______ Importo JWT________
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

#______________________________________

# Estoy instalado una extensión de Flask-JWT-Extended: (siempre)
app.config["JWT_SECRET_KEY"] = "super-secret" 
jwt = JWTManager(app)

#______________________________

# Handle/serialize errors like a JSON object/ 
# Manejar/serializar errores como un objeto JSON

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints

@app.route('/')
def sitemap():
    return generate_sitemap(app)

#___________________________________________________


# Cree una ruta para autenticar a sus usuarios y devolver JWT. Él
# La función create_access_token() se usa para generar realmente el JWT.

@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if email != user.email or password != user.password:
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

# Proteja una ruta con jwt_required, que eliminará las solicitudes
# sin un JWT válido presente.

@app.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


if __name__ == "__main__":
    app.run()

# ____________________________________















 #_____________________________________

@app.route('/characters', methods=['GET'])
def personajes():

    allpersoajes = Characters.query.all()
    results = list(map(lambda item: item.serialize(), allpersoajes))

    return jsonify(results), 200

# obteniendo info de un solo personaje:

@app.route('/characters/<int:character_id>', methods=['GET'])
def get_info_personaje(character_id):

    characters = Characters.query.filter_by(id=character_id).first()
    return jsonify(characters.serialize()), 200

#________________________________________________________________


@app.route('/characters', methods=['POST'])
def add_new_todo():

    me = User('admin', 'admin@example.com') 
    db.session.add(me)
    db.session.commit()


    return jsonify(todos)

#_______________________________________

@app.route('/favs', methods=['GET'])
def handle_favs():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# _____________________________________


@app.route('/planets', methods=['GET'])
def planetas():

    allplanetas = Planets.query.all()
    results = list(map(lambda item: item.serialize(), allplanetas))

    return jsonify(results), 200

# obteniendo info de un solo planeta:


@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_info_planet(character_id):

    planets = Planets.query.filter_by(id=planet_id).first()
    return jsonify(planets.serialize()), 200

# _____________________________________________


@app.route('/vehicles', methods=['GET'])
def vehiculos():

    allvehicles = Vehicles.query.all()
    results = list(map(lambda item: item.serialize(), allvehicles))

    return jsonify(results), 200

# obteniendo info de un solo vehiculo:


@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_info_vehicle(vehicle_id):

    vehicles = Vehicles.query.filter_by(id=vehicle_id).first()
    return jsonify(vehicles.serialize()), 200

# ________________________________________________________________________________________
#     Este codígo tiene que estar siempre al final de cada CODE en el que uso Flask?    #
# ________________________________________________________________________________________

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
