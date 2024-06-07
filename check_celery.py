import os

# Переменная окружения DJANGO_SETTINGS_MODULE, можно и в celery.py установить
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_portal.settings')

from news_portal.celery import app

print("Celery app loaded:", app)
