from pymongo import MongoClient
import os

client = MongoClient(os.getenv('MONGO_URI'))
db = client.interaction_tracker
