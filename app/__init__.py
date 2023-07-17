from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

import os

from app.settings import ProdConfig, DevConfig
from routes import api


def create_app():
    app = Flask(__name__)
    load_dotenv()

    db = SQLAlchemy(app)

    stage = os.getenv("STAGE")
    if stage == "dev":
        app.config.from_object(DevConfig())
    elif stage == "prod":
        app.config.from_object(ProdConfig())
    else:
        exit(1)

    api.init_app(app)

    return app

