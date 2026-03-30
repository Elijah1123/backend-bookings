import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:new_password@localhost:5432/mzalendo_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_super_secret_key'
    STRIPE_SECRET_KEY = 'sk_test_your_key_here'