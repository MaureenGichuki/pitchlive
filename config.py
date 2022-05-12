import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:mimo1234@localhost/mimopitchlive'
    SECRET_KEY = ('mimo')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


    #email configurations

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'mimowaruguru@gmail.com'
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_USE_SSL= True

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:mimo1234@localhost/mimopitchlive'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:mimo1234@localhost/mimopitchlive'




class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:mimo1234@localhost/mimopitchlive'

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig,

}