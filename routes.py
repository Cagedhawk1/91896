from models import Car_manufacturer, Car_bodystyle, Car_model, Car_stock, car_images

def register_routes(app, db):
    @app.route('/')
    def index():
        # Display the number of manufacturers in the database
        manufacturers = Car_manufacturer.query.all()
        return f"Found {len(manufacturers)} manufacturers in the database. <br><a href='/add-sample'>Add sample data</a>"
    @app.route('/add-sample')
    def add_sample():
        # Add data to the database
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