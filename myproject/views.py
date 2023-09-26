from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    html = "<h1>Всем привет. Это мой первый сайт на Django</h1>" \
           "<p>Это главная страница, с неё начинается моя история.</p>"
    logger.info(f'Показана информация: {html}')
    return HttpResponse(html)


def about(request):
    html = "<h1>Обо мне</h1>" \
           "<p>Меня зовут Евгений. Обучаюсь на программиста. Учеба дается тяжело, но мне нравится. </p>"
    logger.info(f'Показана информация: {html}')
    return HttpResponse(html)