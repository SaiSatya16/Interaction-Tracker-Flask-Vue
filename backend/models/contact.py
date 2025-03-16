from database.db import db
from bson import ObjectId

class Contact:
    @staticmethod
    def add_contact(user_id, name, notes=None, tags=None):
        contact = {
            'user_id': user_id,
            'name': name,
            'notes': notes or [],
            'tags': tags or []
        }
        return db.contacts.insert_one(contact)
    
    @staticmethod
    def get_contacts(user_id):
        return list(db.contacts.find({'user_id': user_id}))
    
    @staticmethod
    def get_contact(contact_id):
        return db.contacts.find_one({'_id': ObjectId(contact_id)})
    
    @staticmethod
    def update_contact(contact_id, data):
        return db.contacts.update_one(
            {'_id': ObjectId(contact_id)},
            {'$set': data}
        )
    
    @staticmethod
    def add_note_to_contact(contact_id, note):
        return db.contacts.update_one(
            {'_id': ObjectId(contact_id)},
            {'$push': {'notes': note}}
        )
    
    @staticmethod
    def delete_contact(contact_id):
        return db.contacts.delete_one({'_id': ObjectId(contact_id)})
