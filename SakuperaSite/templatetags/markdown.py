from django import template
from django.template.defaultfilters import stringfilter
import markdown

register = template.Library()


@register.filter
@stringfilter
def to_markdown(value):
    html_output = markdown.markdown(value, extensions=[
        'fenced_code',
        'codehilite',
        'admonition',
        'tables',
        'markdown_mark'
    ])
    return (html_output)
