class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/flaskrest'
    SQLALCHEMY_ECHO = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_ECHO = False
