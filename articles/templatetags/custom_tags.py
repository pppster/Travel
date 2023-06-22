from django import template
from django.contrib.auth.models import User


register = template.Library()

users = User.objects.all()

@register.filter
def get_user_by_id(creator_id):
    return users.get(id=creator_id)