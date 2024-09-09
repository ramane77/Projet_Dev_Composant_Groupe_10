from flask import Blueprint, request, jsonify
from models import db, Chambres, Clients, Reservation
from flasgger import swag_from

api = Blueprint('api', __name__)

# Routes pour Chambres

@api.route('/chambres', methods=['GET'])
@swag_from({
    'tags': ['Chambres'],
    'responses': {
        200: {
            'description': 'Liste de toutes les chambres',
            'examples': {
                'application/json': [
                    {
                        "chambre_id": 1,
                        "chambre_number": "101",
                        "chambre_type": "Single",
                        "prix_par_nuit": 100.0,
                        "disponible": True
                    }
                ]
            }
        }
    }
})
def get_chambres():
    chambres = Chambres.query.all()
    return jsonify([chambre.to_dict() for chambre in chambres])

@api.route('/chambres/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Chambres'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID de la chambre'
        }
    ],
    'responses': {
        200: {
            'description': 'Détails de la chambre',
            'examples': {
                'application/json': {
                    "chambre_id": 1,
                    "chambre_number": "101",
                    "chambre_type": "Single",
                    "prix_par_nuit": 100.0,
                    "disponible": True
                }
            }
        }
    }
})
def get_chambre(id):
    chambre = Chambres.query.get_or_404(id)
    return jsonify(chambre.to_dict())

@api.route('/chambres', methods=['POST'])
@swag_from({
    'tags': ['Chambres'],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'chambre_number': {'type': 'string'},
                        'chambre_type': {'type': 'string'},
                        'prix_par_nuit': {'type': 'number'},
                        'disponible': {'type': 'boolean'}
                    },
                    'example': {
                        'chambre_number': '101',
                        'chambre_type': 'Single',
                        'prix_par_nuit': 100.0,
                        'disponible': True
                    }
                }
            }
        }
    },
    'responses': {
        201: {
            'description': 'Chambre ajoutée avec succès',
            'examples': {
                'application/json': {
                    "chambre_id": 1,
                    "chambre_number": "101",
                    "chambre_type": "Single",
                    "prix_par_nuit": 100.0,
                    "disponible": True
                }
            }
        }
    }
})
def add_chambre():
    data = request.json
    new_chambre = Chambres(
        chambre_number=data['chambre_number'], 
        chambre_type=data['chambre_type'], 
        prix_par_nuit=data['prix_par_nuit'], 
        disponible=data.get('disponible', True)
    )
    db.session.add(new_chambre)
    db.session.commit()
    return jsonify(new_chambre.to_dict()), 201

@api.route('/chambres/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Chambres'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID de la chambre'
        }
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'chambre_number': {'type': 'string'},
                        'chambre_type': {'type': 'string'},
                        'prix_par_nuit': {'type': 'number'},
                        'disponible': {'type': 'boolean'}
                    },
                    'example': {
                        'chambre_number': '101',
                        'chambre_type': 'Single',
                        'prix_par_nuit': 100.0,
                        'disponible': True
                    }
                }
            }
        }
    },
    'responses': {
        200: {
            'description': 'Chambre mise à jour avec succès',
            'examples': {
                'application/json': {
                    "chambre_id": 1,
                    "chambre_number": "101",
                    "chambre_type": "Single",
                    "prix_par_nuit": 100.0,
                    "disponible": True
                }
            }
        }
    }
})
def update_chambre(id):
    chambre = Chambres.query.get_or_404(id)
    data = request.json
    chambre.chambre_number = data['chambre_number']
    chambre.chambre_type = data['chambre_type']
    chambre.prix_par_nuit = data['prix_par_nuit']
    chambre.disponible = data.get('disponible', chambre.disponible)
    db.session.commit()
    return jsonify(chambre.to_dict())

@api.route('/chambres/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Chambres'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID de la chambre'
        }
    ],
    'responses': {
        200: {
            'description': 'Chambre supprimée avec succès',
            'examples': {
                'application/json': {
                    'message': 'Chambre supprimée avec succès'
                }
            }
        }
    }
})
def delete_chambre(id):
    chambre = Chambres.query.get_or_404(id)
    db.session.delete(chambre)
    db.session.commit()
    return jsonify({'message': 'Chambre supprimée avec succès'})


