from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import News, Article
from .filters import NewsFilter

from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class NewsList(ListView):
    model = News
    ordering = 'updated_at'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        # context['news'] = News.objects.all()
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'any_news.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs


class NewsSearch(ListView):
    template_name = 'news_search.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        category = request.POST.get('category')
        date = request.POST.get('date')

        # Получите отфильтрованные новости на основе критериев
        filtered_news = self.filter_news(title, category, date)

        context = {'news': filtered_news}
        return render(request, self.template_name, context)

    def filter_news(self, title, category, date):

        filtered_news = News.objects.all()

        if title:
            filtered_news = filtered_news.filter(title__icontains=title)

        if category:
            filtered_news = filtered_news.filter(category__iexact=category)

        if date:
            filtered_news = filtered_news.filter(date__gte=date)

        return filtered_news



class NewsArticleFormMixin:
    model = None
    fields = ['title', 'content', 'date']


class NewsCreateView(NewsArticleFormMixin, CreateView):
    template_name = 'news_create.html'
    model = News


class NewsEditView(NewsArticleFormMixin, UpdateView):
    template_name = 'news_edit.html'
    model = News
    queryset = News.objects.all()


class NewsDeleteView(DeleteView):
    template_name = 'news_delete.html'
    model = News
    success_url = '/news/'


class ArticleCreateView(NewsArticleFormMixin, CreateView):
    template_name = 'article_create.html'
    model = Article


class ArticleEditView(NewsArticleFormMixin, UpdateView):
    template_name = 'article_edit.html'
    model = Article
    queryset = Article.objects.all()


class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    model = Article
    success_url = '/articles/'
