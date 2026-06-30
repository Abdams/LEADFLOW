from flask import Flask
from config import Keys
from .views import views
from .auth import auth
from .extensions import db, migrate

#Create a function "Create_app"
def create_app():
    app = Flask(__name__)
    app.config.from_object(Keys)


    app.register_blueprint(views)
    app.register_blueprint(auth)

    #Start database
    db.init_app(app)
    migrate.init_app(app, db)
 



    return app