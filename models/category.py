from db import db
from models.base import BaseModel

class CategoryModel(BaseModel):
    __tablename__ = 'category'

    name = db.Column(db.String(32), unique=True)

    def __init__(self, name):
        self.name = name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_all(cls):
        cls.query.filter().delete()
        db.session.commit()