# Routes pour Clients

@api.route('/clients', methods=['GET'])
@swag_from({
    'tags': ['Clients'],
    'responses': {
        200: {
            'description': 'Liste de tous les clients',
            'examples': {
                'application/json': [
                    {
                        "id": 1,
                        "nom": "Dupont",
                        "prenom": "Jean",
                        "email": "jean.dupont@example.com",
                        "telephone": "0123456789"
                    }
                ]
            }
        }
    }
})
def get_clients():
    clients = Clients.query.all()
    return jsonify([client.to_dict() for client in clients])

@api.route('/clients/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Clients'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID du client'
        }
    ],
    'responses': {
        200: {
            'description': 'Détails du client',
            'examples': {
                'application/json': {
                    "id": 1,
                    "nom": "Dupont",
                    "prenom": "Jean",
                    "email": "jean.dupont@example.com",
                    "telephone": "0123456789"
                }
            }
        }
    }
})
def get_client(id):
    client = Clients.query.get_or_404(id)
    return jsonify(client.to_dict())

@api.route('/clients', methods=['POST'])
@swag_from({
    'tags': ['Clients'],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'nom': {'type': 'string'},
                        'prenom': {'type': 'string'},
                        'email': {'type': 'string'},
                        'telephone': {'type': 'string'}
                    },
                    'example': {
                        'nom': 'Dupont',
                        'prenom': 'Jean',
                        'email': 'jean.dupont@example.com',
                        'telephone': '0123456789'
                    }
                }
            }
        }
    },
    'responses': {
        201: {
            'description': 'Client ajouté avec succès',
            'examples': {
                'application/json': {
                    "id": 1,
                    "nom": "Dupont",
                    "prenom": "Jean",
                    "email": "jean.dupont@example.com",
                    "telephone": "0123456789"
                }
            }
        }
    }
})
def add_client():
    data = request.json
    new_client = Clients(
        nom=data['nom'], 
        prenom=data['prenom'], 
        email=data['email'], 
        telephone=data['telephone']
    )
    db.session.add(new_client)
    db.session.commit()
    return jsonify(new_client.to_dict()), 201

@api.route('/clients/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Clients'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID du client'
        }
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'nom': {'type': 'string'},
                        'prenom': {'type': 'string'},
                        'email': {'type': 'string'},
                        'telephone': {'type': 'string'}
                    },
                    'example': {
                        'nom': 'Dupont',
                        'prenom': 'Jean',
                        'email': 'jean.dupont@example.com',
                        'telephone': '0123456789'
                    }
                }
            }
        }
    },
    'responses': {
        200: {
            'description': 'Client mis à jour avec succès',
            'examples': {
                'application/json': {
                    "id": 1,
                    "nom": "Dupont",
                    "prenom": "Jean",
                    "email": "jean.dupont@example.com",
                    "telephone": "0123456789"
                }
            }
        }
    }
})
def update_client(id):
    client = Clients.query.get_or_404(id)
    data = request.json
    client.nom = data['nom']
    client.prenom = data['prenom']
    client.email = data['email']
    client.telephone = data['telephone']
    db.session.commit()
    return jsonify(client.to_dict())

@api.route('/clients/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Clients'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID du client'
        }
    ],
    'responses': {
        200: {
            'description': 'Client supprimé avec succès',
            'examples': {
                'application/json': {
                    'message': 'Client supprimé avec succès'
                }
            }
        }
    }
})
def delete_client(id):
    client = Clients.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    return jsonify({'message': 'Client supprimé avec succès'})


# Routes pour Reservation

