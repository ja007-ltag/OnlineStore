from django import template

register = template.Library()

CURRENCIES_SYMBOLS = {
    'rub': '₽',
    'usd': '$',
}


# Регистрируем наш фильтр под именем currency, чтобы Django понимал,
# что это именно фильтр для шаблонов, а не простая функция
@register.filter()
# @register.filter(name='currency_rub')  # можно сделать и так, у фильтра будет альтернативное название
def currency(value, code='rub'):
    """
    :value: значение, к которому нужно применить фильтр.
    :code: код валюты.
    """
    postfix = CURRENCIES_SYMBOLS[code]
    return f'{value} {postfix}'
