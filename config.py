import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# Give access to the project in ANY OS we find ourselves in
# Allow outside files/folders to be added to the project from the
# base directory.

class Config():
    """
        Set config variables for the flask app.
        Using Environment variables where available otherwise
        create the config variables if not done already.
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:99013Pog@127.0.0.1:5432/car-collection'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turn off Update Messages from the sqlalchemy