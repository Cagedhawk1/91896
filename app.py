from sqlalchemy.orm import sessionmaker

from models import Car, engine

Session = sessionmaker(bind=engine)

session = Session()

car = Car(car_name = "Skyline", car_price = "50000", car_year=2019)
car2 = Car(car_name = "GTR", car_price = "100000", car_year=2020)
car3 = Car(car_name = "Supra", car_price = "60000", car_year=2021)

# Add a single instance of the Car class to the session (Uncoment line below to add select cars)
# session.add(car3)   
# Commits all the session changes (Uncoment line below to add all cars)
# session.add_all([car])

# Commit the session to save the changes to the database
session.commit()

# Access car data
cars = session.query(Car).filter_by(id=1).all()

# Index position
#cars = cars[0]

#print(cars.id)
print(cars.car_name)
#print(cars.car_price)
#print(cars.car_year)

# Accessing all elements (Everything in the database)
for car in cars:
    print(f"Car ID: {car.id}, Car Name: {car.car_name}, Car Price: {car.car_price}, Car Year: {car.car_year}")