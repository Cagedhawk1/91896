from flask import Flask,g,render_template, request
from models import db
from routes import register_routes
import sqlite3
from sqlalchemy import create_engine
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, 'instance', 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
register_routes(app, db)

if __name__ == "__main__":
    # Ensure instance folder exists
    os.makedirs(os.path.join(BASE_DIR, 'instance'), exist_ok=True)
    with app.app_context():
        db.create_all()
    app.run(debug=True)


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, 'instance', 'database.db')

conn = sqlite3.connect(db_path)


app = Flask(__name__)

DATABASE = 'southeys_autoworld_database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()





# Create Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Register routes
register_routes(app, db)

# Create tables
with app.app_context():
    db.create_all()




if __name__ == "__main__":
    app.run(debug=True)

    #engine = create_engine('sqlite:///southeys_autoworld_database.db', echo=True)

    


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

    