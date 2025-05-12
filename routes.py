#from flask import Flask,g,render_template, request

from models import car_stock, car_manufacturer, car_model, car_bodystyle, car_images


#def regsister_routes(app, db):

    @app.route("/contents")
    def index():
        cars = car_stock.query.all()
        return str(cars)
