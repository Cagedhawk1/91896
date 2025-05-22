from sqlalchemy.orm import DeclarativeBase, sessionmaker

from models import Car, engine


Session = sessionmaker(bind=engine)

session = Session()

cars = session.query(Car).all()


# Index position
#cars = cars[0]


# Accessing all elements (Everything in the database)

# Update a car
#car_name = "Not Skyline"

# delete a car
# session.delete(car)

# Commit the session to save the changes to the database
session.commit()
