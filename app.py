from flask import Flask, render_template, request, redirect, url_for , jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import desc
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/store"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class CarsModel(db.Model):
    __tablename__ = 'test12'

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

@app.route('/')
def home_route():
    hotels = CarsModel.query.all()
    output = []
    for hotel in hotels:
        data = {}
        data['amentites'] = hotel.amenities
        data['location'] = hotel.location
        data['price'] = hotel.price
        data['rating'] = hotel.rating
        data['image'] = hotel.image
        data['herf'] = hotel.herf
        data['title'] = hotel.title
        output.append(data)
    return jsonify(output)

@app.route('/name=<string:title>', methods=['GET'])
def get_product(title):
    hotel2 = CarsModel.query.filter_by(title=title).all()
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

@app.route('/location=<string:location>', methods=['GET'])
def get_product1(location):
    hotel3 = CarsModel.query.filter_by(location=location).all()
    output3 = []
    for hotel in hotel3:
        data3 = {}
        data3['amentites'] = hotel.amenities
        data3['location'] = hotel.location
        data3['price'] = hotel.price
        data3['rating'] = hotel.rating
        data3['image'] = hotel.image
        data3['herf'] = hotel.herf
        data3['title'] = hotel.title
        output3.append(data3)
    return jsonify(output3)

@app.route('/pricea', methods=['GET'])
def get_product2():
    hotel4 = CarsModel.query.order_by(CarsModel.price).all()
    output4 = []
    for hotel in hotel4:
        data4 = {}
        data4['amentites'] = hotel.amenities
        data4['location'] = hotel.location
        data4['price'] = hotel.price
        data4['rating'] = hotel.rating
        data4['image'] = hotel.image
        data4['herf'] = hotel.herf
        data4['title'] = hotel.title
        output4.append(data4)
    return jsonify(output4)

@app.route('/price_dsc', methods=['GET'])
def get_product3():
    hotel5 = CarsModel.query.order_by(CarsModel.price.desc()).all()
    output5 = []
    for hotel in hotel5:
        data5 = {}
        data5['amentites'] = hotel.amenities
        data5['location'] = hotel.location
        data5['price'] = hotel.price
        data5['rating'] = hotel.rating
        data5['image'] = hotel.image
        data5['herf'] = hotel.herf
        data5['title'] = hotel.title
        output5.append(data5)
    return jsonify(output5)

if __name__ == '__main__':
    app.run(debug=True)