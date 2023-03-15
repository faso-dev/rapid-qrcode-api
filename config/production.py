import os
from datetime import timedelta

SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = False

# ---------------------------------------------------------------
# < SQL ALCHEMY CONFIGURATION
# ---------------------------------------------------------------
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
# ---------------------------------------------------------------
# > END SQL ALCHEMY CONFIGURATION
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# < JWT CONFIGURATION
# ---------------------------------------------------------------
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', SECRET_KEY)
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')
JWT_EXPIRATION_DELTA = timedelta(days=1)
JWT_BLACKLIST_ENABLED = os.getenv('JWT_BLACKLIST_ENABLED', True)
JWT_BLACKLIST_TOKEN_CHECKS = os.getenv('JWT_BLACKLIST_TOKEN_CHECKS', ['access', 'refresh'])
# ---------------------------------------------------------------
# > END JWT CONFIGURATION
# ---------------------------------------------------------------
