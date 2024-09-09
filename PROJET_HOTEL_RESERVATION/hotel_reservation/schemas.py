from models import db, Chambres, Clients, Reservation

def create_all_tables(app):
    """
    Crée toutes les tables définies dans les modèles SQLAlchemy de `models.py`.
    Cette fonction doit être appelée avec le contexte de l'application Flask.
    """
    with app.app_context():  # Utilise le contexte de l'application Flask
        # Crée toutes les tables définies dans `models.py`
        db.create_all()
        print("Toutes les tables ont été créées avec succès.")
