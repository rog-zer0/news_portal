from django.views.generic import ListView, DetailView
from .models import News

class NewsList(ListView):
    model = News
    template_name = 'flatpages/default.html'
    context_object_name = 'news'

