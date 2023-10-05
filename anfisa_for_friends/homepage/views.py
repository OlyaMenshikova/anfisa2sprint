from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    # Запрос к БД, запрашиваем только нужные поля
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
        ).filter(
            is_published=True,
            is_on_main=True,
            category__is_published=True
        )
    # Полученный из БД QuerySet передаем в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаем в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)
