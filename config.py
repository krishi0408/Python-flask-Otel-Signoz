import os
from dotenv import load_dotenv
from db import mongo

load_dotenv()

def configure_app(app):
    app.config['MONGO_URI'] = os.getenv("MONGO_URI")
    mongo.init_app(app)
    app.template_folder = os.path.join(os.path.dirname(__file__), 'templates')