@api.route('/reservations', methods=['GET'])
@swag_from({
    'tags': ['Reservations'],
    'responses': {
        200: {
            'description': 'Liste de toutes les réservations',
            'examples': {
                'application/json': [
                    {
                        "id": 1,
                        "chambre_id": 1,
                        "client_id": 1,
                        "date_entree": "2024-09-01",
                        "date_sortie": "2024-09-05",
                        "status": "Confirmé"
                    }
                ]
            }
        }
    }
})
def get_reservations():
    reservations = Reservation.query.all()
    return jsonify([reservation.to_dict() for reservation in reservations])

@api.route('/reservations/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Reservations'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID de la réservation'
        }
    ],
    'responses': {
        200: {
            'description': 'Détails de la réservation',
            'examples': {
                'application/json': {
                    "id": 1,
                    "chambre_id": 1,
                    "client_id": 1,
                    "date_entree": "2024-09-01",
                    "date_sortie": "2024-09-05",
                    "status": "Confirmé"
                }
            }
        }
    }
})
def get_reservation(id):
    reservation = Reservation.query.get_or_404(id)
    return jsonify(reservation.to_dict())

@api.route('/reservations', methods=['POST'])
@swag_from({
    'tags': ['Reservations'],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'chambre_id': {'type': 'integer'},
                        'client_id': {'type': 'integer'},
                        'date_entree': {'type': 'string', 'format': 'date'},
                        'date_sortie': {'type': 'string', 'format': 'date'},
                        'status': {'type': 'string'}
                    },
                    'example': {
                        'chambre_id': 1,
                        'client_id': 1,
                        'date_entree': '2024-09-01',
                        'date_sortie': '2024-09-05',
                        'status': 'Confirmé'
                    }
                }
            }
        }
    },
    'responses': {
        201: {
            'description': 'Réservation ajoutée avec succès',
            'examples': {
                'application/json': {
                    "id": 1,
                    "chambre_id": 1,
                    "client_id": 1,
                    "date_entree": "2024-09-01",
                    "date_sortie": "2024-09-05",
                    "status": "Confirmé"
                }
            }
        }
    }
})
def add_reservation():
    data = request.json
    new_reservation = Reservation(
        chambre_id=data['chambre_id'], 
        client_id=data['client_id'], 
        date_entree=data['date_entree'], 
        date_sortie=data['date_sortie'], 
        status=data['status']
    )
    db.session.add(new_reservation)
    db.session.commit()
    return jsonify(new_reservation.to_dict()), 201

@api.route('/reservations/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Reservations'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID de la réservation'
        }
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'chambre_id': {'type': 'integer'},
                        'client_id': {'type': 'integer'},
                        'date_entree': {'type': 'string', 'format': 'date'},
                        'date_sortie': {'type': 'string', 'format': 'date'},
                        'status': {'type': 'string'}
                    },
                    'example': {
                        'chambre_id': 1,
                        'client_id': 1,
                        'date_entree': '2024-09-01',
                        'date_sortie': '2024-09-05',
                        'status': 'Confirmé'
                    }
                }
            }
        }
    },
    'responses': {
        200: {
            'description': 'Réservation mise à jour avec succès',
            'examples': {
                'application/json': {
                    "id": 1,
                    "chambre_id": 1,
                    "client_id": 1,
                    "date_entree": "2024-09-01",
                    "date_sortie": "2024-09-05",
                    "status": "Confirmé"
                }
            }
        }
    }
})
def update_reservation(id):
    reservation = Reservation.query.get_or_404(id)
    data = request.json
    reservation.chambre_id = data['chambre_id']
    reservation.client_id = data['client_id']
    reservation.date_entree = data['date_entree']
    reservation.date_sortie = data['date_sortie']
    reservation.status = data['status']
    db.session.commit()
    return jsonify(reservation.to_dict())

@api.route('/reservations/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Reservations'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID de la réservation'
        }
    ],
    'responses': {
        200: {
            'description': 'Réservation supprimée avec succès',
            'examples': {
                'application/json': {
                    'message': 'Réservation supprimée avec succès'
                }
            }
        }
    }
})
def delete_reservation(id):
    reservation = Reservation.query.get_or_404(id)
    db.session.delete(reservation)
    db.session.commit()
    return jsonify({'message': 'Réservation supprimée avec succès'})
