from flask_restful import Resource, reqparse
import re

from models.user import UserModel
from utils import create_token, login_required

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('nickname',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('birthday',
                        type=str,
                        default=''
                        )
    parser.add_argument('avatar',
                        type=str,
                        default=''
                        )

    def post(self):
        email_rex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        data = UserRegister.parser.parse_args()
        username = data['username']
        password = data['password']
        email=data['email']
        nickname=data['nickname']
        birthday=data['birthday']
        avatar=data['avatar']

        user = UserModel.find_by_username(username)
        has_email = UserModel.find_by_email(email)

        if user is not None:
            return {"message": "same username exists"}, 202

        if has_email is not None:
            return {"message": "same email exists"}, 202

        if len(password)<6 or len(password)>32:
            return {"message": "Password must be between 6 and 32 digits"}, 202

        if len(nickname)<2 or len(nickname)>32:
            return {"message": "nickname must be between 6 and 32 digits"}, 202

        if not re.match(email_rex, email):
            return {"message": "Email format error"}, 202

        user = UserModel(
            username=username,
            password=password,
            email=email,
            nickname=nickname,
            birthday=birthday,
            avatar=avatar)
        user.save_to_db()
        return {"message": "User created successfully."}, 201


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="username cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="password cannot be blank."
                        )

    def post(self):
        data = UserLogin.parser.parse_args()
        username = data['username']
        password = data['password']
        user = UserModel.find_by_login(username, password)

        if not user:
            return {"message": "user not exits"}, 202

        token = create_token(user.id)
        return {"data": {'token': token}}, 200


class UserInfo(Resource):

    @login_required
    def get(self, id):
        user = UserModel.find_by_id(id)
        if not user:
            return {"message": "user not exits"}, 202

        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'nickname': user.nickname,
            'birthday': str(user.birthday),
            'avatar': user.avatar,
        }

        return {"data": data}, 200