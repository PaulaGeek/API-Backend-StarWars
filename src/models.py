from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    favs = db.relationship('Favs', backref='user', lazy=True)


    def __repr__(self):
        return '<User %r>' % self.id
        

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            # do not serialize the password, its a security breach
        }

# ______________________________________

class Favs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=True)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=True)
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=True)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            # do not serialize the password, its a security breach
        }

#___________________________________________

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    hairColor = db.Column(db.String(250), nullable=True)
    gender = db.Column(db.String(250), nullable=True)
    favs = db.relationship('Favs', backref='characters', lazy=True)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            # do not serialize the password, its a security breach
        }

#___________________________________________

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    favs = db.relationship('Favs', backref='planets', lazy=True)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            # do not serialize the password, its a security breach
        }

#_______________________________________________

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    crew = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    favs = db.relationship('Favs', backref='vehicles', lazy=True)

    def __repr__(self):
        return '<Vehicles %r>' % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "crew": self.crew,
            "model": self.model,
            # do not serialize the password, its a security breach
        }

 #______________________________