import os
from celery import Celery

app = Celery('news_portal')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_portal.settings')

# Определение тестовой задачи для проверки
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Настройка повторного подключения при запуске, во избежание ошибок в версии 6 и выше.
app.conf.broker_connection_retry_on_startup = True