from flask_restful import Resource
from models.category import CategoryModel
from models.user import UserModel
from models.novel import NovelModel
from models.chapter import ChapterModel
import random

from db import db

class TestInit(Resource):

    def get(self):
        db.drop_all()
        db.create_all()

        user = UserModel(
            username='admin01',
            password='123456',
            email='admin01@yahoo.com',
            nickname='admin01',
            birthday='1990-01-01',
            avatar='')
        user.save_to_db()

        chapter_id = 1
        categorys = ['玄幻', '武侠', '青春', '穿越']
        for idx,c in enumerate(categorys):
            c_model = CategoryModel(c)
            c_model.save_to_db()

            for i in range(0, 10):
                n_model = NovelModel(
                    name=c+str(i),
                    intro=c+'intro'+str(i),
                    avatar='',
                    user_id=1,
                    category_id=idx+1)
                n_model.good = random.randint(0,1000)
                n_model.read = random.randint(0,1000)
                n_model.save_to_db()

                for j in range(0, 10):
                    ch_model = ChapterModel(
                        name='章节'+str(j+1),
                        num=j+1,
                        content='内容'*100,
                        novel_id=i+1+(10*idx))
                    ch_model.save_to_db()

        return {"message": "db init successfully."}, 200