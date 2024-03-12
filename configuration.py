from routes.show_data import data_route
from routes.avaliate import avaliate_route
from database.database import db
from database.models.laudo import Laudo

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(data_route)
    app.register_blueprint(avaliate_route)

def configure_db():
    db.connect()
    
    db.create_tables([Laudo])