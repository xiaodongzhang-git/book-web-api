from flask import current_app, request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import functools

from models.user import UserModel

def create_token(uid):
    '''
    生成token
    :param uid:用户id
    :return: token
    '''

    #第一个参数是内部的私钥，这里写在共用的配置信息里了，如果只是测试可以写死
    #第二个参数是有效期(秒)
    s = Serializer(current_app.config["SECRET_KEY"],expires_in=3600)
    #接收用户id转换与编码
    token = s.dumps({"id":uid}).decode("ascii")
    return token

def login_required(view_func):
    @functools.wraps(view_func)
    def verify_token(*args,**kwargs):
        try:
            token = request.headers["z-token"]
        except Exception:
            return {"message": "token is not blank"}, 202

        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            s.loads(token)
        except Exception:
            return {"message": "token verification failed"}, 202

        return view_func(*args,**kwargs)

    return verify_token

def get_id_by_token():
    token = request.headers["z-token"]
    s = Serializer(current_app.config["SECRET_KEY"])
    obj = s.loads(token)
    return obj['id']