# config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/reservation_hotel'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
