from models import Car_manufacturer, Car_bodystyle, Car_model, Car_stock, car_images

def register_routes(app, db):
    @app.route('/')
    def index():
        # Display the number of manufacturers in the database
        manufacturers = Car_manufacturer.query.all()
        return f"Found {len(manufacturers)} manufacturers in the database. <br><a href='/add-sample'>Add sample data</a> <br><a href='/add-10-cars'>Add 10 sample cars</a>"

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
    def add_10_cars():
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
            
            
            cars = [
                # Toyota Cars
                {
                    "model": Car_model(
                        model_name="Corolla",
                        model_horsepower=140,
                        model_torque=126,
                        eco_rating=9,
                        safety_rating=8,
                        model_seats=5
                    ),
                    "manufacturer": toyota,
                    "bodystyle": sedan,
                    "image": car_images(image="corolla_image.jpg", image_car="Corolla_2021"),
                    "stock": {
                        "year": "2021-03-15",
                        "car_price": 22000,
                        "distance": 15000
                    }
                },
                {
                    "model": Car_model(
                        model_name="RAV4",
                        model_horsepower=203,
                        model_torque=184,
                        eco_rating=7,
                        safety_rating=9,
                        model_seats=5
                    ),
                },
                # Honda Cars
                {
                    "model": Car_model(
                        model_name="Civic",
                        model_horsepower=158,
                        model_torque=138,
                        eco_rating=8,
                        safety_rating=9,
                        model_seats=5
                    ),
                    "manufacturer": honda,
                    "bodystyle": sedan,
                    "image": car_images(image="civic_image.jpg", image_car="Civic_2022"),
                    "stock": {
                        "year": "2022-04-25",
                        "car_price": 23000,
                        "distance": 10000
                    }
                },
                {
                    "model": Car_model(
                        model_name="CR-V",
                        model_horsepower=190,
                        model_torque=179,
                        eco_rating=7,
                        safety_rating=9,
                        model_seats=5
                    ),
                }
            ]
            # Add models, images, and stock to the database
                for car in cars:
                    db.session.add(car["model"])
                    db.session.add(car["image"])
                    db.session.commit()  # Commit to get IDs for foreign keys
                    stock = Car_stock(
                        manufacturer=car["manufacturer"],
                        bodystyle=car["bodystyle"],
                        model=car["model"],
                        year=car["stock"]["year"],
                        car_price=car["stock"]["car_price"],
                        distance=car["stock"]["distance"],
                        image=car["image"]
                    )
                    db.session.add(stock)

                db.session.commit()
                return "6 sample cars <br><a href='/'>Back to home</a>"