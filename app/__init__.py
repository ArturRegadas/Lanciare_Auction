from flask import blueprints, Flask
from flask_socketio import SocketIO
from typing import Dict, Any
from config import Config

socket_io = SocketIO(cors_allowed_origins="*")

def create_app() -> Dict[str, Any]:
    app = Flask(__name__)
    app.config.from_object(Config)
  
    #Listing blueprints
    from app.services.CreateAsaasCustomer import payment_bp

    app.register_blueprint(payment_bp)
    
    socket_io.init_app(app)
    #Returning instance
    return {"app":app, "socket":socket_io}