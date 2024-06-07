from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.timezone import now
from datetime import timedelta
from news.models import News, Subscriber  # Абсолютный импорт

@shared_task
def send_news_notification(news_id):
    news = News.objects.get(id=news_id)
    subscribers = Subscriber.objects.all()
    for subscriber in subscribers:
        subject = f"New article: {news.title}"
        message = render_to_string('news_notification_email.html', {'news': news, 'subscriber': subscriber})
        send_mail(subject, message, 'from@example.com', [subscriber.email])

@shared_task
def send_weekly_newsletter():
    last_week = now() - timedelta(days=7)
    recent_news = News.objects.filter(published_at__gte=last_week)
    subscribers = Subscriber.objects.all()
    for subscriber in subscribers:
        subject = "Weekly News Digest"
        message = render_to_string('weekly_newsletter_email.html', {'news_list': recent_news, 'subscriber': subscriber})
        send_mail(subject, message, 'from@example.com', [subscriber.email])
