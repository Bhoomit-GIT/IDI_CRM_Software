# custom_filters.py

from django import template

register = template.Library()

@register.filter(name='addattr')
def addattr(field, attr):
    """Add attributes to a form field widget."""
    attrs = {}
    definition = attr.split(',')
    for d in definition:
        key, val = d.split(':')
        attrs[key] = val
    return field.as_widget(attrs=attrs)