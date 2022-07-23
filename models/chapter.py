from db import db
from models.base import BaseModel
from flask import current_app

class ChapterModel(BaseModel):
    __tablename__ = 'chapter'

    name = db.Column(db.String(32))
    num = db.Column(db.Integer)
    content = db.Column(db.Text())

    novel_id = db.Column(db.Integer, db.ForeignKey('novel.id'))
    novel = db.relationship('NovelModel', backref=db.backref('chapters'))

    def __init__(self, name, num, content, novel_id):
        self.name = name
        self.num = num
        self.content = content
        self.novel_id = novel_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_chapter_list_by_nid(cls, nid, limit, offset):
        return cls.query.filter_by(novel_id=nid, is_delete=1).order_by(cls.update_time.desc()).limit(limit).offset(offset).all()

    @classmethod
    def get_chapter_list_count(cls, nid):
        return cls.query.filter_by(novel_id=nid,is_delete=1).count()