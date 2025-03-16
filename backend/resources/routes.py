from resources.auth import SignupApi, LoginApi
from resources.interaction import InteractionsApi, InteractionApi
from resources.contact import ContactsApi, ContactApi, ContactNoteApi
from resources.analytics import InteractionHeatmapApi, NetworkGraphApi

def initialize_routes(api):
    # Auth routes
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    
    # Interaction routes
    api.add_resource(InteractionsApi, '/api/interactions')
    api.add_resource(InteractionApi, '/api/interactions/<id>')
    
    # Contact routes
    api.add_resource(ContactsApi, '/api/contacts')
    api.add_resource(ContactApi, '/api/contacts/<id>')
    api.add_resource(ContactNoteApi, '/api/contacts/<id>/notes')
    
    # Analytics routes
    api.add_resource(InteractionHeatmapApi, '/api/analytics/heatmap')
    api.add_resource(NetworkGraphApi, '/api/analytics/network')
