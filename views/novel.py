from flask_restful import Resource, reqparse
from models.novel import NovelModel
import constant

class NovelList(Resource):

    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('cid',
                            type=int,
                            default=0,
                            location='args'
                            )
        parser.add_argument('action',
                            type=int,
                            default=0, # 1代表点赞排行 2代表阅读排行
                            location='args'
                            )
        parser.add_argument('limit',
                            type=int,
                            default=10,
                            location='args'
                            )
        parser.add_argument('offset',
                            type=int,
                            default=0,
                            location='args'
                            )

        data = parser.parse_args()
        cid = data['cid']
        action = data['action']
        offset = data['offset']
        limit = data['limit']

        novel_list = []
        if cid > 0:
            novel_list = NovelModel.get_novel_list_by_cid(cid, limit, offset)
        elif action in [1, 2]:
            novel_list = NovelModel.get_novel_list_order_by_action(limit, offset, action)
        else:
            return {"message": "error request"}, 202

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