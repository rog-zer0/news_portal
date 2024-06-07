from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'
    ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )
    
    
class Subscriber(models.Model):
    email = models.EmailField()
    
class NewsSender:
    pass