from flask import Blueprint, request, jsonify
from car_collection.helpers import token_required
from car_collection.models import db, User, Car, car_schema, cars_schema

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
@token_required
def get_data(current_user_token):
    return {'some': 'value'}

# Create Car Endpoint
@api.route('/cars', methods = ['POST'])
@token_required
def create_car(current_user_token):
    year = request.json['year']
    car_make = request.json['car_make']
    car_model = request.json['car_model']
    color = request.json['color']
    name = request.json['name']
    horsepower = request.json['horsepower']
    top_speed = request.json['top_speed']
    modifications = request.json['modifications']
    user_token = current_user_token.token

    car = Car(year, car_make, car_model, color, name, horsepower, top_speed, modifications, user_token)
    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)


#  Retrieve All Cars Endpoint
@api.route('/cars', methods = ['GET'])
@token_required
def get_cars(current_user_token):
    owner = current_user_token.token
    cars = Car.query.filter_by(user_token = owner).all()
    response = cars_schema.dump(cars)
    return jsonify(response)


# Retrieve One Car Endpoint
@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_car(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        car = Car.query.get(id)
        response = car_schema.dump(car)
        return jsonify(response)
    else:
        return jsonify({'message' : 'Valid Token Required'}), 401


# Update Drone Endpoint
@api.route('/cars/<id>', methods = ['POST', 'PUT'])
@token_required
def update_drone(current_user_token, id):
    car = Car.query.get(id) # Get Drone Instance


    car.year = request.json['year']
    car.car_make = request.json['car_make']
    car.car_model = request.json['car_model']
    car.color = request.json['color']
    car.name = request.json['name']
    car.horsepower = request.json['horsepower']
    car.top_speed = request.json['top_speed']
    car.modifications = request.json['modifications']
    car.user_token = current_user_token.token

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)


# Delete Drone Endpoint
@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)