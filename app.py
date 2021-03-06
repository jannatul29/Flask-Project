import argparse
import os
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from flask import jsonify, abort, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import desc, and_, or_, not_
from functools import wraps
import uuid
import jwt
import datetime
from werkzeug.security import generate_password_hash,check_password_hash


APP = Flask(__name__)
APP.config['SECRET_KEY']='004f2af45d3a4e161a7dd2d17fdae47f'
APP.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/store"
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(APP)
migrate = Migrate(APP, db)

class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String())
    name = db.Column(db.String())
    password = db.Column(db.String())

class store(db.Model):
    __tablename__ = 'hotel1'
    #__tablename__ = 'data1'

    id = db.Column(db.INTEGER, primary_key=True)
    amenities = db.Column(db.String())
    location = db.Column(db.String())
    price = db.Column(db.String())
    rating = db.Column(db.String())
    image = db.Column(db.String())
    herf = db.Column(db.String())
    title = db.Column(db.String())



    def __init__(self, title, herf, image, rating, price, location, amenities):   
        self.amenities = amenities
        self.location = location
        self.price = price
        self.rating = rating
        self.image = image
        self.herf = herf
        self.title = title


    def __repr__(self):
        return f"<Car {self.title}>"


### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Flask Api"
    }
)
APP.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@APP.route('/register', methods=['POST'])
def signup_user(): 
   data = request.get_json() 
   hashed_password = generate_password_hash(data['password'], method='sha256')

   new_user = Users(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password)
   db.session.add(new_user) 
   db.session.commit()   
   return jsonify({'message': 'Registered successfully'})

token = 'key'

@APP.route('/login', methods=['POST']) 
def login_user():
    auth = request.get_json()
    if not auth or not auth['name'] or not auth['password']: 
        return make_response('could not verify', 401, {'Authentication': 'login required"'}) 
        
    user = Users.query.filter_by(name=auth['name']).first()  
    if check_password_hash(user.password, auth['password']):
        global token
        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=40)}, APP.config['SECRET_KEY'], "HS256")
        return jsonify({'Api key' : token})
    else:
        return make_response('could not verify',  401, {'Authentication': '"login required"'})

