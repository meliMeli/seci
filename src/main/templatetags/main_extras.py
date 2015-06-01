from django.template.defaulttags import register


@register.filter
def look_for(value, n):
    return value[n]
