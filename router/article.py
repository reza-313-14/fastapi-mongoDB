from fastapi import APIRouter
from schemas import ArticleBase
from database.db_article import db_create_article, get_articles

router = APIRouter(prefix='/article', tags=['article'])


# , response_model=ArticleDisplay
@router.post('/create-article')
async def create_article(article: ArticleBase):
    db_create_article(article)
    return {
        'status': 'ok',
        'article_created': {
            'title': article.title,
            'description': article.description,
            'published': article.published
        }
    }

@router.get('/articles')
async def show_articles():
    return get_articles()