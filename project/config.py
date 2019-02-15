class BaseConfig:
    """ BASE CONFIGURATION """
    DEBUG = False
    TESTING = False

class DevelopmentConfig:
    DEBUG = True

class TestingConfig:
    DEBUG = True
    TESTING = True

class ProductionCofig:
    DEBUG= False
