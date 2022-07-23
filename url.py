from views.user import UserRegister,UserLogin, UserInfo
from views.test import TestInit
from views.category import CategoryInfo
from views.novel import NovelList
from views.chapter import ChapterList

class urlManage():

    def __init__(self):
        pass

    @staticmethod
    def init_url(api):
        # user
        api.add_resource(UserRegister, '/user/register')
        api.add_resource(UserLogin, '/user/login')
        api.add_resource(UserInfo, '/user/info/<int:id>')

        # index
        api.add_resource(CategoryInfo, '/category/list')
        api.add_resource(NovelList, '/novelList/list')
        # chapter
        api.add_resource(ChapterList, '/chapterList/list')
        # test
        api.add_resource(TestInit, '/test/init')