import os

from dotenv import load_dotenv

load_dotenv()

env = os.getenv('FLASK_ENV', 'development')

if env == 'development':
    from .development import *
elif env == 'production':
    from .production import *
else:
    raise ValueError('Invalid FLASK_ENV value')
