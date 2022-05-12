import os

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL')

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL')

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://nancyngunjiri1@gmail.com:nazarenah333@localhost:5432/product'
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL')
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
