from .setting import db
from schemas import UserBase
from fastapi.exceptions import HTTPException
from fastapi import status


def db_create_user(request: UserBase):

    # email validate    
    if '@' not in request.email:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"your email {request.email} not valid")

    # password validate
    elif len(request.password) < 4:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="your password is short")
 
    else:
        user_dict = {
            'username': request.username,
            'password': request.password,
            'email': request.email}
        db.users.insert_one(user_dict)
        return {'status': 'ok', 'username': request.username, 'email': request.email}