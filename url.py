from views.user import UserRegister,UserLogin, UserInfo, UserUpdateInfo
from views.test import TestInit
from views.category import CategoryInfo
from views.novel import NovelList

class urlManage():

    def __init__(self):
        pass

    @staticmethod
    def init_url(api):
        # user
        api.add_resource(UserRegister, '/user/register')
        api.add_resource(UserLogin, '/user/login')
        api.add_resource(UserInfo, '/user/info/<int:id>')
        api.add_resource(UserUpdateInfo, '/user/update/info')
        # index
        api.add_resource(CategoryInfo, '/category/list')
        api.add_resource(NovelList, '/novelList/list/<int:id>')
        # test
        api.add_resource(TestInit, '/test/init')