@APP.route('/search', methods=['GET'])
def search():
    args = request.args
    key = args.get('key')
    title = args.get('title')
    location = args.get('location')
    price = args.get('price')
    pr = "%{}%".format(price)
    amenities = args.get('amenities')
    search = "%{}%".format(amenities)
    sorting = args.get('sorting')

    global token

    if key == token :
        if None not in (title, location, price, amenities, sorting):
            if sorting == 'asc':
                hotel2 = store.query.filter(store.title==title, store.location == location, store.price.like(pr), store.amenities.like(search)).order_by(store.price).all()
            elif sorting == 'dsc':
                hotel2 = store.query.filter(store.title==title, store.location == location, store.price.like(pr), store.amenities.like(search)).order_by(store.price.desc()).all()
        if None not in (title, location, price, amenities):
            hotel2 = store.query.filter(store.title==title, store.location == location, store.price.like(pr), store.amenities.like(search)).all()
        elif None not in (location, price, amenities, sorting):
            if sorting == 'asc':
                hotel2 = store.query.filter(store.location == location, store.price.like(pr), store.amenities.like(search)).order_by(store.price).all()
            elif sorting == 'dsc':
                hotel2 = store.query.filter(store.location == location, store.price.like(pr), store.amenities.like(search)).order_by(store.price.desc()).all()
        elif None not in (title, location, amenities, sorting):
            if sorting == 'asc':
                hotel2 = store.query.filter(store.title==title, store.location == location, store.amenities.like(search)).order_by(store.price).all()
            elif sorting == 'dsc':
                hotel2 = store.query.filter(store.title==title, store.location == location, store.amenities.like(search)).order_by(store.price.desc()).all()
        elif None not in (title, location, price, sorting):
            if sorting == 'asc':
                hotel2 = store.query.filter(store.title==title, store.location == location, store.price.like(pr)).order_by(store.price).all()
            elif sorting == 'dsc':
                hotel2 = store.query.filter(store.title==title, store.location == location, store.price.like(pr)).order_by(store.price.desc()).all() 
        elif None not in (price, amenities, sorting):
            if sorting == 'asc':
                hotel2 = store.query.filter(store.price.like(pr), store.amenities.like(search)).order_by(store.price).all()
            elif sorting == 'dsc':
                hotel2 = store.query.filter(store.price.like(pr), store.amenities.like(search)).order_by(store.price.desc()).all()
        elif None not in (location, amenities, sorting):
            if sorting == 'asc':
                hotel2 = store.query.filter(store.location == location, store.amenities.like(search)).order_by(store.price).all()
            elif sorting == 'dsc':
                hotel2 = store.query.filter(store.location == location, store.amenities.like(search)).order_by(store.price.desc()).all()
        elif None not in (location, price, sorting):
            if sorting == 'asc':
                hotel2 = store.query.filter(store.location == location, store.price.like(pr)).order_by(store.price).all()
            elif sorting == 'dsc':
                hotel2 = store.query.filter(store.location == location, store.price.like(pr)).order_by(store.price.desc()).all()
        elif None not in (location, price, amenities):
            hotel2 = store.query.filter(store.location == location, store.price.like(pr), store.amenities.like(search)).all()
        elif None not in (title, amenities, sorting):
            if sorting == 'asc':
                hotel2 = store.query.filter(store.title==title, store.amenities.like(search)).order_by(store.price).all()
            elif sorting == 'dsc':
                hotel2 = store.query.filter(store.title==title, store.amenities.like(search)).order_by(store.price.desc()).all()
        elif None not in (title, price, sorting):
            if sorting == 'asc':
                hotel2 = store.query.filter(store.title==title, store.price.like(pr)).order_by(store.price).all()
            elif sorting == 'dsc':
                hotel2 = store.query.filter(store.title==title, store.price.like(pr)).order_by(store.price.desc()).all()
        elif None not in (title, price, amenities):
            hotel2 = store.query.filter(store.title==title, store.price.like(pr), store.amenities.like(search)).all()
        elif None not in (title, location, sorting):
            if sorting == 'asc':
                hotel2 = store.query.filter(store.title==title, store.location == location).order_by(store.price).all()
            elif sorting == 'dsc':
                hotel2 = store.query.filter(store.title==title, store.location == location).order_by(store.price.desc()).all()
        elif None not in (title, location, amenities):
            hotel2 = store.query.filter(store.title==title, store.location == location, store.amenities.like(search)).all()
        elif None not in (title, location, price):
            hotel2 = store.query.filter(store.title==title, store.location == location, store.price.like(pr)).all()
        elif None not in (title, sorting):
            if sorting == 'asc':
                hotel2 = store.query.filter(store.title==title).order_by(store.price).all()
            elif sorting == 'dsc':
                hotel2 = store.query.filter(store.title==title).order_by(store.price.desc()).all()
        elif None not in (title, amenities):
            hotel2 = store.query.filter(store.title==title, store.amenities.like(search)).all()
        elif None not in (title, price):
            hotel2 = store.query.filter(store.title==title, store.price.like(pr)).all()   
        elif None not in (title, location):
            hotel2 = store.query.filter(store.title==title, store.location == location).all()
        elif None not in (location, sorting):
            if sorting == 'asc':
                hotel2 = store.query.filter(store.location == location).order_by(store.price).all()
            elif sorting == 'dsc':
                hotel2 = store.query.filter(store.location == location).order_by(store.price.desc()).all()
        elif None not in (location, amenities):
            hotel2 = store.query.filter(store.location == location, store.amenities.like(search)).all()
        elif None not in (location, price):
            hotel2 = store.query.filter(store.location == location, store.price.like(pr)).all()
        elif None not in (price, amenities):
            hotel2 = store.query.filter(store.price.like(pr), store.amenities.like(search)).all()
        elif None not in (price, sorting):
            if sorting == 'asc':
                hotel2 = store.query.filter(store.price.like(pr)).order_by(store.price).all()
            elif sorting == 'dsc':
                hotel2 = store.query.filter(store.price.like(pr)).order_by(store.price.desc()).all()
        elif None not in (amenities, sorting):
            if sorting == 'asc':
                hotel2 = store.query.filter(store.amenities.like(search)).order_by(store.price).all()
            elif sorting == 'dsc':
                hotel2 = store.query.filter(store.amenities.like(search)).order_by(store.price.desc()).all()
        elif title is not None:
            hotel2 = store.query.filter_by(title=title).all()
        elif location is not None:
            hotel2 = store.query.filter_by(location=location).all()
        elif amenities is not None:
            hotel2 = store.query.filter(store.amenities.like(search)).all()
        elif price is not None:
            hotel2 = store.query.filter(store.price.like(pr)).all()
        elif sorting == 'asc' and sorting is not None:
            hotel2 = store.query.order_by(store.price).all()
        elif sorting == 'dsc' and sorting is not None:
            hotel2 = store.query.order_by(store.price.desc()).all()
        elif None in (title, location, price, amenities, sorting):
            hotel2 = store.query.all()
        try:     
            data = jwt.decode(token, APP.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message': 'Api key is invalid. Please login again.'})
        output2 = []
        for hotel in hotel2:
            data2 = {}
            data2['amentites'] = hotel.amenities
            data2['location'] = hotel.location
            data2['price'] = hotel.price
            data2['rating'] = hotel.rating
            data2['image'] = hotel.image
            data2['herf'] = hotel.herf
            data2['title'] = hotel.title
            output2.append(data2)
        #return jsonify(output2)
        if output2 != []:
            return jsonify(output2)
        else:
            return jsonify({'message': 'No data found'})
    else:
        return jsonify({'message': 'Worng api key'})


@APP.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@APP.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@APP.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@APP.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)


if __name__ == '__main__':
    APP.run(debug=True)
