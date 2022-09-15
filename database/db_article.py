# from pymongo import MongoClient
from .setting import clinet, db
from schemas import ArticleBase


def db_create_article(request: ArticleBase):
    article_dict = {
        "title": request.title,
        "description": request.description,
        "published": request.published
    }
    db.articles.insert_one(article_dict)
    
    return {'status': 'ok'}

def get_articles():
    articles = db.articles.find({'published': True})
    article_dicts = {}
    number = 0
    for article in articles:
        article.pop("_id")
        article_dicts[f"article {number}"] = article
        number += 1

    return article_dicts