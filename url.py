from views.user import UserRegister
from views.user import UserLogin
from views.user import UserInfo

class urlManage():

    def __init__(self):
        pass

    @staticmethod
    def init_url(api):
        api.add_resource(UserRegister, '/user/register')
        api.add_resource(UserLogin, '/user/login')
        api.add_resource(UserInfo, '/user/info/<int:id>')