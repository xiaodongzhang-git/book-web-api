from flask_restful import Resource, reqparse
import re

from config import Config
from models.user import UserModel

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
                        default=Config.DEFAULT_AVATAR
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