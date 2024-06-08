from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch
from .views import NewsCreateView, NewsEditView, NewsDeleteView
from .views import ArticleCreateView, ArticleEditView, ArticleDeleteView
from .views import subscriptions
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [

   path('news/<int:pk>/', cache_page(60 * 5)(views.DetailView.as_view()), name='news-detail'),
   path('', cache_page(60)(views.NewsList.as_view()), name='home'),
   #path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
   path('search/', NewsSearch.as_view(), name='news_search'),
   path('create/', NewsCreateView.as_view(), name='news_create'),
   path('<int:pk>/edit/', NewsEditView.as_view(), name='news_edit'),
   path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
   path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
   path('articles/<int:pk>/edit/', ArticleEditView.as_view(), name='article_edit'),
   path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),
]

