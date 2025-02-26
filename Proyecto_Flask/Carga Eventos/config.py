import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://apsa:Apsa2812p.@192.168.0.12:5432/db_mto'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'supersecreto'
