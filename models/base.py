from db import db
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    is_delete = db.Column(db.Integer, default=1)
    create_time1 = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now,onupdate=datetime.now)
