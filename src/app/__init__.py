from flask import Flask
from flask_mongoengine import MongoEngine
import os


app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config["MONGODB_SETTINGS"] = {
    "host" : "mongodb://app_db/dashboardData"
}

db = MongoEngine(app)

from app import routes