from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

db_url = "sqlite:////database.db"
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

class Car_model(Base):
    __tablename__ = 'car_model'
    model_id = Column(Integer, primary_key=True)
    model_name = Column(String(100), nullable=False)
    model_horsepower = Column(Integer)
    model_torque = Column(Integer)
    eco_rating = Column(Integer)
    safety_rating = Column(Integer)
    model_seats = Column(Integer)

    def __repr__(self):
        return f'<Car_model {self.model_name}>'

class Car_stock(Base):
    __tablename__ = 'car_stock'
    stock_id = Column(Integer, primary_key=True)
    manufacturer_id = Column(Integer, ForeignKey('car_manufacturer.manufacturer_id'), nullable=False)
    bodystyle_id = Column(Integer, ForeignKey('car_bodystyle.bodystyle_id'), nullable=False)
    model_id = Column(Integer, ForeignKey('car_model.model_id'), nullable=False)
    year = Column(Date)
    car_price = Column(Integer)
    distance = Column(Integer)
    image_id = Column(Integer, ForeignKey('car_images.image_id'))

    manufacturer = relationship('Car_manufacturer')
    bodystyle = relationship('Car_bodystyle')
    model = relationship('Car_model')
    image = relationship('car_images')

    def __repr__(self):
        return f'<Car_stock {self.stock_id}>'
    
class car_images(Base):
    __tablename__ = 'car_images'
    image_id = Column(Integer, primary_key=True)
    image = Column(String)  
    image_car = Column(String(100))

    def __repr__(self):
        return f'<car_images {self.image_id}>'


Base.metadata.create_all(engine)