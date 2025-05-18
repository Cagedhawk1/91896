from sqlalchemy.orm import sessionmaker

from models import Car, engine

Session = sessionmaker(bind=engine)

session = Session()

car = Car(car_name = "Skyline", car_price = "50000", car_year=2019)

session.add(car)   

session.commit()