from django import template
register = template.Library()

@register.simple_tag
def row_css(cl, index):
    if not hasattr(cl.model_admin, 'get_row_css'):
        return u''
    return cl.model_admin.get_row_css(cl.result_list[index], index)
