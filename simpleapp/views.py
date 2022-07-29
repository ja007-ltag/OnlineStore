# Импортируем класс, который говорит о том,
# что в этом представлении будет выводиться список объектов БД
from django.views.generic import ListView, DetailView
from .models import Product


class ProductList(ListView):
    # Указываем модель, объекты которой мы будем выводить.
    model = Product

    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'name'

    # queryset = Product.objects.filter(price__gte=200).\
    #     order_by('name')

    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'products.html'

    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'products'


class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Product

    # Используем другой шаблон - product.html
    template_name = 'product.html'

    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'product'

    pk_url_kwarg = 'id'
