from flask import Flask
from routes.home import home_bp
from routes.chat import chat_bp  # Import the chat_bp Blueprint

app = Flask(__name__, template_folder='templates', static_folder='static')

# Register Blueprints
app.register_blueprint(home_bp, url_prefix='/')
app.register_blueprint(chat_bp, url_prefix='/')  # Register the chat Blueprint

if __name__ == '__main__':
    app.run(debug=True)
