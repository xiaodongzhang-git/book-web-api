from flask_restful import Resource, reqparse
from models.chapter import ChapterModel
import constant

class ChapterList(Resource):

    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('nid',
                            type=int,
                            required=True,
                            help="This field cannot be blank.",
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
        nid = data['nid']
        offset = data['offset']
        limit = data['limit']

        chapter_list = []
        
        chapter_list = ChapterModel.get_chapter_list_by_nid(nid, limit, offset)

        res = []

        for chapter in chapter_list:
            temp = {}
            temp['id'] = chapter.id
            temp['update_time'] = str(chapter.update_time)
            temp['name'] = chapter.name
            temp['num'] = chapter.num
            # novel
            temp['novel_name'] = chapter.novel.name
            temp['status'] = constant.STATUS.get(chapter.novel.status, '不存在')
            temp['avatar'] = chapter.novel.avatar
            temp['intro'] = chapter.novel.intro
            res.append(temp)

        count = ChapterModel.get_chapter_list_count(nid)
        return {"data": {'result': res, 'count': count}}, 200
