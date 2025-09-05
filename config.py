import os
from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get('x-api-key')  # a chave deve vir no header
        if key and key == API_KEY:
            return f(*args, **kwargs)
        else:
            return jsonify({"error": "Chave de API inválida ou ausente"}), 401
    return decorated