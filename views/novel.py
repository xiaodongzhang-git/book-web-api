from flask_restful import Resource
from models.novel import NovelModel
import constant

class NovelList(Resource):

    def get(self, id):

        novel_list = NovelModel.get_novel_list(id)

        res = []

        for novel in novel_list:
            temp = {}
            temp['id'] = novel.id
            temp['update_time'] = str(novel.update_time)
            temp['name'] = novel.name
            temp['status'] = constant.STATUS.get(novel.status, '不存在')
            temp['good'] = novel.good
            temp['read'] = novel.read
            temp['nickname'] = novel.user.nickname
            res.append(temp)
        return {"data": {'result': res}}, 200