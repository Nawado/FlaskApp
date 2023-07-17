import os

class BaseConfig(object):

    # Database
    db_host = os.getenv("MY_SQL_SERVER")
    db_port = os.getenv("MY_SQL_PORT")
    db_user = os.getenv("MY_SQL_USER")
    db_password = os.getenv("MY_SQL_PASSWORD")
    db_name = os.getenv("MY_SQL_DB")

    sqlalchemy_database_uri = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'


    # Application
    NAME = "flaskapp"
    DESCRIPTION = "flaskapp"
    VERSION = "v1"


class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True


class ProdConfig(BaseConfig):
    FLASK_ENV = 'production'