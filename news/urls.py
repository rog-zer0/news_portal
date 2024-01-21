from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch
from .views import NewsCreateView, NewsEditView, NewsDeleteView
from .views import ArticleCreateView, ArticleEditView, ArticleDeleteView

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', NewsList.as_view()),
   path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
   path('search/', NewsSearch.as_view(), name='news_search'),
   path('create/', NewsCreateView.as_view(), name='news_create'),
   path('<int:pk>/edit/', NewsEditView.as_view(), name='news_edit'),
   path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),

   path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
   path('articles/<int:pk>/edit/', ArticleEditView.as_view(), name='article_edit'),
   path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]

