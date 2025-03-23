from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.interaction import Interaction
from models.contact import Contact
from datetime import datetime, timedelta

# In backend/resources/analytics.py - fix the truncated code
class InteractionHeatmapApi(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        
        # Get interactions for the last 365 days
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=365)
        
        interactions = Interaction.get_interactions(user_id, start_date, end_date)
        
        # Format data for heatmap
        heatmap_data = {}
        for interaction in interactions:
            # Check if timestamp is a string and convert it to datetime if needed
            if isinstance(interaction['timestamp'], str):
                timestamp = datetime.fromisoformat(interaction['timestamp'].replace('Z', '+00:00'))
            else:
                timestamp = interaction['timestamp']
                
            date_str = timestamp.strftime('%Y-%m-%d')
            if date_str in heatmap_data:
                heatmap_data[date_str] += 1
            else:
                heatmap_data[date_str] = 1
        
        return heatmap_data, 200


class NetworkGraphApi(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        
        # Get all contacts
        contacts = Contact.get_contacts(user_id)
        
        # Get all interactions
        interactions = Interaction.get_interactions(user_id)
        
        # Format data for network graph
        nodes = []
        links = []
        
        # Add user as central node
        nodes.append({
            'id': 'user',
            'name': 'You',
            'type': 'user'
        })
        
        # Add contacts as nodes
        contact_dict = {}
        for contact in contacts:
            contact_id = str(contact['_id'])
            contact_dict[contact['name']] = contact_id
            nodes.append({
                'id': contact_id,
                'name': contact['name'],
                'type': 'contact'
            })
        
        # Count interactions between user and contacts
        interaction_counts = {}
        for interaction in interactions:
            contact_name = interaction['contact_name']
            if contact_name in contact_dict:
                contact_id = contact_dict[contact_name]
                if contact_id in interaction_counts:
                    interaction_counts[contact_id] += 1
                else:
                    interaction_counts[contact_id] = 1
        
        # Create links based on interaction counts
        for contact_id, count in interaction_counts.items():
            links.append({
                'source': 'user',
                'target': contact_id,
                'value': count
            })
        
        return {'nodes': nodes, 'links': links}, 200
