import datetime
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.contact import Contact
from models.interaction import Interaction
from bson import ObjectId

class ContactsApi(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        contacts = Contact.get_contacts(user_id)
        
        # Convert ObjectId to string for JSON serialization
        for contact in contacts:
            contact['_id'] = str(contact['_id'])
        
        return contacts, 200
    
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        
        contact = Contact.add_contact(
            user_id=user_id,
            name=body.get('name'),
            notes=body.get('notes'),
            tags=body.get('tags')
        )
        
        return {'id': str(contact.inserted_id)}, 201

class ContactApi(Resource):
    @jwt_required()
    def get(self, id):
        contact = Contact.get_contact(id)
        
        if not contact:
            return {'message': 'Contact not found'}, 404
        
        # Get interactions for this contact
        user_id = get_jwt_identity()
        interactions = Interaction.get_interactions(user_id, contact_name=contact['name'])
        
        # Convert ObjectId to string for JSON serialization
        contact['_id'] = str(contact['_id'])
        for interaction in interactions:
            interaction['_id'] = str(interaction['_id'])
        
        contact['interactions'] = interactions
        
        return contact, 200
    
    @jwt_required()
    def put(self, id):
        body = request.get_json()
        
        result = Contact.update_contact(id, body)
        
        if result.modified_count:
            return {'message': 'Contact updated successfully'}, 200
        return {'message': 'No changes made'}, 200
    
    @jwt_required()
    def delete(self, id):
        result = Contact.delete_contact(id)
        
        if result.deleted_count:
            return {'message': 'Contact deleted successfully'}, 200
        return {'message': 'Contact not found'}, 404

class ContactNoteApi(Resource):
    @jwt_required()
    def post(self, id):
        body = request.get_json()
        note = {
            'content': body.get('content'),
            'timestamp': datetime.utcnow()
        }
        
        result = Contact.add_note_to_contact(id, note)
        
        if result.modified_count:
            return {'message': 'Note added successfully'}, 200
        return {'message': 'Contact not found'}, 404
