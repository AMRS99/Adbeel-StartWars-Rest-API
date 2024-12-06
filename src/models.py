from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String,unique=False, nullable=False)
    last_name = db.Column(db.String,unique=False, nullable=False)
    email = db.Column(db.String,unique=True, nullable=False)
    password = db.Column(db.Integer,unique=False, nullable=False)
    subscription_date = db.Column(db.String,unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.first_name

    def serialize(self):
        return {
            "id": self.id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "email": self.email,
            "subscription_date":self.subscription_date
            # do not serialize the password, its a security breach
        }
    
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String, unique= False,nullable=False)
    birth_year = db.Column(db.String, unique= False,nullable=False) 
    eye_color = db.Column(db.String, unique= False,nullable=False)
    gender = db.Column(db.String, unique= False,nullable=False)
    hair_color = db.Column(db.String, unique= False,nullable=False)

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year":self.birth_year,
            "eye_color":self.eye_color,
            "gender":self.gender,
            "hair_color":self.hair_color
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    climate = db.Column(db.String, unique= False,nullable=False)
    diameter = db.Column(db.Integer, unique= False,nullable=False)
    gravity = db.Column(db.Integer, unique= False,nullable=False)
    name = db.Column(db.String, unique= False,nullable=False)
    orbital_period = db.Column(db.Integer, unique= False,nullable=False)
    population = db.Column(db.Integer, unique= False,nullable=False)
    rotation_period = db.Column(db.Integer, unique= False,nullable=False)
    surface_water = db.Column(db.Integer, unique= False,nullable=False)
    terrain = db.Column(db.String, unique= False,nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate":self.climate,
            "diameter":self.diameter,
            "gravity":self.gravity,
            "orbital_period":self.orbital_period,
            "population":self.population,
            "rotation_period":self.rotation_period,
            "surface_water":self.surface_water,
            "terrain":self.terrain
            # do not serialize the password, its a security breach
        }
    
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargo_capacity = db.Column(db.Integer, unique= False,nullable=False)
    consumables = db.Column(db.String, unique= False,nullable=False)
    crew = db.Column(db.Integer, unique= False,nullable=False)
    length = db.Column(db.Integer, unique= False,nullable=False)
    manufacturer = db.Column(db.String, unique= False,nullable=False)
    model = db.Column(db.String, unique= False,nullable=False)
    name = db.Column(db.String, unique= False,nullable=False)
    passengers = db.Column(db.Integer, unique= False,nullable=False)

    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "cargo_capacity":self.cargo_capacity,
            "passengers":self.passengers,
            "model":self.model,
            "manufacturer":self.manufacturer,
            "length":self.length,
            "crew":self.crew,
            "consumables":self.consumables
            # do not serialize the password, its a security breach
        }
    
class Favorite(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    user_id =  db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship(User)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    vehicles = db.relationship(Vehicle)
    planet_id = db.Column(db.Integer,db.ForeignKey('planet.id'))
    planets = db.relationship(Planet)
    character_id = db.Column(db.Integer,db.ForeignKey('character.id'))
    characters = db.relationship(Character)

    def __repr__(self):
        return '<Favorite %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicle_id":self.vehicle_id,
            "planet_id":self.planet_id,
            "character_id":self.character_id
            # do not serialize the password, its a security breach
        }