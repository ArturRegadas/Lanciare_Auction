from dotenv import load_dotenv
from secrets import token_hex
import os

load_dotenv()


class Config:
    #The constructor method isn't necessary because this class is only a container of static attributes for the server.
    #The attributes are in uppercase in order to follow Flask's standardization.
    SECRET_KEY = token_hex(16)
    SOCKETIO_ASYNC_MODE = "threading"

    URL_API = os.getenv("URL_API")
    SANDBOX_URL_API = os.getenv("SANDBOX_URL_API")

    API_TOKEN = os.getenv("API_TOKEN")
    SANDBOX_API_TOKEN = os.getenv("SANDBOX_API_TOKEN")

    ASAAS_WALLET_ID = os.getenv("ASAAS_WALLET_ID")

    INTERNAL_TOKEN_API = os.getenv("INTERNAL_TOKEN_API")
    
    FLASK_ENV = os.getenv("FLASK_ENV")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = os.getenv("PORT", "5000")
    DEBUG = os.getenv("DEBUG", False)