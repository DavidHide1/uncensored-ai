import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    DEBUG = os.getenv("DEBUG", False)
    UPLOAD_FOLDER = "static/uploads"
