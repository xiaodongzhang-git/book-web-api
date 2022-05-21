from views.user import UserRegister

class urlManage():

    def __init__(self):
        pass

    @staticmethod
    def init_url(api):
        api.add_resource(UserRegister, '/user/register')