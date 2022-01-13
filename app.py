import argparse
import os
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
#from routes import request_api
from flask import jsonify, abort, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import desc, and_, or_, not_

APP = Flask(__name__)

APP.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/store"
db = SQLAlchemy(APP)
migrate = Migrate(APP, db)

class store(db.Model):
    #__tablename__ = 'test12'
    __tablename__ = 'data1'

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
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
APP.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@APP.route('/search', methods=['GET'])
def search():
    args = request.args
    title = args.get('title')
    location = args.get('location')
    price = args.get('price')
    pr = "%{}%".format(price)
    amenities = args.get('amenities')
    search = "%{}%".format(amenities)
    sorting = args.get('sorting')

    # result = db_users
    if None not in (title, location):
        hotel2 = store.query.filter_by(title=title, location=location).all()
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
    elif None in (title, location):
        hotel2 = store.query.all()
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
    return jsonify(output2)


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


# if __name__ == '__main__':

#     PARSER = argparse.ArgumentParser(
#         description="Seans-Python-Flask-REST-Boilerplate")

#     PARSER.add_argument('--debug', action='store_true',
#                         help="Use flask debug/dev mode with file change reloading")
#     ARGS = PARSER.parse_args()

#     PORT = int(os.environ.get('PORT', 5000))

#     if ARGS.debug:
#         print("Running in debug mode")
#         CORS = CORS(APP)
#         APP.run(host='0.0.0.0', port=PORT, debug=True)
#     else:
#         APP.run(host='0.0.0.0', port=PORT, debug=False)
if __name__ == '__main__':
    APP.run(debug=True)