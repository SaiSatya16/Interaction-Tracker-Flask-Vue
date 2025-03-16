from database.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    @staticmethod
    def add_user(username, email, password):
        user = {
            'username': username,
            'email': email,
            'password': generate_password_hash(password)
        }
        return db.users.insert_one(user)
    
    @staticmethod
    def find_by_email(email):
        return db.users.find_one({'email': email})
    
    @staticmethod
    def check_password(user, password):
        return check_password_hash(user['password'], password)
