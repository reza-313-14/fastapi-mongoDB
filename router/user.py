from fastapi import APIRouter
from schemas import UserBase
from database.db_user import db_create_user

router = APIRouter(prefix='/user', tags=['user'])

@router.post('/create-user')
async def create_user(User: UserBase):
    return db_create_user(User)