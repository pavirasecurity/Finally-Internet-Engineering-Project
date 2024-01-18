from helpers import secrets, socket

APP_HOST = socket.gethostbyname(socket.gethostname())  
DEBUG_MODE = True 
LOG_IN = True 
REGISTRATION = True 
SESSION_PERMANENT = True 
SQLALCHEMY_DATABASE_URI = 'sqlite:///flaskblog.db'
APP_SECRET_KEY = secrets.token_urlsafe(32)  
GOOGLE_CLIENT_ID = "my-id-here"
GOOGLE_CLIENT_SECRET = "my-secret-here"