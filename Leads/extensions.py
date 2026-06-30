#importing sqlalchemy for database
from flask_sqlalchemy import SQLAlchemy
#import migrate to describe change in database
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
