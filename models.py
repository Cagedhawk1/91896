from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base


db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    car_model = Column(String)
    seller_name = Column(String)
    car_location = Column(String)
    car_description = Column(String)
    car_condition = Column(String)
    car_color = Column(String)
    car_price = Column(Integer)
    car_year = Column(Integer)
    car_mileage = Column(Integer)
    car_bodystyle = Column(String)
    car_manufacturer = Column(String)
    car_image1 = Column(String)
    car_image2 = Column(String)
    car_image3 = Column(String)
    car_image4 = Column(String)
    car_image5 = Column(String)
    car_image6 = Column(String)
    car_image7 = Column(String)
    car_image8 = Column(String)
    car_image9 = Column(String)
    car_image10 = Column(String)


Base.metadata.create_all(engine)