from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import News
from .filters import NewsFilter
from django.db.models import Q
from django.shortcuts import render

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


