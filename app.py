import os
from flask import Flask
from models import db  # import db SQLAlchemy and models
from routes import register_routes  # function that registers Flask routes

def create_app():
    # Create the app
    app = Flask(__name__, instance_relative_config=True)
    
    # check if instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # database path (in the instance folder)
    DB_FILENAME = 'database.db'
    DB_PATH = os.path.join(app.instance_path, DB_FILENAME)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize plugins
    db.init_app(app)

    # CREATE DB ONLY IF IT DOESN'T EXIST
    with app.app_context():
        if not os.path.exists(DB_PATH):
            db.create_all()

    # Register routes
    register_routes(app, db)
    
    return app

if __name__ == "__main__":
    # create the app again?
    app = create_app()
    app.run(debug=True)