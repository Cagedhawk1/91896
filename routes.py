from models import Car_manufacturer, Car_bodystyle, Car_model, Car_stock, car_images
from datetime import datetime
from flask import render_template


def register_routes(app, db):
    @app.route('/')
    def index():
        # Display the number of manufacturers in the database
        manufacturers = Car_manufacturer.query.all()
        return f"Found {len(manufacturers)} manufacturers in the database. <br><a href='/add-sample'>Add sample data</a> <br><a href='/add-10-cars'>Add 10 sample cars</a>"
    

    @app.route('/cars')
    def cars():
        # get all car with info from the database
        cars = (
            db.session.query(Car_stock)
            .join(Car_model, Car_stock.model_id == Car_model.model_id)
            .join(Car_manufacturer, Car_stock.manufacturer_id == Car_manufacturer.manufacturer_id)
            .join(Car_bodystyle, Car_stock.bodystyle_id == Car_bodystyle.bodystyle_id)
            .join(car_images, Car_stock.image_id == car_images.image_id)
            .all()
        )


        if not cars:
            return "No cars found in the database."
        

        return render_template('cars.html', cars=cars)
    

    @app.route('/add-sample')
    def add_sample():
        # Add a single sample car to the database
        with app.app_context():
            manufacturer = Car_manufacturer(manufacturer_name="Toyota")
            bodystyle = Car_bodystyle(bodystyle_name="Sedan")
            model = Car_model(
                model_name="Camry",
                model_horsepower=200,
                model_torque=180,
                eco_rating=8,
                safety_rating=9,
                model_seats=5
            )
            image = car_images(image="image_data", image_car="Camry_2020")
            stock = Car_stock(
                manufacturer=manufacturer,
                bodystyle=bodystyle,
                model=model,
                year="2020-01-01",
                car_price=25000,
                distance=5000,
                image=image
            )
            db.session.add_all([manufacturer, bodystyle, model, image, stock])
            db.session.commit()
            return "Sample data added! <br><a href='/'>Back to home</a>"

    @app.route('/add-6-cars')
    def add_6_cars():
        with app.app_context():
            # Check if manufacturers already exist
            toyota = Car_manufacturer.query.filter_by(manufacturer_name="Toyota").first()
            if not toyota:
                toyota = Car_manufacturer(manufacturer_name="Toyota")
                db.session.add(toyota)

            honda = Car_manufacturer.query.filter_by(manufacturer_name="Honda").first()
            if not honda:
                honda = Car_manufacturer(manufacturer_name="Honda")
                db.session.add(honda)

            # Check if bodystyles already exist
            sedan = Car_bodystyle.query.filter_by(bodystyle_name="Sedan").first()
            if not sedan:
                sedan = Car_bodystyle(bodystyle_name="Sedan")
                db.session.add(sedan)

            suv = Car_bodystyle.query.filter_by(bodystyle_name="SUV").first()
            if not suv:
                suv = Car_bodystyle(bodystyle_name="SUV")
                db.session.add(suv)

            hatchback = Car_bodystyle.query.filter_by(bodystyle_name="Hatchback").first()
            if not hatchback:
                hatchback = Car_bodystyle(bodystyle_name="Hatchback")
                db.session.add(hatchback)

            # Commit manufacturers and bodystyles
            db.session.commit()
            
            
            cars_data = [
                # Toyota Cars
                {
                    "model_name": "Corolla",
                    "horsepower": 139,
                    "torque": 126,
                    "eco_rating": 8,
                    "safety_rating": 9,
                    "seats": 5,
                    "manufacturer": toyota,
                    "bodystyle": sedan,
                    "year": "2021-01-01",
                    "car_price": 20000,
                    "distance": 15000,
                    "image_name": "corolla_image.jpg",
                
                },
                {
                    "model_name": "Corolla",
                    "horsepower": 139,
                    "torque": 126,
                    "eco_rating": 8,
                    "safety_rating": 9,
                    "seats": 5,
                    "manufacturer": toyota,
                    "bodystyle": sedan,
                    "year": "2021-01-01",
                    "car_price": 20000,
                    "distance": 15000,
                    "image_name": "corolla_image.jpg",
                
                },
                {
                    "model_name": "Corolla",
                    "horsepower": 139,
                    "torque": 126,
                    "eco_rating": 8,
                    "safety_rating": 9,
                    "seats": 5,
                    "manufacturer": toyota,
                    "bodystyle": sedan,
                    "year": "2021-01-01",
                    "car_price": 20000,
                    "distance": 15000,
                    "image_name": "corolla_image.jpg",
                
                },
                {
                    "model_name": "Corolla",
                    "horsepower": 139,
                    "torque": 126,
                    "eco_rating": 8,
                    "safety_rating": 9,
                    "seats": 5,
                    "manufacturer": toyota,
                    "bodystyle": sedan,
                    "year": "2021-01-01",
                    "car_price": 20000,
                    "distance": 15000,
                    "image_name": "corolla_image.jpg",
                
                },
                {
                    "model_name": "Corolla",
                    "horsepower": 139,
                    "torque": 126,
                    "eco_rating": 8,
                    "safety_rating": 9,
                    "seats": 5,
                    "manufacturer": toyota,
                    "bodystyle": sedan,
                    "year": "2021-01-01",
                    "car_price": 20000,
                    "distance": 15000,
                    "image_name": "corolla_image.jpg",
                
                },
                {
                    "model_name": "Corolla",
                    "horsepower": 139,
                    "torque": 126,
                    "eco_rating": 8,
                    "safety_rating": 9,
                    "seats": 5,
                    "manufacturer": toyota,
                    "bodystyle": sedan,
                    "year": "2021-01-01",
                    "car_price": 20000,
                    "distance": 15000,
                    "image_name": "corolla_image.jpg",
                
                },
                {
                    "model_name": "Corolla",
                    "horsepower": 139,
                    "torque": 126,
                    "eco_rating": 8,
                    "safety_rating": 9,
                    "seats": 5,
                    "manufacturer": toyota,
                    "bodystyle": sedan,
                    "year": "2021-01-01",
                    "car_price": 20000,
                    "distance": 15000,
                    "image_name": "corolla_image.jpg",
                
                },
                
            ]


            # Add all data to the database	
            for car_data in cars_data:
                # create model
                model = Car_model(
                    model_name=car_data["model_name"],
                    model_horsepower=car_data["horsepower"],
                    model_torque=car_data["torque"],
                    eco_rating=car_data["eco_rating"],
                    safety_rating=car_data["safety_rating"],
                    model_seats=car_data["seats"]
                )

                # Create image
                image = car_images(
                    image=f"{car_data['image_name']}.jpg",
                    image_car=car_data["image_name"]
                )
                
                db.session.add(model)
                db.session.add(image)
                db.session.commit()  # Commit to get IDs for foreign keys


                stock = Car_stock(
                    manufacturer=car_data["manufacturer"],
                    bodystyle=car_data["bodystyle"],
                    model=model,
                    year=car_data["year"],
                    car_price=car_data["price"],
                    distance=car_data["distance"],
                    image=image
                )

                db.session.add(stock)

            db.session.commit()
            return "6 sample cars <br><a href='/'>Back to home</a>"
