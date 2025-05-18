from sqlalchemy.orm import sessionmaker

from models import Car, engine

Session = sessionmaker(bind=engine)

session = Session()

car = Car(car_name = "Skyline", car_price = "50000", car_year=2019)
car2 = Car(car_name = "GTR", car_price = "100000", car_year=2020)
car3 = Car(car_name = "Supra", car_price = "60000", car_year=2021)

# Add a single instance of the Car class to the session
session.add(car3)   
# Commits all the session changes (Uncoment line below to add all cars)
# session.add_all([car])

# Commit the session to save the changes to the database
session.commit()

# Access car data
cars = session.query(Car).all()

print(car)