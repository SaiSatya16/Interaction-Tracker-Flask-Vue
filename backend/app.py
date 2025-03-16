from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# JWT Configuration
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 86400  # 24 hours
jwt = JWTManager(app)

# Initialize API
api = Api(app)

if __name__ == '__main__':
    from resources.routes import initialize_routes
    initialize_routes(api)
    app.run(debug=True)
