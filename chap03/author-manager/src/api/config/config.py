class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/flaskrest'
    SECRET_KEY = 'sunshine'
    SECURITY_PASSWORD_SALT = 'dawn'
    SQLALCHEMY_ECHO = False

    MAIL_DEFAULT_SENDER = 'menglj@we-wins.com'
    MAIL_SERVER = 'smtp.263.net'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'menglj@we-wins.com'
    MAIL_PASSWORD = 'Lte5563'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_ECHO = False
