from flask import Flask
from webapp.config import Config

app = Flask(__name__)
# app.config.from_object(Config)

SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
DINO_FOLDER = os.path.join('static', 'dino')
BACKGROUND_FOLDER = os.path.join('static', 'backgrounds')
CRED_PATH = os.path.join('static', 'creds')


from webapp import routes

if __name__ == '__main__':
    app.run()
