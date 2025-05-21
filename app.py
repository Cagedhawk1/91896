from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Start SQLAlchemy and Migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Import models
    from models import Car_bodystyle, Car_manufacturer, Car_model, Car_stock, car_images

    # Import routes
    from routes import register_routes
    register_routes(app, db)

    # Start migrations
    migrate.init_app(app, db)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/mail/Documents/database.db'

# Add a single instance of the Car class to the session (Uncoment line below to add select cars)
# session.add(car3)   
# Commits all the session changes (Uncoment line below to add all cars)
# session.add_all([car])

# Commit the session to save the changes to the database

# Access car data
# cars = session.query(Car_stock).all()

# Index position
#cars = cars[0]

#print(cars.id)
#print(cars.car_name)
#print(cars.car_price)
#print(cars.car_year)

# Accessing all elements (Everything in the database)
#for car in cars:
    #print(f"Car ID: {car.id}, Car Name: {car.car_name}, Car Price: {car.car_price}, Car Year: {car.car_year}")

# Update a car
#car_name = "Not Skyline"

# delete a car
# session.delete(car)

# Commit the session to save the changes to the database
#session.commit()

#with engine.connect() as connection:
    #result = connection.execute("SELECT name FROM sqlite_master WHERE type='table';")
    #print(result.fetchall())