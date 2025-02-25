# Here we will initialize the flask app with mongo db and jwt
import os

from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

app: Flask = Flask(__name__)

# Now we will add the CORS support to our app
CORS(app)

load_dotenv()

app.config.update({
    "MONGO_URI": os.getenv("MONGO_URI"),
    "JWT_SECRET_KEY": os.getenv("SECRET_KEY")
})

mongo = PyMongo(app)

jwt = JWTManager(app)

def startup_event() -> None:
    try:
            mongo.db.command("ping")
            print("Connected to MongoDB")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        print("Exiting...")
        exit(1)

with app.app_context():
    startup_event()

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     mongo.db.client.close()
