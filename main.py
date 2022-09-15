from fastapi import FastAPI
from router import article, user

app = FastAPI()

app.include_router(article.router)
app.include_router(user.router)