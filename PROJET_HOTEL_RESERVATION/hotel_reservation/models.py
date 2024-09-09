from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Chambres(db.Model):
    __tablename__ = 'chambres'
    chambre_id = db.Column(db.Integer, primary_key=True)
    chambre_number = db.Column(db.String(50), nullable=False)
    chambre_type = db.Column(db.String(50), nullable=False)
    prix_par_nuit = db.Column(db.Float, nullable=False)
    disponible = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'chambre_id': self.chambre_id,
            'chambre_number': self.chambre_number,
            'chambre_type': self.chambre_type,
            'prix_par_nuit': self.prix_par_nuit,
            'disponible': self.disponible
        }

class Clients(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telephone = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'prenom': self.prenom,
            'email': self.email,
            'telephone': self.telephone
        }

class Reservation(db.Model):
    __tablename__ = 'reservation'
    id = db.Column(db.Integer, primary_key=True)
    chambre_id = db.Column(db.Integer, db.ForeignKey('chambres.chambre_id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    date_entree = db.Column(db.Date, nullable=False)
    date_sortie = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    chambre = db.relationship('Chambres', backref=db.backref('reservations', lazy=True))
    client = db.relationship('Clients', backref=db.backref('reservations', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'chambre_id': self.chambre_id,
            'client_id': self.client_id,
            'date_entree': self.date_entree.isoformat(),
            'date_sortie': self.date_sortie.isoformat(),
            'status': self.status
        }
