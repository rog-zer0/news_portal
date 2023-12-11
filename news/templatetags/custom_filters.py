import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='remove_obscene')
def remove_obscene(value):
    obscene_words = ['гадость', 'гадости', 'нецензурное_слово1', 'нецензурное_слово2', 'и_так_далее']

    # Создаем регулярное выражение, которое будет заменять все формы каждого слова
    regex_pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, obscene_words)) + r')\b', flags=re.IGNORECASE)

    # Заменяем все вхождения на пустую строку
    value = regex_pattern.sub('', value)

    return mark_safe(value)
