from django import template

register = template.Library()


@register.filter
def reverse_text(value):
    """
    يعكس النص
    """
    return str(value)[::-1]


@register.filter
def first_word(value):
    """
    يعرض أول كلمة فقط
    """
    return str(value).split()[0]


@register.filter
def currency(value):
    """
    يضيف رمز الدولار
    """
    return f"${value}"