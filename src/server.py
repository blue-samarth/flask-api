from flask import jsonify

from src import app
from src.apis.user_api import user_api

app.register_blueprint(user_api)

@app.route('/')
def read_root():
    return jsonify({"message": "Welcome to Flask API"})

if __name__ == '__main__':
    app.run()