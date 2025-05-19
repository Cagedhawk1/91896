from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base


db_url = "sqlite:///database.db"
engine = create_engine(db_url)
Base = declarative_base()

class Car_bodystyle(Base):
    __tablename__ = 'car_bodystyle'
    bodystyle_id = Column(Integer, primary_key=True)
    bodystyle_name = Column(String(50), nullable=False)

    def __repr__(self):
        return f'<Car_bodystyle {self.bodystyle_name}>'

class Car_manufacturer(Base):
    __tablename__ = 'car_manufacturer'
    manufacturer_id = Column(Integer, primary_key=True)
    manufacturer_name = Column(String(100), nullable=False)

    def __repr__(self):
        return f'<Car_manufacturer {self.manufacturer_name}>'

Base.metadata.create_all(engine)