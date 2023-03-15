import os
from datetime import timedelta

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
HOST = '127.0.0.1'
PORT = 5000
DEBUG = True

# ---------------------------------------------------------------
# < SQL ALCHEMY CONFIGURATION
# ---------------------------------------------------------------
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost:3306/database?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# ---------------------------------------------------------------
# > END SQL ALCHEMY CONFIGURATION
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# < FILE UPLOAD CONFIGURATION
# ---------------------------------------------------------------
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'mp4', 'mp3', 'doc', 'docx'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
# ---------------------------------------------------------------
# > END FILE UPLOAD CONFIGURATION
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# < JWT CONFIGURATION
# ---------------------------------------------------------------
JWT_SECRET_KEY = SECRET_KEY
JWT_ALGORITHM = 'HS256'
JWT_EXPIRATION_DELTA = timedelta(days=1)
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
# ---------------------------------------------------------------
# > END JWT CONFIGURATION
# ---------------------------------------------------------------
