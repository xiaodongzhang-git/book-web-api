class Config:
    # http://www.pythondoc.com/flask-sqlalchemy/config.html
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    DEFAULT_AVATAR = 'https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.touxiangwu.com%2Ftouxiang%2F84045.html&psig=AOvVaw39cm8wqfWIefoRmddPG1zn&ust=1653824546284000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCLjywZyQgvgCFQAAAAAdAAAAABAD'
    @staticmethod
    def init_app(app):
        pass

# 开发环境   语法：mysql+pymysql://用户名：密码@ip：端口/数据库名
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/bookdb'

# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/bookdb'

# 配置字典
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
