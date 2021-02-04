class Config(object):
    LOG_LEVEL = logging.DEBUG
    

class DevelopmentConfig(Config):
    """
    开发环境下的配置
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    生产环境下的配置
    """
    DEBUG = False
    LOG_LEVEL = logging.WARNING


class TestingConfig(Config):
    """
    单元测试环境下的配置
    """
    DEBUG = False
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}