from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
    "host" : "mongodb://app_db/dashboardData"
}

db = MongoEngine(app)

from app import routes