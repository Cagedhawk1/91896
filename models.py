from app import DATABASE

class car(db.Model):
    __tablename__ = 'car_stock'


    pid = db.Column(*args: db.Interger, primary_key=True) 
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)
    age = db.Column(db.Text )

    def __repr__(self):
        return f'Car with name {self.name} and age {self.age}'
    