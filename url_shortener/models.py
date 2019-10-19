import string
from random import choices
from datetime import datetime

from .extensions import db

class Link(db.Model):
  id = db.Column(db.Interger, primary_key=True)
  original_url = db.Column(db.String(512))
  short_url = db.Column(db.String(3), unique=True)
  visits = db.Column(db.Interger, default=0)
  date_created = db.Column(db.DateTime, default=datetime.now)

  def __init__(self, **kwargs):
    super().__init__(**kwards)
    self.short_url = self.generate_short_link()

  def generate_short_link(self):
      characters = string.digit + string.ascii_letters
      short_url = ''.join(choices(characters, k=3))

      self.query.filter_by(short_url=short_url).first()

      if link:
        return self.generate_short_link()
      
      return short_url