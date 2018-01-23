from django import template

register = template.Library()


@register.inclusion_tag("class.html")
def self_model(Class_obj):
    print("---",type(Class_obj))
    user = Class_obj.user_info_set.all()

    return {"user":user}