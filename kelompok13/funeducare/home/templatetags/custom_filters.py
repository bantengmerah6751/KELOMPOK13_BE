from django import template

register = template.Library()

@register.filter
def split_paragraphs(value):
    if value:  # Pastikan value tidak None
        return value.split("\n")  # Pisahkan berdasarkan baris baru
    return []
