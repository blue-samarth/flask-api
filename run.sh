#!/bin/bash
export FLASK_APP=src/server.py
export MONGO_URI="mongodb://127.0.0.1:27017/users"
gunicorn -w 4 -b 0.0.0.0:8000 src.server:app
