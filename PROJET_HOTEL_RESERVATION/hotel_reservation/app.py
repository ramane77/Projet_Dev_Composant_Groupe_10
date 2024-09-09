from flask import Flask
from flasgger import Swagger
from models import db
from config import Config
from schemas import create_all_tables  # Import de la fonction de création des tables
from routes import api 
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialiser la base de données avec SQLAlchemy
    db.init_app(app)
    
    # Initialiser Swagger
    swagger = Swagger(app)

        # Enregistrer le Blueprint
    app.register_blueprint(api, url_prefix='/api')  # Le préfixe /api est optionnel

    return app

app = create_app()

# Appel pour créer les tables après avoir initialisé l'application
with app.app_context():
    create_all_tables(app)

if __name__ == '__main__':
    app.run(debug=True)
