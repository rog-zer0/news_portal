# from django.apps import AppConfig


# class NewsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'news'

#     def ready(self):
#         from .import signals
        
from django.apps import AppConfig

class NewsPortalConfig(AppConfig):
    name = 'news_portal'

    def ready(self):
        import news.signals
