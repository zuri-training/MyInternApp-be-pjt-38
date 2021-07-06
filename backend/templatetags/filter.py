from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key):
    """
    returns the value turned into a list
    """
    return value.split(key)

@register.filter(name='reverse')
def reverse(value):
    """
    returns the reverse of the list
    """
    return value.reverse()