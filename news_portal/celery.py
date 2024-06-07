from celery import Celery

app = Celery('news_portal')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# Определите какую-либо тестовую задачу для проверки
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
