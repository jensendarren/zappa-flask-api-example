import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    MESSAGE = os.environ.get('MESSAGE') or 'hello from message hardcoded in Config class'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-was-set-in-the-code'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False