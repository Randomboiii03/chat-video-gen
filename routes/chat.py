from flask import Blueprint, request, render_template, jsonify
import json
import os

chat_bp = Blueprint('chat_bp', __name__, template_folder='templates', static_folder='static')

@chat_bp.route('/chat')
def chat():
    file_name = request.args.get('filename')
    file_path = f'static/json/{file_name}'
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

        print(json_data)

        return render_template('chat.html', json_data=json_data)
    except Exception as e:
        return str(e)

