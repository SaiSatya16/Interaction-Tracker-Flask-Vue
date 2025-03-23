from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.interaction import Interaction
from bson import ObjectId
from datetime import datetime
from database.db import db
class InteractionsApi(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        
        # Parse query parameters
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        contact_name = request.args.get('contact_name')
        
        if start_date:
            start_date = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
        if end_date:
            end_date = datetime.fromisoformat(end_date.replace('Z', '+00:00'))
        
        interactions = Interaction.get_interactions(user_id, start_date, end_date, contact_name)
        
        # Convert ObjectId to string for JSON serialization
        for interaction in interactions:
            interaction['_id'] = str(interaction['_id'])
        
        return interactions, 200
    
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        
        interaction = Interaction.add_interaction(
            user_id=user_id,
            contact_name=body.get('contact_name'),
            interaction_type=body.get('interaction_type'),
            notes=body.get('notes'),
            tags=body.get('tags')
        )
        
        return {'id': str(interaction.inserted_id)}, 201

class InteractionApi(Resource):
# In backend/resources/interaction.py
    @jwt_required()
    def get(self, id):
        try:
            interaction = db.interactions.find_one({'_id': ObjectId(id)})
            
            if not interaction:
                return {'message': 'Interaction not found'}, 404
            
            # Convert ObjectId to string for JSON serialization
            interaction['_id'] = str(interaction['_id'])
            
            # Convert datetime to ISO format string
            if 'timestamp' in interaction and isinstance(interaction['timestamp'], datetime):
                interaction['timestamp'] = interaction['timestamp'].isoformat()
            
            return interaction, 200
        except Exception as e:
            return {'message': str(e)}, 500


    
    @jwt_required()
    def put(self, id):
        user_id = get_jwt_identity()
        body = request.get_json()
        
        result = Interaction.update_interaction(id, body)
        
        if result.modified_count:
            return {'message': 'Interaction updated successfully'}, 200
        return {'message': 'No changes made'}, 200
    
    @jwt_required()
    def delete(self, id):
        result = Interaction.delete_interaction(id)
        
        if result.deleted_count:
            return {'message': 'Interaction deleted successfully'}, 200
        return {'message': 'Interaction not found'}, 404
