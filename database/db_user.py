from .setting import db
from schemas import UserBase


def db_create_user(request: UserBase):
    user_dict = {
        'username': request.username,
        'password': request.password,
        'email': request.email
    }
    db.users.insert_one(user_dict)

    return {'status': 'ok', 'username': request.username, 'email': request.email}