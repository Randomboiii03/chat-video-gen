from flask import Blueprint, render_template, request, jsonify
import json
import uuid
import os

home_bp = Blueprint('home_bp', __name__, template_folder='templates', static_folder='static')

@home_bp.route('/')
def home():
    return render_template('index.html')

@home_bp.route('/save_json', methods=['POST'])
def save_json():
    data = request.get_json()
    
    if data:
        file_name = f"{uuid.uuid4()}.json"
        
        file_path = os.path.join('static', 'json', file_name)
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w') as file:
            json.dump(data, file)
        
        return jsonify({
            "success": True,
            "message": "Data saved successfully.",
            "filename": file_name
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "No JSON data received or invalid JSON."
        }), 400