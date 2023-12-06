from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import News


class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = News
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'updated_at'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['news'] = News.objects.all()
        return context


# Создаем свой класс, который наследуется от ListView.
# Указываем модель, из которой будем выводить данные.
# Указываем поле сортировки данных модели (необязательно).
# Записываем название шаблона.
# Объявляем, как хотим назвать переменную в шаблоне.

class NewsDetail(DetailView):
    model = News
    template_name = 'any_news.html'
    context_object_name = 'news'
