from pydantic import BaseModel

# article schemas
class ArticleBase(BaseModel):
    title: str
    description: str
    published: bool


# user schemas
class UserBase(BaseModel):
    username: str
    password: str
    email: str