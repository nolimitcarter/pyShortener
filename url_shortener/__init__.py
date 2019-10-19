from flask import flask

from .extensions import db

def create_app(config_file='settings.py'):
  app = flask(__name__)

  app.config.from_pyfile(config_file)

  db.init_app(app)

  return app