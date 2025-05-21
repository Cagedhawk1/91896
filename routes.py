from models import Car_manufacturer, Car_bodystyle, Car_model, Car_stock, car_images

def register_routes(app, db):
    @app.route('/')
    def index():
        # Display the number of manufacturers in the database
        manufacturers = Car_manufacturer.query.all()
        return f"Found {len(manufacturers)} manufacturers in the database. <br><a href='/add-sample'>Add sample data</a>"
