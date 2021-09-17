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
    SQLALCHEMY_DATABASE_URI = 'postgresql://pkqgrvbvfnnceh:dd9e213fd206011cf6976c16a84ce9ae555434b73d5665fcdddb8c8a3c316c31@ec2-54-81-126-150.compute-1.amazonaws.com:5432/da1qlfgvql5rpe'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turn off Update Messages from the sqlalchemy