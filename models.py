#from app import DATABASE

#class car(db.Model):
    __tablename__ = 'car_stock'
    
    stock_id = db.Column(db.Integer, primary_key=True)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('car_manufacturer.manufacturer_id'))
    model_id = db.Column(db.Integer, db.ForeignKey('car_model.model_id'))
    bodystyle_id = db.Column(db.Integer, db.ForeignKey('car_bodystyle.bodystyle_id'))
    year = db.Column(db.Integer)
    car_price = db.Column(db.Float)
    distance = db.Column(db.Integer)
    image_id = db.Column(db.Integer, db.ForeignKey('car_images.image_id'))


    def __repr__(self):
        return f'Car with name {self.name} and age {self.age}'

