from database.db import db
from datetime import datetime
from bson import ObjectId

class Interaction:
    @staticmethod
    def add_interaction(user_id, contact_name, interaction_type, notes, tags=None):
        interaction = {
            'user_id': user_id,
            'contact_name': contact_name,
            'interaction_type': interaction_type,
            'notes': notes,
            'tags': tags or [],
            'timestamp': datetime.utcnow()
        }
        return db.interactions.insert_one(interaction)
    
    @staticmethod
    def get_interactions(user_id, start_date=None, end_date=None, contact_name=None):
        query = {'user_id': user_id}
        
        if start_date and end_date:
            query['timestamp'] = {
                '$gte': start_date,
                '$lte': end_date
            }
        
        if contact_name:
            query['contact_name'] = contact_name
            
        interactions = list(db.interactions.find(query).sort('timestamp', -1))
        
        # Convert datetime objects to ISO format strings
        for interaction in interactions:
            if 'timestamp' in interaction and isinstance(interaction['timestamp'], datetime):
                interaction['timestamp'] = interaction['timestamp'].isoformat()
        
        return interactions

    
    @staticmethod
    def update_interaction(interaction_id, data):
        return db.interactions.update_one(
            {'_id': ObjectId(interaction_id)},
            {'$set': data}
        )
    
    @staticmethod
    def delete_interaction(interaction_id):
        return db.interactions.delete_one({'_id': ObjectId(interaction_id)})
