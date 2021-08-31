import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Give access to the project on ANY OS
# Allow outside files/folders to be added to the project from the 
# base directory.

class Config():
    """
        Set config variable for the flask app, if not already created.
    """

    SECRET_KEY = os.environ.get('SECRETKEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turn off Update Messages