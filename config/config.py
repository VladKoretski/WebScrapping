## Определяем URL сайта:
from threading import TIMEOUT_MAX

URL = 'https://habr.com/ru/articles/'
## Определяем список ключевых слов:
KEYWORDS = ['SQL', 'индекс', 'нейросет', 'Garmin', 'локал', 'милл']

## Определяем объекты на странице:
CONTENT_BLOCK = 'div.tm-page__main_has-sidebar.tm-page__main'
ARTICLE_BLOCK = 'div.article-snippet'
ARTICLE_TITLE = 'h2.tm-title.tm-title_h2 a'
ARTICLE_BODY = 'div.article-formatted-body p'

## Время задержки
TIMEOUT = 10