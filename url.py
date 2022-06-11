from views.user import UserRegister,UserLogin, UserInfo, UserUpdateInfo

class urlManage():

    def __init__(self):
        pass

    @staticmethod
    def init_url(api):
        api.add_resource(UserRegister, '/user/register')
        api.add_resource(UserLogin, '/user/login')
        api.add_resource(UserInfo, '/user/info/<int:id>')
        api.add_resource(UserUpdateInfo, '/user/update/info')