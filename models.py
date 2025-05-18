from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base


db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    car_name = Column(String)
    car_price = Column(Integer)
    car_year = Column(Integer)

Base.metadata.create_all(engine)