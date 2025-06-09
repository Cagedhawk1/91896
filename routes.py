from models import Car_manufacturer, Car_bodystyle, Car_model, Car_stock, car_images
from datetime import datetime
from flask import Flask,g,render_template, request, redirect
import sqlite3

def register_routes(app, db):



    @app.route("/")
    def home():
        return render_template("home.html")
    

    @app.route("/contents")
    def contents():
        query = request.args.get('query', '')
        conn = sqlite3.connect('instance\database.db')
        cursor = conn.cursor()
        
        if query:
            cursor.execute('''
                SELECT * FROM car_stock
                JOIN car_manufacturer ON car_stock.manufacturer_id = car_manufacturer.manufacturer_id
                JOIN car_bodystyle ON car_stock.bodystyle_id = car_bodystyle.bodystyle_id
                JOIN car_model ON car_stock.model_id = car_model.model_id
                JOIN car_images ON car_stock.image_id = car_images.image_id
                WHERE car_manufacturer.manufacturer_name LIKE ? OR car_model.model_name LIKE ?
                ''', ('%' + query + '%', '%' + query + '%'))
        else:
            cursor.execute('''
                SELECT * FROM car_stock
                JOIN car_manufacturer ON car_stock.manufacturer_id = car_manufacturer.manufacturer_id
                JOIN car_bodystyle ON car_stock.bodystyle_id = car_bodystyle.bodystyle_id
                JOIN car_model ON car_stock.model_id = car_model.model_id
                JOIN car_images ON car_stock.image_id = car_images.image_id
            ''')

        results = cursor.fetchall()
        conn.close()
        return render_template("contents.html", cars=results)

    #@app.route('/')
    #def index():
        # Display the number of manufacturers in the database
        #manufacturers = Car_manufacturer.query.all()
        #return f"Found {len(manufacturers)} manufacturers in the database. <br><a href='/add-sample'>Add sample data</a> <br><a href='/add-10-cars'>Add 10 sample cars</a>"

    @app.route('/cars')
    def cars():
            # Get all cars with their related information
            cars = (
                db.session.query(Car_stock)
                .join(Car_manufacturer, Car_stock.manufacturer_id == Car_manufacturer.manufacturer_id)
                .join(Car_bodystyle, Car_stock.bodystyle_id == Car_bodystyle.bodystyle_id)
                .join(Car_model, Car_stock.model_id == Car_model.model_id)
                .join(car_images, Car_stock.image_id == car_images.image_id)
                .all()
            )
            
            if not cars:
                return "No cars found in the database. <br><a href='/'>Back to home</a> <br><a href='/add-10-cars'>Add sample cars</a>"
            
            return render_template('cars_template.html', cars=cars)


    @app.route('/add-listing', methods=['GET', 'POST'])
    def add_listing():
        if request.method == 'POST':
            manufacturer_name = request.form['manufacturer']
            bodystyle_name = request.form['bodystyle']
            car_name = request.form['car_name']
            horsepower = int(request.form['horsepower'])
            torque = int(request.form['torque'])
            eco_rating = int(request.form['eco_rating'])
            safety_rating = int(request.form['safety_rating'])
            seats = int(request.form['seats'])
            year = datetime.strptime(request.form['year'], "%Y").date()  
            price = float(request.form['price'])
            distance = int(request.form['distance'])
            image_data = request.files['image'].read()  

            # Create data 
            manufacturer = Car_manufacturer(manufacturer_name=manufacturer_name)
            bodystyle = Car_bodystyle(bodystyle_name=bodystyle_name)
            model = Car_model(
                model_name=car_name,
                model_horsepower=horsepower,
                model_torque=torque,
                eco_rating=eco_rating,
                safety_rating=safety_rating,
                model_seats=seats
            )
            image = car_images(image=image_data, image_car=f"{car_name}_{year.year}")
            stock = Car_stock(
                manufacturer=manufacturer,
                bodystyle=bodystyle,
                model=model,
                year=year,
                car_price=price,
                distance=distance,
                image=image
            )

            # Commit to database
            db.session.add_all([manufacturer, bodystyle, model, image, stock])
            db.session.commit()

            return redirect('/contents')  

        return render_template("add-listing.html")
    



    @app.route('/add-sample')
    def add_sample():
        # Add a single sample car to the database
        manufacturer = Car_manufacturer(manufacturer_name="Toyota")
        bodystyle = Car_bodystyle(bodystyle_name="Sedan")
        model = Car_model(
            model_name="Camry",
            model_horsepower=200,
            model_torque=180,
            eco_rating=8,
            safety_rating=9,
            model_seats=5
        )
        image = car_images(image="image_data", image_car="Camry_2020")
        stock = Car_stock(
            manufacturer=manufacturer,
            bodystyle=bodystyle,
            model=model,
            year=datetime.strptime("2020-01-01", "%Y-%m-%d").date(),
            car_price=25000,
            distance=5000,
            image=image
        )
        db.session.add_all([manufacturer, bodystyle, model, image, stock])
        db.session.commit()
        return "Sample data added! <br><a href='/contents'>Back to home</a>"
    
    @app.route('/add-10-cars')
    def add_10_cars():
        # Check if manufacturers already exist
        toyota = Car_manufacturer.query.filter_by(manufacturer_name="Toyota").first()
        if not toyota:
            toyota = Car_manufacturer(manufacturer_name="Toyota")
            db.session.add(toyota)

        honda = Car_manufacturer.query.filter_by(manufacturer_name="Honda").first()
        if not honda:
            honda = Car_manufacturer(manufacturer_name="Honda")
            db.session.add(honda)

        ford = Car_manufacturer.query.filter_by(manufacturer_name="Ford").first()
        if not ford:
            ford = Car_manufacturer(manufacturer_name="Ford")
            db.session.add(ford)

        # Check if bodystyles already exist
        sedan = Car_bodystyle.query.filter_by(bodystyle_name="Sedan").first()
        if not sedan:
            sedan = Car_bodystyle(bodystyle_name="Sedan")
            db.session.add(sedan)

        suv = Car_bodystyle.query.filter_by(bodystyle_name="SUV").first()
        if not suv:
            suv = Car_bodystyle(bodystyle_name="SUV")
            db.session.add(suv)

        hatchback = Car_bodystyle.query.filter_by(bodystyle_name="Hatchback").first()
        if not hatchback:
            hatchback = Car_bodystyle(bodystyle_name="Hatchback")
            db.session.add(hatchback)

        # Commit manufacturers and bodystyles first
        db.session.commit()
        
        # Create 10 cars with complete data
        cars_data = [
            # Toyota Cars
            {
                "model_name": "Corolla",
                "horsepower": 140,
                "torque": 126,
                "eco_rating": 9,
                "safety_rating": 8,
                "seats": 5,
                "manufacturer": toyota,
                "bodystyle": sedan,
                "year": datetime.strptime("2021-03-15", "%Y-%m-%d").date(),
                "price": 22000,
                "distance": 15000,
                "image_name": "Corolla_2021"
            },
            {
                "model_name": "RAV4",
                "horsepower": 203,
                "torque": 184,
                "eco_rating": 7,
                "safety_rating": 9,
                "seats": 5,
                "manufacturer": toyota,
                "bodystyle": suv,
                "year": datetime.strptime("2021-06-10", "%Y-%m-%d").date(),
                "price": 28000,
                "distance": 12000,
                "image_name": "RAV4_2021"
            },
            {
                "model_name": "Prius",
                "horsepower": 121,
                "torque": 105,
                "eco_rating": 10,
                "safety_rating": 8,
                "seats": 5,
                "manufacturer": toyota,
                "bodystyle": hatchback,
                "year": datetime.strptime("2022-01-20", "%Y-%m-%d").date(),
                "price": 26000,
                "distance": 8000,
                "image_name": "Prius_2022"
            },
            # Honda Cars
            {
                "model_name": "Civic",
                "horsepower": 158,
                "torque": 138,
                "eco_rating": 8,
                "safety_rating": 9,
                "seats": 5,
                "manufacturer": honda,
                "bodystyle": sedan,
                "year": datetime.strptime("2022-04-25", "%Y-%m-%d").date(),
                "price": 23000,
                "distance": 10000,
                "image_name": "Civic_2022"
            },
            {
                "model_name": "CR-V",
                "horsepower": 190,
                "torque": 179,
                "eco_rating": 7,
                "safety_rating": 9,
                "seats": 5,
                "manufacturer": honda,
                "bodystyle": suv,
                "year": datetime.strptime("2021-08-12", "%Y-%m-%d").date(),
                "price": 27000,
                "distance": 18000,
                "image_name": "CRV_2021"
            },
            {
                "model_name": "Accord",
                "horsepower": 192,
                "torque": 192,
                "eco_rating": 8,
                "safety_rating": 9,
                "seats": 5,
                "manufacturer": honda,
                "bodystyle": sedan,
                "year": datetime.strptime("2020-11-30", "%Y-%m-%d").date(),
                "price": 24500,
                "distance": 22000,
                "image_name": "Accord_2020"
            },
            {
                "model_name": "Fit",
                "horsepower": 130,
                "torque": 114,
                "eco_rating": 9,
                "safety_rating": 7,
                "seats": 5,
                "manufacturer": honda,
                "bodystyle": hatchback,
                "year": datetime.strptime("2021-02-14", "%Y-%m-%d").date(),
                "price": 18000,
                "distance": 25000,
                "image_name": "Fit_2021"
            },
            # Ford Cars
            {
                "model_name": "Mustang",
                "horsepower": 310,
                "torque": 350,
                "eco_rating": 5,
                "safety_rating": 7,
                "seats": 4,
                "manufacturer": ford,
                "bodystyle": sedan,
                "year": datetime.strptime("2021-05-18", "%Y-%m-%d").date(),
                "price": 35000,
                "distance": 8500,
                "image_name": "Mustang_2021"
            },
            {
                "model_name": "Explorer",
                "horsepower": 300,
                "torque": 310,
                "eco_rating": 6,
                "safety_rating": 8,
                "seats": 7,
                "manufacturer": ford,
                "bodystyle": suv,
                "year": datetime.strptime("2020-09-22", "%Y-%m-%d").date(),
                "price": 32000,
                "distance": 30000,
                "image_name": "Explorer_2020"
            },
            {
                "model_name": "Focus",
                "horsepower": 160,
                "torque": 146,
                "eco_rating": 8,
                "safety_rating": 8,
                "seats": 5,
                "manufacturer": ford,
                "bodystyle": hatchback,
                "year": datetime.strptime("2021-12-05", "%Y-%m-%d").date(),
                "price": 20000,
                "distance": 15500,
                "image_name": "Focus_2021"
            }
        ]

        # Add all cars to the database
        for car_data in cars_data:
            # Create model
            model = Car_model(
                model_name=car_data["model_name"],
                model_horsepower=car_data["horsepower"],
                model_torque=car_data["torque"],
                eco_rating=car_data["eco_rating"],
                safety_rating=car_data["safety_rating"],
                model_seats=car_data["seats"]
            )
            
            # Create image
            image = car_images(
                image=f"{car_data['image_name']}.jpg",
                image_car=car_data["image_name"]
            )
            
            # Add model and image to session
            db.session.add(model)
            db.session.add(image)
            db.session.commit()  # Commit to get IDs for foreign keys
            
            # Create stock entry
            stock = Car_stock(
                manufacturer=car_data["manufacturer"],
                bodystyle=car_data["bodystyle"],
                model=model,
                year=car_data["year"],
                car_price=car_data["price"],
                distance=car_data["distance"],
                image=image
            )
            
            db.session.add(stock)

        db.session.commit()
        return "10 sample cars added successfully! <br><a href='/contents'>Back to home</a>"