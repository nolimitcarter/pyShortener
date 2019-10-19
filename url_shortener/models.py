from datetime import datetime

from .extensions import db

class Link(db.Model):
  id = db.Column(db.Interger, primary_key=True)
  original_url = db.Column(db.String(512))
  short_url = db.Column(db.String(3), unique=True)
  visits = db.Column(db.Interger, default=0)
  date_created = db.Column(db.DateTime, default=datetime.now)

  