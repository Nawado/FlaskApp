from sqlalchemy import create_engine

from app.settings import BaseConfig

engine = create_engine(BaseConfig.sqlalchemy_database_uri, isolation_level="AUTOCOMMIT")
