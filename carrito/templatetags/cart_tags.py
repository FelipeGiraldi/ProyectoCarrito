from django import template

register = template.Library()


@register.filter()
def Multiplicar(value, arg):
    return (value) * arg


@register.filter()
def FormatoMoneda(value, arg):
    return f"{value}{arg}"