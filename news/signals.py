# from django.contrib.auth.models import User
# from django.core.mail import EmailMultiAlternatives
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from .models import News
# from .tasks import send_news_notification

# @receiver(post_save, sender=News)
# def news_created(instance, created, **kwargs):
#     if not created:
#         return

#     emails = User.objects.filter(
#         subscriptions__category=instance.category
#     ).values_list('email', flat=True)

#     subject = f'Новая новость в категории {instance.category}'

#     text_content = (
#         f'Новость: {instance.title}\n'
#         f'Категория: {instance.category}\n\n'
#         f'Ссылка на Новость: http://127.0.0.1:8000{instance.get_absolute_url()}'
#     )
#     html_content = (
#         f'Новость: {instance.title}<br>'
#         f'Категория: {instance.category}<br><br>'
#         f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
#         f'Ссылка на Новость</a>'
#     )
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, None, [email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()
        
from django.db.models.signals import post_save
from django.dispatch import receiver
from news.models import News  # Используем абсолютный импорт
from news.tasks import send_news_notification  # Используем абсолютный импорт

@receiver(post_save, sender=News)
def news_created(sender, instance, created, **kwargs):
    if created:
        send_news_notification.delay(instance.id)