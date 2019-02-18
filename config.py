import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DINO_FOLDER = os.path.join('static', 'dino')
    BACKGROUND_FOLDER = os.path.join('static', 'backgrounds')
    CRED_PATH = os.path.join('static', 'creds')
