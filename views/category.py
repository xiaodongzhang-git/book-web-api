from flask_restful import Resource
from models.category import CategoryModel

class CategoryInfo(Resource):

    def get(self):

        category_list = CategoryModel.get_category_list()
        res = []
        for c in category_list:
            res.append({'id': c.id, 'name': c.name})

        return {"data": {'result': res}}, 200