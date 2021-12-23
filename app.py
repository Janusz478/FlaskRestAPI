from flask import Flask, Blueprint
import settings
from api.myapi import api
from api.shop.endpoints.products import namespace as productsnamespace
from database.db import db

app = Flask(__name__)


def configure_app(app):
    app.config["SWAGGER_UI_DOC_EXPANSION"] = settings.RESTPLUS_SWAGGER_EXPANSION
    app.config["RESTX_VALIDATE"] = settings.RESTPLUS_VAL
    app.config["RESTX_MASK_SWAGGER"] = settings.RESTPLUS_MASK_SWAGGER
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = settings.SQLALCHEMY_TRACK_MODS


def init_app(app):
    configure_app(app)
    blueprint = Blueprint("api", __name__, url_prefix="/api")
    api.init_app(blueprint)
    api.add_namespace(productsnamespace)
    app.register_blueprint(blueprint)
    db.init_app(app)


init_app(app)
app.run(debug=settings.FLASK_DEBUG)

