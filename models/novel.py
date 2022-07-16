from db import db
from models.base import BaseModel
from flask import current_app

class NovelModel(BaseModel):
    __tablename__ = 'novel'

    name = db.Column(db.String(32), unique=True)
    intro = db.Column(db.String(128))
    status = db.Column(db.Integer, default=0)
    avatar = db.Column(db.Text())
    good = db.Column(db.Integer, default=0)
    read = db.Column(db.Integer, default=0)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel', backref=db.backref('novels'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('CategoryModel', backref=db.backref('novels'))

    def __init__(self, name, intro, avatar, user_id, category_id):
        self.name = name
        self.intro = intro
        self.avatar = avatar if avatar else current_app.config['DEFAULT_AVATAR']
        self.user_id = user_id
        self.category_id = category_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_novel_list_by_cid(cls, category_id, limit, offset):
        return cls.query.filter_by(category_id=category_id, is_delete=1).order_by(cls.update_time.desc()).limit(limit).offset(offset).all()

    @classmethod
    def get_novel_list_order_by_action(cls, limit, offset, action):
        if action == 1:
            return cls.query.filter_by(is_delete=1).order_by(cls.good.desc()).limit(limit).offset(offset).all()
        else:
            return cls.query.filter_by(is_delete=1).order_by(cls.read.desc()).limit(limit).offset(offset).all()